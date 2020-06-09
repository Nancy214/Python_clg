from tkinter import *
from tkinter import ttk
from datetime import datetime
import sqlite3 as db
from matplotlib import pyplot as plt

#Making a table if it does not exist
conn = db.connect("Expense.db")
cur = conn.cursor()
sql = '''
create table if not exists expenses (
    date str,
    time str,
    amount number,
    category str,
    description str
    )
'''
cur.execute(sql)
conn.commit()
    
#GUI
root=Tk()
root.geometry("700x700")
root.title("Daily Expense Tracker")
today_date = datetime.today().strftime('%d-%m-%Y')
today_time = datetime.today().strftime('%H:%M:%S')

tabs = ttk.Notebook(root)
add_entry_tab = ttk.Frame(tabs)
view_tab = ttk.Frame(tabs)
stats_tab = ttk.Frame(tabs)
tabs.add(add_entry_tab, text=" Add Entry ")
tabs.add(view_tab, text="   View   ")
tabs.add(stats_tab, text="  Stats  ")


#Add entry tab
def add_entry():
    amount = e1.get()
    category = clicked.get()
    description = e3.get()

    conn = db.connect("Expense.db")
    cur = conn.cursor()
    sql = '''
    insert into expenses values (
        '{}',
        '{}',
        {},
        '{}',
        '{}'
        
        )
    '''.format(today_date,today_time,amount,category,description)
    cur.execute(sql)
    conn.commit()

    e1.delete(0, END)
    clicked.set("Choose Category")
    e3.delete(0, END)

label0 = Label(add_entry_tab, text="Your Daily Expense Tracker",justify='center',compound='center',font = ("Times New Roman",30))
label1 = Label(add_entry_tab, text="Date")
label_date = Label(add_entry_tab, text=today_date)
label_time = Label(add_entry_tab, text=today_time)
label2 = Label(add_entry_tab, text="Amount")
label3 = Label(add_entry_tab, text="Category")
label4 = Label(add_entry_tab, text="Description")
add_button = Button(add_entry_tab,text="Add",command=add_entry)

e1 = Entry(add_entry_tab)
options = ["Food","Transportation","Household","Self-Care","Health","Education","Gifts","Other"]
clicked = StringVar()
clicked.set("Choose Category")
e2 = OptionMenu(add_entry_tab,clicked,*options)
e3 = Entry(add_entry_tab)

tabs.pack(expand=1,fill="both")
label0.grid(row=0,column=0,columnspan=6)
label1.grid(row=1,column=0,rowspan = 3)
label2.grid(row=4,column=0,rowspan = 3)
label3.grid(row=7,column=0,rowspan = 3)
label4.grid(row=10,column=0,rowspan = 3)

label_date.grid(row=1,column=1)
label_time.grid(row=1,column=2)
e1.grid(row=4,column=1,columnspan=2)
e2.grid(row=7,column=1,columnspan=2)
e3.grid(row=10,column=1,columnspan=2)
add_button.grid(row=13,column=2,columnspan=3)

#View Tab
def view_today():
    conn = db.connect("Expense.db")
    cur = conn.cursor()
    sql1 = '''
    select * from expenses where date = '{}'
    '''.format(today_date)
    sql2 = '''
    select sum(amount) from expenses where date = '{}'
    '''.format(today_date)
    cur.execute(sql1)
    result = cur.fetchall()
    cur.execute(sql2)
    total = cur.fetchone()[0]

    label_date = Label(view_tab, text="Date")
    label_time = Label(view_tab, text="Time")
    label_amount = Label(view_tab, text="Amount")
    label_category = Label(view_tab, text="Category")
    label_description = Label(view_tab, text="Description")
    label_total = Label(view_tab, text="Total")

    label_date.grid(row=6,column=0)
    label_time.grid(row=6,column=1)
    label_amount.grid(row=6,column=2)
    label_category.grid(row=6,column=3)
    label_description.grid(row=6,column=4)
    label_total.grid(row=6,column=5,columnspan=2)
    
    date = ''
    time = ''
    amount = ''
    category = ''
    description = ''
    total_amount = ''
    for item in result:
        date += str(item[0])+'\n'
        time += str(item[1])+'\n'
        amount += str(item[2])+'\n'
        category += str(item[3])+'\n'
        description += str(item[4])+'\n'
    total_amount += str(total)+'\n'
    
        

    result_date_label = Label(view_tab,text=date)
    result_time_label = Label(view_tab,text=time)
    result_amount_label = Label(view_tab,text=amount)
    result_category_label = Label(view_tab,text=category)
    result_description_label = Label(view_tab,text=description)
    result_total_label = Label(view_tab,text=total_amount)

    result_date_label.grid(row=7,column=0)
    result_time_label.grid(row=7,column=1)
    result_amount_label.grid(row=7,column=2)
    result_category_label.grid(row=7,column=3)
    result_description_label.grid(row=7,column=4)
    result_total_label.grid(row=7,column=5)

