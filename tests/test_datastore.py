import random, string
from datastore.record import PrimitiveRecord, JsonRecord
from datastore import destination
from datastore import data
from pathlib import Path
import pytest


def test_datastore(basic_data):
    assert basic_data.check_if_exists(key=3) == True

    local = destination.Local(dirpath=Path.cwd() / "input_output_data", filename="data_as_dict.json")
    local.dump_data(basic_data, mode="w", format='json')


@pytest.fixture
def basic_data():
    keys = []
    records = []
    ds_data = data.Data(RecordInstance=PrimitiveRecord)
    for i in range(0, 20):
        key = i
        if key not in keys:
            keys.append(key)
            if random.uniform(0, 1) < 0.5:
                value = random.choice(string.ascii_letters)
            elif random.uniform(0, 1) < 0.5:
                value = random.uniform(0, 100)
            elif random.uniform(0, 1) < 0.5:
                value = random.randint(0, 10)
            else:
                value = False
            ds_data.insert_record(PrimitiveRecord(key, value))
    return ds_data
