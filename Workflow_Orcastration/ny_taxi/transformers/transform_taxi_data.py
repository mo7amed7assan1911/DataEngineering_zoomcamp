if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    non_zero_passengers = data.passenger_count != 0
    print(f'Number of zero passengers: {non_zero_passengers.sum()}')
    return data[non_zero_passengers]


@test
def test_output(output, *args) -> None:

    assert (output.passenger_count == 0).sum() == 0, 'There is rides with zero passengers'
