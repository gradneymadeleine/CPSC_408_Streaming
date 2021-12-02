import mysql.connector as mysql

mydb = mysql.connect(
host="34.121.245.150",
user='root',
password="Mpgradney2017"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE streaming")
