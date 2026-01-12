from app.domain.cart import Cart
from app.domain.product import Product


def test_add_product():
    cart = Cart()
    p = Product(1, "Test", 10)
    cart.add_product(p, 2)
    assert cart.items[1].quantity == 2


def test_remove_product():
    cart = Cart()
    p = Product(1, "Test", 10)
    cart.add_product(p, 2)
    cart.remove_product(1)
    assert cart.is_empty()


def test_update_quantity():
    cart = Cart()
    p = Product(1, "Test", 10)
    cart.add_product(p, 1)
    cart.update_quantity(1, 3)
    assert cart.items[1].quantity == 3

def test_total_price():
    cart = Cart()
    p1 = Product(1, "A", 10)
    p2 = Product(2, "B", 5)

    cart.add_product(p1, 2)   # 20
    cart.add_product(p2, 3)   # 15

    assert cart.total_price() == 35


def test_update_quantity_to_zero_removes_product():
    cart = Cart()
    p = Product(1, "Test", 10)

    cart.add_product(p, 2)
    cart.update_quantity(1, 0)

    assert cart.is_empty()
