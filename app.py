from tkinter import *
from tkinter import scrolledtext
import mysql.connector as mysql
from csv_files import csv_files
from db_op import db_op
import csv

#connect to database
db_ops = db_op()

#add data to Listbox
streaming_data = csv_files.data_cleaner("netflix_titles.csv")

root = Tk()
root.title('Streaminfo.com - Find what movies and shows are on what streaming service!')
root.geometry("600x300")


#update Listbox
def update(data):
    #clear Listbox
    list.delete(0,END)

    #add data to Listbox
    for item in data:
        list.insert(END, item)
#update entry box with listbox clicked
def fillout(event):
    #delete whatver is in the entry box
    searchbar.delete(0,END)
    #add clicked lit item to entry box
    searchbar.insert(0, list.get(ACTIVE))

#create function to check entry vs Listbox
def check(event):
    #grab what was is_empty_Expedition
    typed = searchbar.get()

    if typed == '':
        data = streaming_data
    else:
        data = []
        for item in streaming_data:
            if typed.lower() in item.lower():
                data.append(item)
    #update listbox
    update(data)


#create label
my_label = Label(root, text = "Start typing...",
font =("Helvetica", 14), fg="blue")
my_label.pack(pady=20)

#searchbar
searchbar = Entry(root, font=("Helvetica", 20))
searchbar.pack()




#listbox
filepath = '/Users/madeleinegradney/Desktop/CPSC_408_Ra0/Final_Project/netflix_titles.csv'

file = open(filepath)
reader = csv.reader(file)
streaming_data = list(reader)
#del(data[0])

#list_of_entries = []
#for x in list(range(0,len(data))):
    #list_of_entries.append(data[x][0])
#var = StringVar(value = list_of_entries)
list = Listbox(root)
list.grid(row=0, column=0)
list.pack(pady=40)

update(streaming_data)



#binding on the list Listbox
list.bind("<<ListboxSelect>>", fillout)

#binding on search
searchbar.bind("<KeyRelease>", check)

#______________________________________________________________________________#
#Treeview
from tkinter import *
from tkinter import ttks
from tkinter import scrolledtext
import mysql.connector as mysql
from csv_files import csv_files
from db_op import db_op
import csv

#connect to database
db_ops = db_op()
#data for db
streaming_data = csv_files.data_cleaner("netflix_titles.csv")

#gui
root = Tk()
root.title("Streaminfo.com -- see what streaming site what movie/show you want to watch is on")

root.geometry("10000x550")

TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
#defining
tree = ttk.Treeview(TableMargin, columns=("show_id", "type", "title", "director", "cast", "country", "date_added","release_year", "rating", "duration", "listed_in", "description", "streaming_site"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('show_id', text="show_id", anchor=W)
tree.heading('type', text="type", anchor=W)
tree.heading('title', text="title", anchor=W)
tree.heading('director', text="director", anchor=W)
tree.heading('cast', text="cast", anchor=W)
tree.heading('country', text="country", anchor=W)
tree.heading('date_added', text="date_added", anchor=W)
tree.heading('release_year', text="release_year", anchor=W)
tree.heading('rating', text="rating", anchor=W)
tree.heading('duration', text="duration", anchor=W)
tree.heading('listed_in', text="listed_in", anchor=W)
tree.heading('description', text="description", anchor=W)
tree.heading('streaming_site', text="streaming_site", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()

with open('netflix_titles.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        show_id = row['show_id']
        type = row['type']
        title = row['title']
        director = row['director']
        cast = row['cast']
        country = row['country']
        date_added = row['date_added']
        release_year = row['release_year']
        rating = row['rating']
        duration = row['duration']
        listed_in = row['listed_in']
        description = row['description']
        streaming_site = row['streaming_site']
        tree.insert("", 0, values=(show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description, streaming_site))



#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()




#streaming_databases

root.mainloop()
