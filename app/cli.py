# app/cli.py

from app.domain.cart import Cart
from app.graph.shopping_graph import build_graph
from app.application.parser import parse_input


def main():
    cart = Cart()
    graph = build_graph()
    state = {"cart": cart}

    print("""
🛒 CHATBOT CARRITO DE COMPRA
────────────────────────────────
Comandos disponibles:
• productos              → Ver catálogo
• añadir <id> <cantidad> → Añadir producto
• quitar <id> <cantidad> → Quitar producto
• carrito                → Ver carrito
• finalizar              → Finalizar compra
• salir                  → Salir del programa
────────────────────────────────
""")

    while True:
        user = input("> ")

        parsed = parse_input(user)
        state["intent"] = parsed["intent"]

        if "product_id" in parsed:
            state["product_id"] = parsed["product_id"]
        if "quantity" in parsed:
            state["quantity"] = parsed["quantity"]

        if state["intent"] == "exit":
            graph.invoke(state)
            break

        if state["intent"] == "checkout":
            graph.invoke(state)

            state["name"] = input("📛 Nombre: ")
            state["city"] = input("🏙️ Ciudad: ")
            c = input("¿Confirmas? (si/no): ").lower()

            state["intent"] = "confirm_yes" if c == "si" else "confirm_no"
            graph.invoke(state)
            continue

        graph.invoke(state)


if __name__ == "__main__":
    main()
