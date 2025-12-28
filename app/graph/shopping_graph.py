from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.domain.cart import Cart
from app.domain.product import list_products


class ShoppingState(TypedDict):
    input: str
    intent: str
    cart: Cart


def start_node(state: ShoppingState) -> ShoppingState:
    text = state["input"].lower()

    if "producto" in text:
        state["intent"] = "catalog"
    elif "añadir" in text:
        state["intent"] = "add"
    elif "carrito" in text:
        state["intent"] = "show_cart"
    elif "checkout" in text or "finalizar" in text or "comprar" in text:
        state["intent"] = "checkout"
    elif "salir" in text:
        state["intent"] = "end"
    else:
        print("❓ No he entendido tu mensaje")
        state["intent"] = "start"

    return state


def catalog_node(state: ShoppingState) -> ShoppingState:
    print("📦 Productos disponibles:")
    for p in list_products():
        print(f"{p.id} - {p.name} ({p.price}€)")
    return state


def cart_node(state: ShoppingState) -> ShoppingState:
    print("🛒 Carrito actual:")
    print(state["cart"].summary())
    return state


def checkout_node(state: ShoppingState) -> ShoppingState:
    print("🧾 Resumen del pedido:")
    print(state["cart"].summary())
    print("✔ Pedido preparado (simulado)")
    return state


def end_node(state: ShoppingState) -> ShoppingState:
    print("👋 Gracias por usar el chatbot")
    return state


def build_graph():
    graph = StateGraph(ShoppingState)

    graph.add_node("start", start_node)
    graph.add_node("catalog", catalog_node)
    graph.add_node("cart", cart_node)
    graph.add_node("checkout", checkout_node)
    graph.add_node("end", end_node)

    graph.set_entry_point("start")

    graph.add_conditional_edges(
        "start",
        lambda s: s["intent"],
        {
            "catalog": "catalog",
            "add": "cart",
            "show_cart": "cart",
            "checkout": "checkout",
            "end": "end",
            "start": "end",  # si no entiende, termina
        },
    )

    graph.add_edge("catalog", END)
    graph.add_edge("cart", END)
    graph.add_edge("checkout", END)
    graph.add_edge("end", END)

    return graph.compile()

