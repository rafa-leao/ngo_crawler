# -*- coding: utf-8 -*-
import scrapy
import json
import pandas

class TransparenciasocialSpider(scrapy.Spider):
    name = 'TransparenciaSocial'
    start_urls = ['http://transparenciasocial.com.br/ongs/listar/5?search=&length=5&page=1']     

    def parse(self, response):
        ongs = response.css('.ong_list_box')
        for ong in ongs:
            links_from_ong = ong.css('.trans3 ::attr(href)').extract()
            has_ver_mapa_link = len(links_from_ong) > 1 
            if has_ver_mapa_link:
                for link in links_from_ong:
                    if "/mapa?" not in link:
                        yield response.follow(link, self.parse_ong_link)
        
    def parse_ong_link(self, response):
        possible_ong_name = response.css('.name_ong_profile::text').get()       
        ong_nome = possible_ong_name if possible_ong_name is not None else response.css('h5::text').get() 
        
        ong_profile_list = response.css('.list_profile li')
        
        possible_ong_site = ong_profile_list.css('a::attr(href)').get()
        ong_site = possible_ong_site if possible_ong_site is not None else "Sem site"

        self.json_to_csv([{
            'nome': ong_nome ,
            'site': ong_site ,
            'link da ONG': response.url
        }], ong_nome)

    def json_to_csv(self, data, file_name):
        pandas.read_json(json.dumps(data)).to_csv(f'{file_name}.csv')
        