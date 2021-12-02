import csv


class csv_files():

    netflix_csv = "netflix_titles.csv"
    hulu_csv = "hulu_titles.csv"
    disney_csv = "disney_plus_tiles.csv"

    # constructor
    def __init__(self): 
        pass

    # function parses a string and converts to appropriate type
    @staticmethod
    def convert(value):
        types = [int,float,str] # order needs to be this way
        if value == '':
            return None
        for t in types:
            try:
                return t(value)
            except:
                pass

    # function reads file path to clean up data file
    @staticmethod
    def data_cleaner(path):
        with open(path,"r",encoding="utf-8") as f:
            data = f.readlines()

        data = [i.strip().split(",") for i in data]
        data_cleaned = []
        for row in data[:]:
            row = [csv_files.convert(i) for i in row]
            data_cleaned.append(tuple(row))
        return data_cleaned

#    # loads streaming services files and cleans up data
#     def load_files():
#         netflix_data = self.data_cleaner(self.netflix_csv)
#         hulu_data = self.data_cleaner(self.hulu_csv)
#         disney_data = self.data_cleaner(self.disney_csv)
#         return [netflix_data, hulu_data, disney_data]
