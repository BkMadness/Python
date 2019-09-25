#!/usr/bin/python

import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","root" , "studentregister")
cur = db.cursor()

#delete any exisiting tables 
cur.execute('DROP TABLE IF EXISTS Students')
cur.execute('DROP TABLE IF EXISTS Module')
cur.execute('DROP TABLE IF EXISTS Lectures')
cur.execute('DROP TABLE IF EXISTS Facility')
cur.execute('DROP TABLE IF EXISTS Room')
cur.execute('DROP TABLE IF EXISTS Grade')

#create tables 
cur.execute("create table Students(Studentno varchar(20),firstname varchar(20),lastname varchar(20), DOB  varchar(20), Address1 varchar(20) ,Address2 varchar(20),Town varchar(20), City varchar(20), Module varchar(20) ,MacAddress varchar(20) , Gender varchar(6)) ")
cur.execute("create table Module(ModuleId varchar(5),Tittle varchar(20),StartTime TIME,EndTime TIME) ")
cur.execute("create table Lectures(LectureId varchar(20),firstname varchar(20),lastname varchar(20), DOB varchar(20), Address1 varchar(20) ,Address2 varchar(20),Town varchar(20), City varchar(20), Module varchar(20) ,MacAddress varchar(20) , Gender varchar(6)) ")
cur.execute("create table Facility(FacilityId varchar(20),Facilityname varchar(20))")
cur.execute("create table Grade(Studentno varchar(8),ModuleId varchar(20), Semester int(1), Grade int(1)) ")
cur.execute("create table Room(RoomNo int(4)) ")


print "table created successfully"

cur.close()
db.close()

