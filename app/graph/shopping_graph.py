# app/graph/shopping_graph.py

from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.domain.cart import Cart
from app.domain.product import list_products, get_product_by_id


class ShoppingState(TypedDict, total=False):
    intent: str
    cart: Cart
    product_id: int
    quantity: int
    name: str
    city: str
    confirm: str


def start_node(state): return state

def list_products_node(state):
    for p in list_products():
        print(f"{p.id} - {p.name} ({p.price}€)")
    return state

def add_product_node(state):
    p = get_product_by_id(state.get("product_id"))
    if not p:
        print("❌ Producto no encontrado")
        return state
    state["cart"].add_product(p, state.get("quantity", 1))
    print(state["cart"].summary())
    return state

def remove_product_node(state):
    cart = state["cart"]
    pid = state.get("product_id")
    qty = state.get("quantity", 1)

    if pid not in cart.items:
        print("❌ Ese producto no está en el carrito")
        return state

    current = cart.items[pid].quantity

    if qty < current:
        cart.update_quantity(pid, current - qty)
        print(f"➖ Se han quitado {qty} unidad(es)")
    else:
        cart.remove_product(pid)
        print("🗑️ Producto eliminado")

    print(cart.summary())
    return state


def show_cart_node(state):
    print(state["cart"].summary())
    return state

def checkout_node(state):
    print("🧾 Resumen:")
    print(state["cart"].summary())
    return state

def confirm_yes_node(state):
    print("\n✅ Pedido confirmado")
    print(state["cart"].summary())
    print(f"{state['name']} - {state['city']}")
    return state

def confirm_no_node(state):
    print("❌ Pedido cancelado. Carrito conservado.")
    print(state["cart"].summary())
    return state

def unknown_node(state):
    print("❓ No he entendido el comando")
    return state

def end_node(state):
    print("👋 Gracias por usar el chatbot")
    return state


def build_graph():
    g = StateGraph(ShoppingState)

    for name, fn in [
        ("start", start_node),
        ("list_products", list_products_node),
        ("add_product", add_product_node),
        ("remove_product", remove_product_node),
        ("show_cart", show_cart_node),
        ("checkout", checkout_node),
        ("confirm_yes", confirm_yes_node),
        ("confirm_no", confirm_no_node),
        ("unknown", unknown_node),
        ("end", end_node),
    ]:
        g.add_node(name, fn)

    g.set_entry_point("start")

    g.add_conditional_edges(
        "start",
        lambda s: s["intent"],
        {
            "list_products": "list_products",
            "add_product": "add_product",
            "remove_product": "remove_product",
            "show_cart": "show_cart",
            "checkout": "checkout",
            "confirm_yes": "confirm_yes",
            "confirm_no": "confirm_no",
            "exit": "end",
            "unknown": "unknown",
        },
    )

    for n in [
        "list_products",
        "add_product",
        "remove_product",
        "show_cart",
        "checkout",
        "confirm_yes",
        "confirm_no",
        "unknown",
        "end",
    ]:
        g.add_edge(n, END)

    return g.compile()
