import mysql.connector as mysql
from csv_files import csv_files
from db_op import db_op
import csv

# connect to database
db_ops = db_op()

# load csv files and clean up data
netflix_csv = "netflix_titles.csv"
netflix_cleaned = csv_files.data_cleaner(netflix_csv)

hulu_csv = "hulu_titles.csv"
hulu_cleaned = csv_files.data_cleaner(hulu_csv)

disney_csv = "disney_plus_titles.csv"
disney_cleaned = csv_files.data_cleaner(disney_csv)

# update show id's to make them unique to each streaming site
netflix_data = []
hulu_data = []
disney_data = []

for row in netflix_cleaned[1:]:
    updated_id = row[0].replace("s", "N")
    netflix_row = [updated_id] + row[1:]
    netflix_data.append(netflix_row)
    

for row in hulu_cleaned[1:]:
    updated_id = row[0].replace("s", "H")
    hulu_row = [updated_id] + row[1:]
    hulu_data.append(hulu_row)

for row in disney_cleaned[1:]:
    updated_id = row[0].replace("s", "D")
    disney_row = [updated_id] + row[1:]
    disney_data.append(disney_row)


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
        attribute_count = len(netflix_data[0])
        placeholders = ("%s,"*attribute_count)[:-1]
        query = "INSERT INTO netflix(show_ID, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description) VALUES("+placeholders+")"
        db_ops.bulk_insert(query, netflix_data) 
    else:
        return 

pre_process_netflix()