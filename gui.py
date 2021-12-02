from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import mysql.connector as mysql
from csv_files import csv_files
from db_op import db_op#
import csv

#connect to database
db_ops = db_op()
#data for db
streaming_data = csv_files.data_cleaner("netflix_titles.csv")

def select_record():
    s_s_box.delete(0,END)
    s_id_box.delete(0,END)
    type_box.delete(0,END)
    title_box.delete(0,END)
    director_box.delete(0,END)
    cast_box.delete(0,END)
    country_box.delete(0,END)
    date_added_box.delete(0,END)
    release_year_box.delete(0,END)
    rating_box.delete(0,END)
    duration_box.delete(0,END)
    listed_in_box.delete(0,END)
    description_box.delete(0,END)

    #Grab record number
    selected = tree.focus()
    select = watch.focus()
    #grab record VALUES
    values = tree.item(selected, 'values')
    value = watch.item(select, 'values')

    s_s_box.insert(0, values[0])
    s_id_box.insert(0, values[1])
    type_box.insert(0, values[2])
    title_box.insert(0, values[3])
    director_box.insert(0, values[4])
    cast_box.insert(0, values[5])
    country_box.insert(0, values[6])
    date_added_box.insert(0, values[7])
    release_year_box.insert(0, values[8])
    rating_box.insert(0, values[9])
    duration_box.insert(0, values[10])
    listed_in_box.insert(0, values[11])
    description_box.insert(0, values[12])


#create binding click function
def clicker(event):
    select_record()


#add record
def add_record():
    watch.insert("", 0, values=(s_s_box.get(), s_id_box.get(), type_box.get(), title_box.get(), director_box.get(), cast_box.get(), country_box.get(), date_added_box.get(), release_year_box.get(), rating_box.get(), duration_box.get(), listed_in_box.get(), description_box.get()))

#clear boxes
    s_s_box.delete(0, END)
    s_id_box.delete(0, END)
    type_box.delete(0, END)
    title_box.delete(0, END)
    director_box.delete(0, END)
    cast_box.delete(0, END)
    country_box.delete(0, END)
    date_added_box.delete(0, END)
    release_year_box.delete(0, END)
    rating_box.delete(0, END)
    duration_box.delete(0, END)
    listed_in_box.delete(0, END)
    description_box.delete(0, END)










#gui
root = Tk()
root.title("Streaminfo.com -- see what streaming site what movie/show you want to watch is on")
root.geometry("1500x700")


tabs = ttk.Notebook(root)
tabs.pack(pady=15)

database_frame = Frame(tabs, width=1500, height=700)
watchlist_frame = Frame(tabs, width=1500, height=700)

database_frame.pack(fill="both", expand=1)
watchlist_frame.pack(fill="both", expand=1)

tabs.add(database_frame, text = 'Streaming Sites')
tabs.add(watchlist_frame, text = 'Your Watchlist')
#styling gui
style = ttk.Style()
#theme
style.theme_use("default")

#confiuge treeview colors
style.configure("Treeview",
background = "#D3D3D3",
foreground="black",
rowheight=25,
fieldbackground="#D3D3D3")

#change slected color
style.map('Treeview',
background=[('selected', '#347083')])

