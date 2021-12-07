from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import mysql.connector as mysql
from csv_files import csv_files
from tkinter import messagebox
import csv
#from insert import insert


#connect to database
conn = mysql.connect(
host="34.121.245.150",
user='root',
password="Mpgradney2017",
database = "streaming")


cur = conn.cursor()
print("Connection made...")


cur.execute('''CREATE TABLE if not exists netflix (
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
show_movies VARCHAR(10),
title VARCHAR(250),
director VARCHAR(300),
actors VARCHAR(800),
country VARCHAR(550),
date_added VARCHAR(20),
release_year VARCHAR(7),
rating VARCHAR(10),
duration VARCHAR(20),
listed_in VARCHAR(100),
summary VARCHAR(8000)

)''')

cur.execute(''' CREATE TABLE if not exists watchlist (
show_id VARCHAR(10) NOT NULL PRIMARY KEY,
show_movies VARCHAR(10),
title VARCHAR(250),
director VARCHAR(300),
actors VARCHAR(800),
country VARCHAR(550),
date_added VARCHAR(20),
release_year VARCHAR(7),
rating VARCHAR(10),
duration VARCHAR(20),
listed_in VARCHAR(100),
summary VARCHAR(8000)

)''')

print("Created tables")


file = open('netflix_titles.csv')
netflix_csv = csv.reader(file)
next(netflix_csv)



#for row in netflix_csv:
#    netflix_data = cur.execute('INSERT INTO netflix(show_ID, show_movies, title, director, actors, country, date_added, release_year, rating, duration, listed_in, summary)' 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)

conn.commit()


def query_database_net():
    #global show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description
    conn = mysql.connect(
    host="34.121.245.150",
    user='root',
    password="Mpgradney2017",
    database = "streaming")

    cur = conn.cursor()

    cur.execute("SELECT DISTINCT * FROM netflix")
    records = cur.fetchall()


    global count
    count = 0

    for row in records:
        show_id = row[0]
        type = row[1]
        title = row[2]
        director = row[3]
        cast = row[4]
        country = row[5]
        date_added = row[6]
        release_year = row[7]
        rating = row[8]
        duration = row[9]
        listed_in = row[10]
        description = row[11]

        if count % 2 ==0:
            tree.insert("",0, values=(show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description), tags=('evenrow',))
        else:
            tree.insert("",0, values=(show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description), tags=('oddrow',))
        count += 1

    conn.commit()

def query_database_watch():
    conn = mysql.connect(
    host="34.121.245.150",
    user='root',
    password="Mpgradney2017",
     database = "streaming")

    cur = conn.cursor()



    cur.execute("SELECT DISTINCT * FROM watchlist")
    records = cur.fetchall()

    global count
    count = 0

    for row in records:
        show_id = row[0]
        type = row[1]
        title = row[2]
        director = row[3]
        cast = row[4]
        country = row[5]
        date_added = row[6]
        release_year = row[7]
        rating = row[8]
        duration = row[9]
        listed_in = row[10]
        description = row[11]

        if count % 2 ==0:
            watch.insert("", 0, values=( show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description), tags=('evenrow',))
        else:
            watch.insert("", 0, values=(show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description), tags=('oddrow',))
        count += 1

    conn.commit()
    conn.close()

#create binding click function
def clicker(event):
    select_record_tree()

def clicker_watch(event):
    select_record_watch()


def add_record():
    conn = mysql.connect(
    host="34.121.245.150",
    user='root',
    password="Mpgradney2017",
    database = "streaming")

    cur = conn.cursor()



    add_data = s_id_box.get(),type_box.get(),title_box.get(),director_box.get(),cast_box.get(),country_box.get(),date_added_box.get(),release_year_box.get(),rating_box.get(),duration_box.get(),listed_in_box.get(),description_box.get()
    add_data_button=iter(add_data)
    next(add_data_button)

    #for row in add_data:
    val = (s_id_box.get(),type_box.get(),title_box.get(),director_box.get(),cast_box.get(),country_box.get(),date_added_box.get(),release_year_box.get(),rating_box.get(),duration_box.get(),listed_in_box.get(),description_box.get())
    query = 'INSERT INTO watchlist(show_ID, show_movies, title, director, actors, country, date_added, release_year, rating, duration, listed_in, summary)' 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)'
    cur.execute(query, val)
    conn.commit()
    conn.close()

    #clear treeview table
    watch.delete(*watch.get_children())


    query_database_watch()

