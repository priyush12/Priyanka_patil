import sqlite3
con=sqlite3.connect("G:/database_sql/student.db")
c=con.cursor()

def create_table():
    c.execute("create table student (stud_ID int  not null PRIMARY KEY, fname text,lname text,gender text,age int,contact_add text,stud_email text,stud_pass text)")

#create_table()

import random,time
def dynamic_entry(n):
    print("Inserting dyanmic entries into student table")
    for i in range(n):
        Eid=random.randint(1,7)
        fn=random.choice(['priyanka','raj','khushi','aayan','kunal','janvi','yash'])
        ln=random.choice(['patil','sonar','wagh','kuvar','shinde'])
        gn=random.choice(['female','male'])
        ag=random.randint(21,28)
        ca=random.choice(['vapi','pune','goa','mumbai'])
        se=random.choice(['khy@gmail.com','trg@gmail.com','abd@gmail.com','wew@gmail.com','yel@gmail.com','wqw@gamil.com'])
        sp=random.randint(2017,2020)
        c.execute("insert or ignore into student(stud_ID,fname,lname,gender,age,contact_add,stud_email,stud_pass)values(?,?,?,?,?,?,?,?)",(Eid,fn,ln,gn,ag,ca,se,sp))
        con.commit()
        
dynamic_entry(int(input("How many enteries you want to insert into student table? ")))    
  

def create_table():
    c.execute("create table schedules(sched_ID int not null PRIMARY KEY,course_ID int,ins_ID int,sub_ID int,stud_ID int,day text,time_start text,time_end text,FOREIGN KEY(course_ID)REFERENCES Courses(course_ID),FOREIGN KEY (ins_ID) REFERENCES instructor(ins_ID),FOREIGN KEY (sub_ID) REFERENCES subjects(sub_ID),FOREIGN KEY(stud_ID) REFERENCES student(stud_ID))")
    
create_table()

import random
def dynamic_entry1(n1):
    print("Inserting dyanmic entries into schedules table")
    for i in range(n1):
        Seid=random.randint(0,7)
        ceid=random.randint(101,108)
        ieid=random.randint(201,208)
        sueid=random.randint(1,8)
        steid=random.randint(1,7)
        dy=random.choice(['monday','tuesday','wednesday','thursday','friday'])
        tst=random.choice(['1:20:00','1:47:25','1:2:47','1:00:00'])
        tsst=random.choice(['2:2:12','2:10:23','2:3:00','2:00:00'])
        c.execute("insert or ignore into schedules(sched_ID,course_ID,ins_ID,sub_ID ,stud_ID,day,time_start,time_end)values(?,?,?,?,?,?,?,?)",(Seid,ceid,ieid,sueid,steid,dy,tst,tsst))
        con.commit()
        
dynamic_entry1(int(input("How many enteries you want to insert into schedules table? ")))         

        
def create_table():
    c.execute("create table instructor(ins_ID int not null PRIMARY KEY,fname text,lname text,gender text,age int,contact_add text,iins_email text,ins_pass text)")

create_table()

import  random
def dynamic_entry2(n2):
    print("Inserting dyanmic entries into instructor table")
    for i in range(n2):
        ineid=random.randint(201,208)
        fna=random.choice(['dipali','hitesh','tejas','piyush'])
        lna=random.choice(['patil','kuwar','salunke'])
        gen=random.choice(['female','male'])
        ag=random.randint(30,35)
        ad=random.choice(['pune','mumbai','delhi'])
        em=random.choice(['avs@gmail','hde@gmail','lao@gmail','bg@gmail'])
        inp=random.randint(2000,2015)
        c.execute("Insert or ignore into instructor (ins_ID,fname,lname,gender ,age ,contact_add ,iins_email,ins_pass)values(?,?,?,?,?,?,?,?)",(ineid,fna,lna,gen,ag,ad,em,inp))
        con.commit()
dynamic_entry2(int(input("How many enteries you want to insert into instructor table? ")))         
        

def create_table():
    
    c.execute("create table tra(trans_ID int not null PRIMARY KEY,trans_name text ,stud_ID int,trans_date 'YYYY-MM-DD', FOREIGN KEY (stud_ID) REFERENCES student(stud_ID))")

create_table()


import random
def dynamic_entry3(n3):
     print("Inserting dyanmic entries into tra table")
     for i in range(n3):
         teid=random.randint(401,406)
         tname=random.choice(['yash','ravi','dimple','jija'])
         steid=random.randint(1,7)
         trdate=random.choice(['2-5-2022','3-5-2022'])
         c.execute("Insert or ignore into tra(trans_ID,trans_name,stud_ID ,trans_date) values(?,?,?,?)",(teid,tname,steid,trdate))
         con.commit()

dynamic_entry3(int(input("How many enteries you want to insert into tra table? ")))
        

def create_table():
    c.execute("create table Courses(course_ID int not null PRIMARY KEY,course_name text,course_desc text,school_yr int)")



create_table()

import random
def dynamic_entry4(n4):
     print("Inserting dyanmic entries into course table")
     for i in range(n4):
         ceid=random.randint(101,108)
         cname=random.choice(['python','java','cpp','c++'])
         cdes=random.choice(['software dev','engineer'])
         syr=random.randint(2015,2021)
         c.execute("insert or ignore into Courses(course_ID,course_name,course_desc,school_yr)values(?,?,?,?)",(ceid,cname,cdes,syr))
         con.commit()

dynamic_entry4(int(input("How many enteries you want to insert into courses table? ")))
        
def create_table():
    c.execute("create table subjects(sub_ID not null PRIMARY KEY,name text,course_ID int,FOREIGN KEY(course_ID) REFERENCES courses(course_ID))")
create_table()

import random
def dynamic_entry5(n5):
     print("Inserting dyanmic entries into subject table")
     for i in range(n5):
         seid=random.randint(1,8)
         na=random.choice(['english','math'])
         ceid=random.randint(101,108)
         c.execute("insert or ignore into subjects(sub_ID,name,course_ID)values(?,?,?)",(seid,na,ceid))
         con.commit()

dynamic_entry5(int(input("How many enteries you want to insert into subject table? ")))




