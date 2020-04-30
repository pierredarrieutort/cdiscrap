from cdiscount_parser.price_parser import parse_price


def test_parse_price_no_params():
    assert parse_price() is False


def test_parse_price_random_params():
    assert parse_price("random") is False


def test_parse_price_with_params():
    assert isinstance(parse_price("del5397184246030"), float)
