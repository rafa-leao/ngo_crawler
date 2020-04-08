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
            if len(links_from_ong) > 1:
                for link in links_from_ong:
                    if "/mapa?" not in link:
                        print(link)
                        # yield response.follow(link, self.parse_ong_link)
        
    def parse_ong_link(self, response):
        ong_profile_list = response.css('.list_profile li')

        # vc esta com problema nesse for aqui cara, cê só ta iterando de forma errada! bom dia <3
        for ong_profile in ong_profile_list: 
            ong_nome = response.css('.name_ong_profile::text').get()
            ong_link = ong_profile.css('a::attr(href)').get()
            ong_email = ong_profile.css('li::text').get()

            print("a.link", ong_link, "a.email", ong_email)

            if ong_link is None:
                ong_link = "ONG sem site cadastrado"

            if '@' not in ong_email:
                ong_email = "ONG sem email cadastrado"
                
            print("b.link", ong_link, "b.email", ong_email, "b.nome", ong_nome)

            # sending a list to self.json_to_csv is better for csv format, trust me!
            self.json_to_csv([{
                'nome': ong_nome,
                'link': ong_link,
                'email': ong_email
            }], response.css('title::text').get())

    def json_to_csv(self, data, file_name):
        pandas.read_json(json.dumps(data)).to_csv(f'{file_name}.csv')
        
        