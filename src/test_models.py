import models
import pytest


@pytest.fixture
def special_offer():
    return models.SpecialOffer("My Special Offer", 2)


@pytest.fixture
def basic_item():
    return models.Item("Apple", 0.20)


@pytest.fixture
def item_offer(special_offer):
    return models.Item("Apple", 0.20, special_offer)


@pytest.fixture
def basket_empty():
    return models.Basket()


@pytest.fixture
def basket():
    basket_ = models.Basket()
    basket_.add(
        models.Item(
            "Apple",
            0.20,
            models.SpecialOffer(
                "Buy One Get One Free on Apples",
                2
            )
        ),
        4,
    )
    return basket_


def test_special_offer_init(special_offer, capsys):
    print(special_offer)
    out, err = capsys.readouterr()
    assert "My Special Offer" in out
    assert special_offer.__repr__() == "My Special Offer"
    assert special_offer.title == "My Special Offer"
    assert special_offer.count == 2


def test_item_init(basic_item, capsys):
    print(basic_item)
    out, err = capsys.readouterr()
    assert "Apple" in out
    assert basic_item.__repr__() == "Apple"
    assert basic_item.name == "Apple"
    assert basic_item.price == 0.20
    assert basic_item.has_offer() is False


def test_item_init_with_offer(item_offer):
    assert item_offer.has_offer() is True


def test_basket_init(basket_empty):
    assert basket_empty.content == {}
    assert basket_empty.total == 0


def test_basket_add_item(basket_empty):
    apple = models.Item("Apple", 0.40)
    basket_empty.add(apple, 3)
    basket_empty.add(apple, 5)
    assert basket_empty.content != {}
    assert basket_empty.content[apple] == 8


def test_basket_add_item_quantity_null(basket_empty):
    basket_empty.add(None, 0)
    assert basket_empty.content == {}


def test_basket_calculate_total(basket_empty):
    basket_empty.calculate_price()
    assert basket_empty.get_price() == 0


def test_basket_get_price(basket):
    basket.calculate_price()
    assert basket.get_price() == 4 * 0.20


def test_basket_apply_special_offers(basket):
    basket.apply_special_offers()
    assert basket.get_price() == 2 * 0.20


def test_basket_show(capsys):
    basket = models.Basket()
    basket.add(models.Item("Apple", 0.20), 2)
    basket.calculate_price()
    basket.show()
    out, err = capsys.readouterr()
    assert "Apple" in out
    assert f"{0.20 * 2:.2f}£" in out
