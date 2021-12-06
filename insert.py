import csv
import mysql.connector as mysql





conn = mysql.connect(
host="34.121.245.150",
user='root',
password="Mpgradney2017",
database = "streaming")


cur = conn.cursor()
print("Connection made...")


file = open('netflix_titles.csv')
netflix_csv = csv.reader(file)
next(netflix_csv)


print("after true")

for row in netflix_csv:
    print("after continue")
    netflix_data = cur.execute('INSERT INTO netflix(show_ID, show_movies, title, director, actors, country, date_added, release_year, rating, duration, listed_in, summary)' 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)

    #query = "LOAD DATA INFILE 'C:/Users/madeleinegradney/Desktop/CPSC_408_Ra0/CPSC_408_Streaming/netfix_titles.csv' INTO TABLE netflix FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (show_ID, show_movies, title, director, actors, country, date_added, release_year, rating, duration, listed_in, summary)"

    #cur.execute(query)
    conn.commit()

print("query committed")