TableMargin = Frame(database_frame, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

#-------streaming site tab-------

#create treeview
tree = ttk.Treeview(TableMargin, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree['columns']=("streaming_site", "show_id", "type", "title", "director", "cast", "country", "date_added","release_year", "rating", "duration", "listed_in", "description" )
#create columns
tree.column('#0', width=0)
tree.column('streaming_site',anchor=W, width=110)
tree.column('show_id', anchor=W, width=80)
tree.column('type', anchor=W, width=120)
tree.column('title', anchor=W, width=120)
tree.column('director',anchor=W, width=120)
tree.column('cast', anchor=W, width=400)
tree.column('country',anchor=W, width=150)
tree.column('date_added', anchor=W, width=175)
tree.column('release_year', anchor=W, width=120)
tree.column('rating', anchor=W, width=120)
tree.column('duration', anchor=W, width=120)
tree.column('listed_in', anchor=W, width=300)
tree.column('description', anchor=W, width=500)

#create headings
tree.heading('streaming_site', text="streaming_site", anchor=W)
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

tree.pack(pady=30)

with open('netflix_titles.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    count = 0
    for row in reader:
        streaming_site = row['streaming_site']
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

        if count % 2 ==0:
            tree.insert("", 0, values=(streaming_site, show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description), tags=('evenrow',))
        else:
            tree.insert("", 0, values=(streaming_site, show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description), tags=('oddrow',))
        count += 1

#add record entry boxes
w_data_frame = LabelFrame(watchlist_frame, text="Record")
w_data_frame.pack(fill = "x", expand = "yes", padx= 20)


s1 = Label(w_data_frame, text = "streaming_site")
s1.grid(row=0, column=0, padx = 7, pady =7)
s_s_box = Entry(w_data_frame)
s_s_box.grid(row=0, column=1, padx = 7, pady =7)

i1 = Label(w_data_frame, text="show_id")
i1.grid(row=0, column=2, padx = 7, pady =7)
s_id_box = Entry(w_data_frame)
s_id_box.grid(row=0, column=3, padx = 7, pady =7)

t1 = Label(w_data_frame, text = "type")
t1.grid(row=0, column=4, padx = 7, pady =7)
type_box = Entry(w_data_frame)
type_box.grid(row=0, column=5,padx = 7, pady =7)

title1 = Label(w_data_frame, text = "title")
title1.grid(row=0, column=6, padx = 7, pady =7)
title_box = Entry(w_data_frame)
title_box.grid(row=0, column=7, padx = 7, pady =7)

d1 = Label(w_data_frame, text = "director")
d1.grid(row=1, column=0,padx = 7, pady =7)
director_box = Entry(w_data_frame)
director_box.grid(row=1, column=1,padx = 7, pady =7)


c1 = Label(w_data_frame, text = "cast")
c1.grid(row=1, column=2, padx = 7, pady =7)
cast_box = Entry(w_data_frame)
cast_box.grid(row=1, column=3, padx = 7, pady =7)

country1 = Label(w_data_frame, text = "country")
country1.grid(row=1, column=4, padx = 7, pady =7)
country_box = Entry(w_data_frame)
country_box.grid(row=1, column=5, padx = 7, pady =7)

date_added1 = Label(w_data_frame, text = "date_added")
date_added1.grid(row=2, column=0, padx = 7, pady =7)
date_added_box = Entry(w_data_frame)
date_added_box.grid(row=2, column=1, padx = 7, pady =7)

release_year1 = Label(w_data_frame, text = "release_year")
release_year1.grid(row=2, column=2, padx = 7, pady =7)
release_year_box = Entry(w_data_frame)
release_year_box.grid(row=2, column=3, padx = 7, pady =7)

r1 = Label(w_data_frame, text = "rating")
r1.grid(row=2, column=4, padx = 7, pady =7)
rating_box = Entry(w_data_frame)
rating_box.grid(row=2, column=5, padx = 7, pady =7)

duration1 = Label(w_data_frame, text = "duration")
duration1.grid(row=3, column=0, padx = 7, pady =7)
duration_box = Entry(w_data_frame)
duration_box.grid(row=3, column=1, padx = 7, pady =7)

l1 = Label(w_data_frame, text = "listed_in")
l1.grid(row=3, column=2, padx = 7, pady =7)
listed_in_box = Entry(w_data_frame)
listed_in_box.grid(row=3, column=3, padx = 7, pady =7)

description1 = Label(w_data_frame, text = "description")
description1.grid(row=3, column=4, padx = 7, pady =7)
description_box = Entry(w_data_frame)
description_box.grid(row=3, column=5, padx = 7, pady =7)


tree.bind("<ButtonRelease-1>", clicker)

#add to watchlist button




#-------------- watchlist tab---------------


tableList = Frame(watchlist_frame, width=500)
tableList.pack(side=TOP)
scrollbarx = Scrollbar(tableList, orient=HORIZONTAL)
scrollbary = Scrollbar(tableList, orient=VERTICAL)

#create treeview
watch = ttk.Treeview(tableList, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=watch.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=watch.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
watch['columns']=("streaming_site", "show_id", "type", "title", "director", "cast", "country", "date_added","release_year", "rating", "duration", "listed_in", "description" )
#create columns
watch.column('#0', width=0)
watch.column('streaming_site',anchor=W, width=110)
watch.column('show_id', anchor=W, width=80)
watch.column('type', anchor=W, width=120)
watch.column('title', anchor=W, width=120)
watch.column('director',anchor=W, width=120)
watch.column('cast', anchor=W, width=400)
watch.column('country',anchor=W, width=150)
watch.column('date_added', anchor=W, width=175)
watch.column('release_year', anchor=W, width=120)
watch.column('rating', anchor=W, width=120)
watch.column('duration', anchor=W, width=120)
watch.column('listed_in', anchor=W, width=300)
watch.column('description', anchor=W, width=500)

#create headings
watch.heading('streaming_site', text="streaming_site", anchor=W)
watch.heading('show_id', text="show_id", anchor=W)
watch.heading('type', text="type", anchor=W)
watch.heading('title', text="title", anchor=W)
watch.heading('director', text="director", anchor=W)
watch.heading('cast', text="cast", anchor=W)
watch.heading('country', text="country", anchor=W)
watch.heading('date_added', text="date_added", anchor=W)
watch.heading('release_year', text="release_year", anchor=W)
watch.heading('rating', text="rating", anchor=W)
watch.heading('duration', text="duration", anchor=W)
watch.heading('listed_in', text="listed_in", anchor=W)
watch.heading('description', text="description", anchor=W)

watch.pack(pady=30)


#add record entry boxes
data_frame = LabelFrame(database_frame, text="Record")
data_frame.pack(fill = "x", expand = "yes", padx= 20)


s1 = Label(data_frame, text = "streaming_site")
s1.grid(row=0, column=0, padx = 7, pady =7)
s_s_box = Entry(data_frame)
s_s_box.grid(row=0, column=1, padx = 7, pady =7)

i1 = Label(data_frame, text="show_id")
i1.grid(row=0, column=2, padx = 7, pady =7)
s_id_box = Entry(data_frame)
s_id_box.grid(row=0, column=3, padx = 7, pady =7)

t1 = Label(data_frame, text = "type")
t1.grid(row=0, column=4, padx = 7, pady =7)
type_box = Entry(data_frame)
type_box.grid(row=0, column=5,padx = 7, pady =7)

title1 = Label(data_frame, text = "title")
title1.grid(row=0, column=6, padx = 7, pady =7)
title_box = Entry(data_frame)
title_box.grid(row=0, column=7, padx = 7, pady =7)

d1 = Label(data_frame, text = "director")
d1.grid(row=1, column=0,padx = 7, pady =7)
director_box = Entry(data_frame)
director_box.grid(row=1, column=1,padx = 7, pady =7)


c1 = Label(data_frame, text = "cast")
c1.grid(row=1, column=2, padx = 7, pady =7)
cast_box = Entry(data_frame)
cast_box.grid(row=1, column=3, padx = 7, pady =7)

country1 = Label(data_frame, text = "country")
country1.grid(row=1, column=4, padx = 7, pady =7)
country_box = Entry(data_frame)
country_box.grid(row=1, column=5, padx = 7, pady =7)

date_added1 = Label(data_frame, text = "date_added")
date_added1.grid(row=2, column=0, padx = 7, pady =7)
date_added_box = Entry(data_frame)
date_added_box.grid(row=2, column=1, padx = 7, pady =7)

release_year1 = Label(data_frame, text = "release_year")
release_year1.grid(row=2, column=2, padx = 7, pady =7)
release_year_box = Entry(data_frame)
release_year_box.grid(row=2, column=3, padx = 7, pady =7)

r1 = Label(data_frame, text = "rating")
r1.grid(row=2, column=4, padx = 7, pady =7)
rating_box = Entry(data_frame)
rating_box.grid(row=2, column=5, padx = 7, pady =7)

duration1 = Label(data_frame, text = "duration")
duration1.grid(row=3, column=0, padx = 7, pady =7)
duration_box = Entry(data_frame)
duration_box.grid(row=3, column=1, padx = 7, pady =7)

l1 = Label(data_frame, text = "listed_in")
l1.grid(row=3, column=2, padx = 7, pady =7)
listed_in_box = Entry(data_frame)
listed_in_box.grid(row=3, column=3, padx = 7, pady =7)

description1 = Label(data_frame, text = "description")
description1.grid(row=3, column=4, padx = 7, pady =7)
description_box = Entry(data_frame)
description_box.grid(row=3, column=5, padx = 7, pady =7)

#add to watchlist Button
add_record = Button(data_frame, text ="Add Record")
add_record.grid(row=3, column=6, padx =7, pady=7)

#create striped row tags
tree.tag_configure('oddrow', background= "white")
tree.tag_configure('evenrow', background= "light blue")
watch.tag_configure('oddrow', background= "white")
watch.tag_configure('evenrow', background= "light blue")
#binding

watch.bind("<ButtonRelease-1>", clicker)

#adding Button
w_button_frame = LabelFrame(watchlist_frame, text="Configure")
w_button_frame.pack(fill = "x", expand = "yes", padx= 20)




#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()
