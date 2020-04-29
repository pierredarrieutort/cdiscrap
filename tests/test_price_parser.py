from price_parser import parse_price


def test_parse_price_no_params():
    assert parse_price("") == False


def test_parse_price_with_params():
    assert parse_price("del5397184246030") == 1776.6
