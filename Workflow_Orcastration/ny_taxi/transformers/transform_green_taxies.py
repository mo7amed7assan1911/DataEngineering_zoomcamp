if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    trips_with_passengers = data.passenger_count > 0
    trips_with_distance   = data.trip_distance > 0

    data = data[trips_with_passengers & trips_with_distance]
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
