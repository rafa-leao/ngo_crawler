scrapy runspider crawler/transparencia_social/transparencia_social/spiders/TransparenciaSocial.py
python helper/join_csv_files.py

echo "---------------------------------"
echo "Path to create final_file.csv:"
read path

echo ""
echo "Moving final_file.csv to ${path}"
echo ""
mv final_file.csv ${path}
rm -v *.csv