def view_specific_date():
    specific_date = e_specific.get()
    conn = db.connect("Expense.db")
    cur = conn.cursor()
    sql1 = '''
    select * from expenses where date = '{}'
    '''.format(specific_date)
    sql2 = '''
    select sum(amount) from expenses where date = '{}'
    '''.format(specific_date)
    cur.execute(sql1)
    result = cur.fetchall()
    cur.execute(sql2)
    total = cur.fetchone()[0]

    label_date = Label(view_tab, text="Date")
    label_time = Label(view_tab, text="Time")
    label_amount = Label(view_tab, text="Amount")
    label_category = Label(view_tab, text="Category")
    label_description = Label(view_tab, text="Description")
    label_total = Label(view_tab, text="Total")

    label_date.grid(row=6,column=0)
    label_time.grid(row=6,column=1)
    label_amount.grid(row=6,column=2)
    label_category.grid(row=6,column=3)
    label_description.grid(row=6,column=4)
    label_total.grid(row=6,column=5,columnspan=2)
    
    date = ''
    time = ''
    amount = ''
    category = ''
    description = ''
    total_amount = ''
    for item in result:
        date += str(item[0])+'\n'
        time += str(item[1])+'\n'
        amount += str(item[2])+'\n'
        category += str(item[3])+'\n'
        description += str(item[4])+'\n'
    total_amount += str(total)+'\n'
    
        

    result_date_label = Label(view_tab,text=date)
    result_time_label = Label(view_tab,text=time)
    result_amount_label = Label(view_tab,text=amount)
    result_category_label = Label(view_tab,text=category)
    result_description_label = Label(view_tab,text=description)
    result_total_label = Label(view_tab,text=total_amount)

    result_date_label.grid(row=7,column=0)
    result_time_label.grid(row=7,column=1)
    result_amount_label.grid(row=7,column=2)
    result_category_label.grid(row=7,column=3)
    result_description_label.grid(row=7,column=4)
    result_total_label.grid(row=7,column=5)

def view_range():
    from_date = e_from.get()
    to_date = e_to.get()
    conn = db.connect("Expense.db")
    cur = conn.cursor()
    sql1 = '''
    select * from expenses where date between '{}' and '{}'
    '''.format(from_date,to_date)
    sql2 = '''
    select sum(amount) from expenses where date between '{}' and '{}'
    '''.format(from_date,to_date)
    cur.execute(sql1)
    result = cur.fetchall()
    cur.execute(sql2)
    total = cur.fetchone()[0]
   
    label_date = Label(view_tab, text="Date")
    label_time = Label(view_tab, text="Time")
    label_amount = Label(view_tab, text="Amount")
    label_category = Label(view_tab, text="Category")
    label_description = Label(view_tab, text="Description")
    label_total = Label(view_tab, text="Total")

    label_date.grid(row=6,column=0)
    label_time.grid(row=6,column=1)
    label_amount.grid(row=6,column=2)
    label_category.grid(row=6,column=3)
    label_description.grid(row=6,column=4)
    label_total.grid(row=6,column=5,columnspan=2)
    
    date = ''
    time = ''
    amount = ''
    category = ''
    description = ''
    total_amount = ''
    for item in result:
        date += str(item[0])+'\n'
        time += str(item[1])+'\n'
        amount += str(item[2])+'\n'
        category += str(item[3])+'\n'
        description += str(item[4])+'\n'
    total_amount += str(total)+'\n'
    
        

    result_date_label = Label(view_tab,text=date)
    result_time_label = Label(view_tab,text=time)
    result_amount_label = Label(view_tab,text=amount)
    result_category_label = Label(view_tab,text=category)
    result_description_label = Label(view_tab,text=description)
    result_total_label = Label(view_tab,text=total_amount)

    result_date_label.grid(row=7,column=0)
    result_time_label.grid(row=7,column=1)
    result_amount_label.grid(row=7,column=2)
    result_category_label.grid(row=7,column=3)
    result_description_label.grid(row=7,column=4)
    result_total_label.grid(row=7,column=5)
    
    
today_label = Label(view_tab,text="Today's Entries")
today_button = Button(view_tab,text="View Today",command=view_today)
specific_date = Label(view_tab,text="Specific Date")
e_specific = Entry(view_tab)
e_specific.insert(0,"DD-MM-YYYY")
specific_button = Button(view_tab,text="Show",command=view_specific_date)
or_label = Label(view_tab,text="OR")
from_label = Label(view_tab,text="From Date:")
e_from = Entry(view_tab)
e_from.insert(0,"DD-MM-YYYY")
to_label = Label(view_tab,text="To Date:")
e_to = Entry(view_tab)
e_to.insert(0,"DD-MM-YYYY")
range_button = Button(view_tab,text="Show",command=view_range)

