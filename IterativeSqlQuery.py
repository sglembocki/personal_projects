#imports

import pandas as pd
import cx_Oracle as ora
import base64
import smtplib

#sql for list that will be used for parameters

sql = '''
    SELECT DISTINCT NAME
    FROM LIST
    WHERE FIELD LIKE '%%'
'''

#connect and save all list items to df

conn = ora.connect('user/password@connection')
cursor = conn.cursor()
names = pd.read_sql(sql, conn)
names.head()

#sql query that iterates through list items

df = pd.DataFrame()

for index, row in names.iterrows():
    df = df.append(pd.read_sql(("""
        SELECT *
        FROM table
        WHERE condition LIKE '{}'
    """.format(row['name'])), conn))

#save file as csv

df.to_csv('test.csv', sep = ',', index = 'False') #save file as csv
