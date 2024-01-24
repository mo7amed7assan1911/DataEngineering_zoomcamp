# Creating image for downloading data and add it to the SQL server running.
FROM python:3.9.1

RUN ["apt-get", "install", "wget"]

WORKDIR /app

COPY requirements.txt requirements.txt
COPY ingest_data.py ./code/

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT [ "python", "./code/ingest_data.py" ]


# docker build -t taxi_data_image .

# URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

# docker run -it --network=pg-network taxi_data_image \
#     --user=root \
#     --password=mypass \
#     --host=pgServer \
#     --port=5432 \
#     --db=ny_taxi \
#     --table_name=yello_taxis \
#     --url=${URL}