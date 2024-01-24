# Contarization_of_postgreSQL


### First, you need to create external volume & network

```bash
docker create network pg-network
docker create volume pg-volume
```

### Run the PostgreSQL environment by:

```bash
docker-compose -f postgres_env.yml up -d
```

### Load and save in the database the dataset of ny_taxi

##### First, creat a Image that makes the process
```bash
docker build -t taxi_data_image . 
```

##### Then, create a container from this image and connect it to the same volume and network

```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

docker run -it --network=pg-network taxi_data_image --user=root --password=mypass --host=pgServer --port=5432 --db=ny_taxi --table_name=yello_taxis --url=${URL}
```