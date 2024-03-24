import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    # Notice: We didn't use int and used pd.Int64Dtype() as there are many Nan values couldent int.
    taxi_dtypes = {
        'VendorID': pd.Int64Dtype(),
        'passenger_count': pd.Int64Dtype(),
        'trip_distance': float,
        'RatecodeID': pd.Int64Dtype(),
        'PULocationID': pd.Int64Dtype(),
        'store_and_fwd_flag': str,
        'PULocationID': pd.Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd.Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'ehail_fee': pd.Int64Dtype(),
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float,
        'trip_type': pd.Int64Dtype()

    }

    date_coulumns = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    dfs = []
    for month in [10, 11, 12]:
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz'
        df = pd.read_csv(url, compression='gzip', dtype=taxi_dtypes, parse_dates=date_coulumns, sep=',')

        dfs.append(df)

    data = pd.concat(dfs, ignore_index=True)
    return data
        



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
