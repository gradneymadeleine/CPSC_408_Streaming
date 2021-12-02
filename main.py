import mysql.connector as mysql
from csv_files import csv_files
from db_op import db_op
import csv

# connect to database
db_ops = db_op()

# load csv files and clean up data
netflix_csv = "netflix_titles.csv"
netflix_data = csv_files.data_cleaner(netflix_csv)

hulu_csv = "hulu_titles.csv"
hulu_data = csv_files.data_cleaner(hulu_csv)

disney_csv = "disney_plus_titles.csv"
disney_data = csv_files.data_cleaner(disney_csv)


#  insert data
def is_empty_netflix():
   query = '''
   SELECT COUNT(*)
   FROM netflix;
   '''
   result = db_ops.single_record(query)
   return result == 0

def pre_process_netflix():
    if is_empty_netflix():
        attribute_count = len(netflix_data)
        placeholders = ("%s,"*attribute_count)[:-1]
        query = '''INSERT INTO netflix(show_ID, type, title, director, cast, country, 
                    date_added, release_year, rating, duration, listed_in, description) VALUES("+placeholders+")'''
        db_ops.bulk_insert(query, netflix_data) 
    else:
        return 

pre_process_netflix()