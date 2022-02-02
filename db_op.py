import mysql.connector as mysql



class db_op():
    def __init__(self): # constructor with connection path to db
        self.connection = mysql.connect(
            host="34.121.245.150",
            user='root',
            password="Mpgradney2017",
            database = "streaming")
        self.cursor = self.connection.cursor()
        print("connection made..")

    # function for bulk inserting records
    def bulk_insert(self,query,records):
        self.cursor.executemany(query,records)
        self.connection.commit()
        print("query executed..")


    # function to return a single value from table
    def single_record(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]
        print("single record working")

    # close connection
    def destructor(self):
        self.connection.close()
        print("connection closed.")
