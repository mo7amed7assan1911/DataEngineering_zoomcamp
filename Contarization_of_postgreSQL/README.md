# ETL & Contarization of PostgreSQl env

## Building the PostgreSQL Environment

#### You need to run this:

```bash
docker-compose -f postgres_env.yml up -d
```

## Loading dataset then add it to the database

#### You could run the ingest_data.py script to do that.
> But, use good values in the arguments such as the user, password, host, port based on the running containers.

> **NOTICE:** the host will be pgServer `server of the postgresql in our docker-compose file` if you run the script inside a container that on the pg-network.

#### You need to run this:

```bash
trips_url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"

zones_url="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"

python ingest_data_homeWork.py \
    --user=root \
    --password=mypass \
    --host=localhost \
    --port=5432 \
    --db=taxi_dataset \
    --trips_table_name="taxi_trips" \
    --zones_table_name="zones" \
    --trips_data_url=${trips_url} \
    --zones_data_url=${zones_url}
```