from parse_price import sku_to_price, sku, price


def test_sku_no_exists_params():
    assert sku("pamplemousse") == sku_to_price()


def test_sku_with_params():
    assert sku("kaneco250v") == print(160.99)
