#!/usr/bin/env python3

import json
import jsonschema
import pytest
from pathlib import Path

base_path = Path(__file__).parent
data_path = base_path / "data"
schema = json.load(open(base_path / '../../files/assertions/criteria/symlinks_criteria.json'))

def test_empty_array():
	data = json.load(open(data_path / "./empty_list.json"))

	jsonschema.validate(instance=data, schema=schema)

def test_missing_location():
	data = json.load(open(data_path / "./missing_location.json"))

	with pytest.raises(Exception, match=r"'location' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_location_path():
	data = json.load(open(data_path / "./missing_location_path.json"))

	with pytest.raises(Exception, match=r"'path' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_location_path():
	data = json.load(open(data_path / "./empty_location_path.json"))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_location_owner():
	data = json.load(open(data_path / "./missing_location_owner.json"))

	with pytest.raises(Exception, match=r"'owner' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_location_owner():
	data = json.load(open(data_path / "./empty_location_owner.json"))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_location_group():
	data = json.load(open(data_path / "./missing_location_group.json"))

	with pytest.raises(Exception, match=r"'group' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_location_group():
	data = json.load(open(data_path / "./empty_location_group.json"))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_destination():
	data = json.load(open(data_path / "./missing_destination.json"))

	with pytest.raises(Exception, match=r"'destination' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_destination_path():
	data = json.load(open(data_path / "./missing_destination_path.json"))

	with pytest.raises(Exception, match=r"'path' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_destination_path():
	data = json.load(open(data_path / "./empty_destination_path.json"))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_non_make_destination():
	data = json.load(open(data_path / "./non_make_destination.json"))

	jsonschema.validate(instance=data, schema=schema)

def test_missing_destination_owner():
	data = json.load(open(data_path / "./missing_destination_owner.json"))

	with pytest.raises(Exception, match=r"'owner' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_destination_owner():
	data = json.load(open(data_path / "./empty_destination_owner.json"))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_destination_group():
	data = json.load(open(data_path / "./missing_destination_group.json"))

	with pytest.raises(Exception, match=r"'group' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_destination_owner():
	data = json.load(open(data_path / "./empty_destination_group.json"))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)

def test_missing_destination_mode():
	data = json.load(open(data_path / "./missing_destination_mode.json"))

	with pytest.raises(Exception, match=r"'mode' is a required property"):
		jsonschema.validate(instance=data, schema=schema)

def test_empty_destination_mode():
	data = json.load(open(data_path / "./empty_destination_mode.json"))

	with pytest.raises(Exception, match=r"'' should be non-empty"):
		jsonschema.validate(instance=data, schema=schema)