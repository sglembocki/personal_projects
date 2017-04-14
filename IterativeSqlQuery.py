#imports

import pandas as pd
import cx_Oracle as ora
import base64
import smtplib

#sql for all mapped_course_names, specify courses of interest here

sql = '''
    SELECT DISTINCT NAME
    FROM LIST
    WHERE FIELD LIKE '%%'
'''

#connect and save all course_names to df, input username and password

conn = ora.connect('user/password@connection')
cursor = conn.cursor()
names = pd.read_sql(sql, conn)
names.head()

#course completion, iterating through each course_name

df = pd.DataFrame()

for index, row in names.iterrows():
    df = df.append(pd.read_sql(("""
        SELECT *
        FROM table
        WHERE condition LIKE '{}'
    """.format(row['name'])), conn))

#save file as csv

df.to_csv('test.csv', sep = ',', index = 'False') #save file as csv