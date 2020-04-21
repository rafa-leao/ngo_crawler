import pandas
import glob

list_of_files = [file for file in glob.glob('*.csv')]
result_obj = pandas.concat([pandas.read_csv(file) for file in list_of_files])
result_obj.to_csv("final_file.csv", index=False, encoding="utf-8")
