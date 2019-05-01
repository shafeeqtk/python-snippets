import pandas as pd
# this psycopg package is required for running sqlalchemy
# import sys
# !{sys.executable} -m pip install psycopg2-binary
import sqlalchemy as sa

#create connection to postgres database
con = sa.create_engine('postgresql://user:password@server_ip/dbname')

'''
QUERYING THE DATABASE
'''


df = pd.read_sql('select * from schema_name."tablename" limit 10', con)


'''
WRITING TO THE DATABASE
'''

#read csv file as chunks
chunks = pd.read_csv("source.csv", chunksize=100000)

#write each chunk into database table
for chunk in chunks:
    chunk.to_sql(schema='schema_name', name="dest_table", if_exists='replace', con=con, index=False)