def update_record():
    conn = mysql.connect(
    host="34.121.245.150",
    user='root',
    password="Mpgradney2017",
    database = "streaming")

    cur = conn.cursor()

    # selected = watch.focus()
    #
    # watch.item(selected, text="", values=(s_id_box.get(),type_box.get(),title_box.get(),director_box.get(),cast_box.get(),country_box.get(),date_added_box.get(),release_year_box.get(),rating_box.get(),duration_box.get(),listed_in_box.get(),description_box.get()))
    #
    #
    # cur.execute("""UPDATE watchlist SET
    #
    # show_ID = %s ,
    # show_movies = %s,
    # title, director = %s,
    # actors = %s,
    # country = %s,
    # date_added = %s,
    # release_year = %s,
    # rating = %s,
    # duration = %s,
    # listed_in = %s,
    # summary = %s
    #
    # WHERE oid = :oid""",
    # {
    #
    #
    # }
    #
    #
    # )



def delete_record():
    conn = mysql.connect(
    host="34.121.245.150",
    user='root',
    password="Mpgradney2017",
    database = "streaming")

    cur = conn.cursor()
    #delete from database
    selected = title_box2.get()
    selected_data=iter(selected)
    next(selected_data)

    query = "DELETE FROM watchlist WHERE title = %s"
    value = (selected,)
    cur.execute(query,value)

    conn.commit()
    conn.close()



    #add message Boxes
    messagebox.showinfo("Deleted!", "Your Record has been deleted!")

    watch.delete(*watch.get_children())
    query_database_watch()

def search_records():

    #clear Treeview

    conn = mysql.connect(
    host="34.121.245.150",
    user='root',
    password="Mpgradney2017",
    database = "streaming")

    cur = conn.cursor()

    lookup_record = search_entry.get()
    #close search box
    search.destroy()

    search_query ="SELECT * FROM netflix WHERE title LIKE %s"
    val = (lookup_record,)
    cur.execute(search_query, val)
    records=cur.fetchall()

    tree.delete(*tree.get_children())

    global count
    count = 0

    for row in records:
        show_id = row[0]
        type = row[1]
        title = row[2]
        director = row[3]
        cast = row[4]
        country = row[5]
        date_added = row[6]
        release_year = row[7]
        rating = row[8]
        duration = row[9]
        listed_in = row[10]
        description = row[11]

        if count % 2 == 0:
            tree.insert("", 0, values=( show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description), tags=('evenrow',))
        else:
            tree.insert("", 0, values=(show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description), tags=('oddrow',))
        count += 1

    conn.commit()
    conn.close()



def lookup_records():
    global search_entry, search
    search = Toplevel(root)
    search.title("Lookup Records")
    root.geometry("1500x700")


    #create Label
    search_frame = LabelFrame(search, text="Title of Show/Movie")
    search_frame.pack(fill = "x", expand = "yes", padx= 30)

    #add entry box
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.grid(row=0,column=4, padx=10, pady=10)

    #add Button
    search_button = ttk.Button(search_frame, text= "Search Records", command=search_records)
    search_button.grid(row=2, column=4, padx=20, pady=20)











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
tree['columns']=("show_id", "type", "title", "director", "cast", "country", "date_added","release_year", "rating", "duration", "listed_in", "description" )
#create columns
tree.column('#0', width=0)
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

#with open('netflix_titles.csv') as f:
#    reader = csv.DictReader(f, delimiter=',')



