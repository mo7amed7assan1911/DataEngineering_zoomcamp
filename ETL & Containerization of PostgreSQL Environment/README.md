# ETL & Containerization of PostgreSQL Environment
### Building the PostgreSQL Environment
🚀 To build the PostgreSQL environment, run the following command:

```bash
docker-compose -f postgres_env.yml up -d
```

### Loading Dataset and Adding it to the Database

🛠️ To load the dataset and add it to the database, execute the `ingest_data.py` script. Ensure to provide accurate values for the arguments, such as user, password, host, and port based on the running containers.

📝 **NOTICE:** The host will be pgServer (the PostgreSQL server in our `docker-compose` file) if you run the script inside a container that is on the pg-network.

🚀 Run the following command:

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
