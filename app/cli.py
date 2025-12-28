from app.domain.cart import Cart
from app.graph.shopping_graph import build_graph


def main():
    cart = Cart()
    graph = build_graph()

    print("🛒 Chatbot carrito con LangGraph")
    print("Ejemplos: productos | añadir | carrito | finalizar | salir")

    while True:
        user_input = input("> ")

        if user_input.lower() in ["salir", "exit", "quit"]:
            break

        state = {
            "input": user_input,
            "intent": "",
            "cart": cart,
        }

        graph.invoke(state)


if __name__ == "__main__":
    main()