#add record entry boxes







#add to watchlist button
#add record entry boxes





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
watch['columns']=( "show_id", "type", "title", "director", "cast", "country", "date_added","release_year", "rating", "duration", "listed_in", "description" )
#create columns
watch.column('#0', width=0)
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

w_button_frame = LabelFrame(watchlist_frame, text="Records")
w_button_frame.pack(fill = "x", expand = "yes", padx= 30)

i1 = Label(w_button_frame, text="show_id")
i1.grid(row=0, column=0, padx = 7, pady =7)
s_id_box2 = Entry(w_button_frame)
s_id_box2.grid(row=0, column=1, padx = 7, pady =7)

t1 = Label(w_button_frame, text = "type")
t1.grid(row=0, column=2, padx = 7, pady =7)
type_box2 = Entry(w_button_frame)
type_box2.grid(row=0, column=3,padx = 7, pady =7)

title1 = Label(w_button_frame, text = "title")
title1.grid(row=0, column=4, padx = 7, pady =7)
title_box2 = Entry(w_button_frame)
title_box2.grid(row=0, column=5, padx = 7, pady =7)

d1 = Label(w_button_frame, text = "director")
d1.grid(row=1, column=0,padx = 7, pady =7)
director_box2 = Entry(w_button_frame)
director_box2.grid(row=1, column=1,padx = 7, pady =7)

c1 = Label(w_button_frame, text = "cast")
c1.grid(row=1, column=2, padx = 7, pady =7)
cast_box2 = Entry(w_button_frame)
cast_box2.grid(row=1, column=3, padx = 7, pady =7)

country1 = Label(w_button_frame, text = "country")
country1.grid(row=1, column=4, padx = 7, pady =7)
country_box2 = Entry(w_button_frame)
country_box2.grid(row=1, column=5, padx = 7, pady =7)

date_added1 = Label(w_button_frame, text = "date_added")
date_added1.grid(row=2, column=0, padx = 7, pady =7)
date_added_box2 = Entry(w_button_frame)
date_added_box2.grid(row=2, column=1, padx = 7, pady =7)

release_year1 = Label(w_button_frame, text = "release_year")
release_year1.grid(row=2, column=2, padx = 7, pady =7)
release_year_box2 = Entry(w_button_frame)
release_year_box2.grid(row=2, column=3, padx = 7, pady =7)

r1 = Label(w_button_frame, text = "rating")
r1.grid(row=2, column=4, padx = 7, pady =7)
rating_box2 = Entry(w_button_frame)
rating_box2.grid(row=2, column=5, padx = 7, pady =7)

duration1 = Label(w_button_frame, text = "duration")
duration1.grid(row=3, column=0, padx = 7, pady =7)
duration_box2 = Entry(w_button_frame)
duration_box2.grid(row=3, column=1, padx = 7, pady =7)

l1 = Label(w_button_frame, text = "listed_in")
l1.grid(row=3, column=2, padx = 7, pady =7)
listed_in_box2 = Entry(w_button_frame)
listed_in_box2.grid(row=3, column=3, padx = 7, pady =7)

description1 = Label(w_button_frame, text = "description")
description1.grid(row=3, column=4, padx = 7, pady =7)
description_box2 = Entry(w_button_frame)
description_box2.grid(row=3, column=5, padx = 7, pady =7)

#update to watchlist Button
update_button = ttk.Button(w_button_frame, text ="Update Record", command = update_record)
update_button.grid(row=3, column=6, padx =7, pady=7)

delete_button = ttk.Button(w_button_frame, text ="Delete Record", command = delete_record)
delete_button.grid(row=3, column=7, padx =7, pady=7)
#create striped row tags

watch.tag_configure('oddrow', background= "white")
watch.tag_configure('evenrow', background= "light blue")

#add record entry boxes
data_frame = LabelFrame(database_frame, text="Record")
data_frame.pack(fill = "x", expand = "yes", padx= 20)


