
from parser import parse_product_basic, parse_availability


def test_parse_product_basic_extracts_id(valid_product):
    response = parse_product_basic(valid_product)
    assert response["id"] == valid_product["id"]



def test_parse_product_basic_extracts_name(valid_product):
    response = parse_product_basic(valid_product)
    assert response["name"] == valid_product["name"]


def test_parse_product_basic_returns_only_id_and_name(valid_product):
    response = parse_product_basic(valid_product)
    assert list(response.keys()) == ["id", "name"]







