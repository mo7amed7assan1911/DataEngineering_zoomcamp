import re
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


def trips_with_passengers_distance(data):
    trips_with_passengers = data.passenger_count > 0
    trips_with_distance   = data.trip_distance > 0

    data = data[trips_with_passengers & trips_with_distance]
    return data

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

@transformer
def transform(data, *args, **kwargs):
    data = trips_with_passengers_distance(data)

    data.lpep_pickup_datetime = data.lpep_pickup_datetime.dt.date

    data.rename(columns={name: camel_to_snake(name) for name in data.columns}, inplace=True)

    data.drop(columns='ehail_fee', inplace=True)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    no_passengers_trips = (output.passenger_count <= 0).sum()
    no_distance_trips   = (output.trip_distance <= 0).sum()

    summation = no_distance_trips + no_passengers_trips
    assert summation == 0, 'There is a problem !'
    assert 'vendor_id' in output.columns, 'No vendor_id'
