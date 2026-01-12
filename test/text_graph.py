from app.graph.shopping_graph import build_graph
from app.domain.cart import Cart


def make_state(**kwargs):
    state = {
        "cart": Cart()
    }
    state.update(kwargs)
    return state


def test_add_product_flow():
    graph = build_graph()

    state = make_state(
        intent="add_product",
        product_id=1,
        quantity=2
    )

    result = graph.invoke(state)

    cart = result["cart"]
    assert 1 in cart.items
    assert cart.items[1].quantity == 2


def test_checkout_cancel_keeps_cart():
    graph = build_graph()

    # Estado con un producto en el carrito
    state = make_state(
        intent="confirm_no",
        name="Ana",
        city="Madrid"
    )

    # metemos producto manualmente
    state["cart"].items[1] = type(
        "X", (), {"quantity": 2, "product": type("P", (), {"price": 10, "name": "Test"})()}
    )()

    result = graph.invoke(state)

    # El carrito NO debe borrarse
    assert not result["cart"].is_empty()
    assert result["cart"].items[1].quantity == 2
