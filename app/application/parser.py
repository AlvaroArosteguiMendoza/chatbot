def parse_input(text: str) -> dict:
    text = text.lower().strip()
    parts = text.split()

    if text in ("salir", "exit", "terminar"):
        return {"intent": "exit"}

    if "producto" in text or "productos" in text:
        return {"intent": "list_products"}

    if text.startswith("añadir"):
        try:
            return {
                "intent": "add_product",
                "product_id": int(parts[1]),
                "quantity": int(parts[2]) if len(parts) > 2 else 1,
            }
        except:
            return {"intent": "unknown"}

    if text.startswith("quitar"):
        try:
            return {
                "intent": "remove_product",
                "product_id": int(parts[1]),
                "quantity": int(parts[2]) if len(parts) > 2 else 1,
            }
        except:
            return {"intent": "unknown"}

    if text == "carrito":
        return {"intent": "show_cart"}

    if text == "finalizar":
        return {"intent": "checkout"}

    return {"intent": "unknown"}