i1 = Label(data_frame, text="show_id")
i1.grid(row=0, column=0, padx = 7, pady =7)
s_id_box = Entry(data_frame)
s_id_box.grid(row=0, column=1, padx = 7, pady =7)

t1 = Label(data_frame, text = "type")
t1.grid(row=0, column=2, padx = 7, pady =7)
type_box = Entry(data_frame)
type_box.grid(row=0, column=3,padx = 7, pady =7)

title1 = Label(data_frame, text = "title")
title1.grid(row=0, column=4, padx = 7, pady =7)
title_box = Entry(data_frame)
title_box.grid(row=0, column=5, padx = 7, pady =7)

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
add_button = ttk.Button(data_frame, text ="Add Record", command = add_record)
add_button.grid(row=3, column=7, padx =7, pady=7)

#create striped row tags
tree.tag_configure('oddrow', background= "white")
tree.tag_configure('evenrow', background= "light blue")
#binding

watch.bind("<ButtonRelease-1>", clicker_watch)

#adding Button


def select_record_tree():

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


    #grab record VALUES
    values = tree.item(selected, 'values')


    s_id_box.insert(0, values[0])
    type_box.insert(0, values[1])
    title_box.insert(0, values[2])
    director_box.insert(0, values[3])
    cast_box.insert(0, values[4])
    country_box.insert(0, values[5])
    date_added_box.insert(0, values[6])
    release_year_box.insert(0, values[7])
    rating_box.insert(0, values[8])
    duration_box.insert(0, values[9])
    listed_in_box.insert(0, values[10])
    description_box.insert(0, values[11])


#clear boxes
    #s_id_box.delete(0, END)
    #type_box.delete(0, END)
    #title_box.delete(0, END)
    #director_box.delete(0, END)
    #cast_box.delete(0, END)
    #country_box.delete(0, END)
    #date_added_box.delete(0, END)
    #release_year_box.delete(0, END)
    #rating_box.delete(0, END)
    #duration_box.delete(0, END)
    #listed_in_box.delete(0, END)
    #description_box.delete(0, END)
def select_record_watch():

    s_id_box2.delete(0,END)
    type_box2.delete(0,END)
    title_box2.delete(0,END)
    director_box2.delete(0,END)
    cast_box2.delete(0,END)
    country_box2.delete(0,END)
    date_added_box2.delete(0,END)
    release_year_box2.delete(0,END)
    rating_box2.delete(0,END)
    duration_box2.delete(0,END)
    listed_in_box2.delete(0,END)
    description_box2.delete(0,END)

    #Grab record number
    selected = watch.focus()


    #grab record VALUES
    values = watch.item(selected, 'values')


    s_id_box2.insert(0, values[0])
    type_box2.insert(0, values[1])
    title_box2.insert(0, values[2])
    director_box2.insert(0, values[3])
    cast_box2.insert(0, values[4])
    country_box2.insert(0, values[5])
    date_added_box2.insert(0, values[6])
    release_year_box2.insert(0, values[7])
    rating_box2.insert(0, values[8])
    duration_box2.insert(0, values[9])
    listed_in_box2.insert(0, values[10])
    description_box2.insert(0, values[11])



#binding

tree.bind("<ButtonRelease-1>", clicker)

#search menu
my_menu = Menu(root)
root.config(menu=my_menu)

#option Menu
# option_menu = Menu(my_menu, tearoff=0)
# my_menu.add_cascade(label="Option")
#add to watchlist Button
search_menu_button = ttk.Button(data_frame, text ="Search Record", command = lookup_records)
search_menu_button.grid(row=3, column=8, padx =7, pady=7)

reset_button = ttk.Button(data_frame, text ="Back to Records", command = query_database_net)
reset_button.grid(row=3, column=9, padx =7, pady=7)



# run to pull data rrom database on start
query_database_net()
query_database_watch()

#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()