today_label.grid(row=0,column=0)
today_button.grid(row=0,column=1)
specific_date.grid(row=1,column=0)
e_specific.grid(row=1,column=1)
specific_button.grid(row=1,column=2)
or_label.grid(row=2,column=2)
from_label.grid(row=3,column=0)
e_from.grid(row=3,column=1)
to_label.grid(row=3,column=2)
e_to.grid(row=3,column=3)
range_button.grid(row=4,column=2)



#Stats Tab
def today_chart():
    options = ["Food","Transportation","Household","Self-Care","Health","Education","Gifts","Other"]
    amount = []
    explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
    conn = db.connect("Expense.db")
    cur = conn.cursor()
    for category in options:
        sql1 = '''
        select sum(amount) from expenses where date = '{}' and category = '{}'
        '''.format(today_date,category)
        cur.execute(sql1)
        result = cur.fetchone()[0]
        amount.append(result)
    for index,value in enumerate(amount):
        if value == None:
            amount[index]=0
    plt.style.use("fivethirtyeight")
    plt.title("Today's Data")
    pie = plt.pie(amount,labels=options,explode=explode,shadow=True,autopct='%1.1f%%',labeldistance=1.1)
    plt.legend(pie[0],options,loc="upper right",bbox_to_anchor=(0,1))
    plt.tight_layout()
    plt.show()
    
def specific_date_chart():
    stats_specific_date = stats_e_specific.get()
    options = ["Food","Transportation","Household","Self-Care","Health","Education","Gifts","Other"]
    amount = []
    explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
    conn = db.connect("Expense.db")
    cur = conn.cursor()
    for category in options:
        sql1 = '''
        select sum(amount) from expenses where date = '{}' and category = '{}'
        '''.format(stats_specific_date,category)
        cur.execute(sql1)
        result = cur.fetchone()[0]
        amount.append(result)
    for index,value in enumerate(amount):
        if value == None:
            amount[index]=0
    plt.style.use("fivethirtyeight")
    plt.title("Data of the Specified Date")
    pie = plt.pie(amount,labels=options,explode=explode,shadow=True,autopct='%1.1f%%',labeldistance=1.1)
    plt.legend(pie[0],options,loc="upper right",bbox_to_anchor=(0,1))
    plt.tight_layout()
    plt.show()

def range_chart():
    from_date = stats_e_from.get()
    to_date = stats_e_to.get()
    options = ["Food","Transportation","Household","Self-Care","Health","Education","Gifts","Other"]
    amount = []
    explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
    conn = db.connect("Expense.db")
    cur = conn.cursor()
    for category in options:
        sql1 = '''
        select sum(amount) from expenses where date between '{}' and '{}' and category = '{}'
        '''.format(from_date,to_date,category)
        cur.execute(sql1)
        result = cur.fetchone()[0]
        amount.append(result)
    for index,value in enumerate(amount):
        if value == None:
            amount[index]=0
    plt.style.use("fivethirtyeight")
    plt.title("Data of the Specified Date Range")
    pie = plt.pie(amount,labels=options,explode=explode,shadow=True,autopct='%1.1f%%',labeldistance=1.1)
    plt.legend(pie[0],options,loc="upper right",bbox_to_anchor=(0,1))
    plt.tight_layout()
    plt.show()
   
stats_today_label = Label(stats_tab,text="Today's Entries")
stats_today_button = Button(stats_tab,text="View Today",command=today_chart)
stats_specific_date = Label(stats_tab,text="Specific Date")
stats_e_specific = Entry(stats_tab)
stats_e_specific.insert(0,"DD-MM-YYYY")
stats_specific_button = Button(stats_tab,text="Show",command=specific_date_chart)
stats_or_label = Label(stats_tab,text="OR")
stats_from_label = Label(stats_tab,text="From Date:")
stats_e_from = Entry(stats_tab)
stats_e_from.insert(0,"DD-MM-YYYY")
stats_to_label = Label(stats_tab,text="To Date:")
stats_e_to = Entry(stats_tab)
stats_e_to.insert(0,"DD-MM-YYYY")
stats_range_button = Button(stats_tab,text="Show",command=range_chart)

stats_today_label.grid(row=0,column=0)
stats_today_button.grid(row=0,column=1)
stats_specific_date.grid(row=1,column=0)
stats_e_specific.grid(row=1,column=1)
stats_specific_button.grid(row=1,column=2)
stats_or_label.grid(row=2,column=2)
stats_from_label.grid(row=3,column=0)
stats_e_from.grid(row=3,column=1)
stats_to_label.grid(row=3,column=2)
stats_e_to.grid(row=3,column=3)
stats_range_button.grid(row=4,column=2)



root.mainloop()
