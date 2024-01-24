
import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(args):
    user = args.user
    password = args.password
    host = args.host
    port = args.port
    db   = args.db
    table_name = args.table_name
    csv_url    = args.url
    csv_name   = 'output.csv'
    
    # downloading the csv and name it 'output.csv'
    os.system(f'wget {csv_url} -O {csv_name}')
    
    print('Data Is downloaded 🥰')
    df = pd.read_csv(csv_name, nrows=1, compression='gzip')
    print('good dataframe')
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    engine.connect()
    
    print('Connected to posgresql server 🥰')

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000, compression='gzip')
    
    # adding no line just making the schema of the database.
    df.head(0).to_sql(con=engine, name=table_name, if_exists='replace', index=False)
    
    print('Created new schema 🥰')

    for batch in df_iter:
        
        t_start = time()
                
        batch.tpep_dropoff_datetime = pd.to_datetime(batch.tpep_dropoff_datetime)
        batch.tpep_pickup_datetime  = pd.to_datetime(batch.tpep_pickup_datetime)

        batch.to_sql(con=engine, name=table_name, if_exists='append', index=False)

        t_end = time()
        print(f'inserted another chunk, took {(t_end-t_start):.3f} 🥰')


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Ingest CSV to postgresql database')

    # user, password, host, port, database name, table name, url of the csv
    parser.add_argument('--user', help='user name')
    parser.add_argument('--password', help='password of teh posgres server')
    parser.add_argument('--host', help='host of the pg server')
    parser.add_argument('--port', help='port of pg server')
    parser.add_argument('--db', help='database name')
    parser.add_argument('--table_name', help='table name')
    parser.add_argument('--url', help='url of the csv file')
    
    args = parser.parse_args()
    
    main(args=args)
    
    
# URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"


# # the host is pg_server if you run the script inside a container that on the pg-network.

# python ingest_data.py \
#     --user=root \
#     --password=mypass \
#     --host=localhost \
#     --port=5432 \
#     --db=ny_taxi \
#     --table_name=yello_taxis \
#     --url=${URL}