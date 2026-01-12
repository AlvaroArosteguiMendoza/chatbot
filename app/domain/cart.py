from dataclasses import dataclass
from typing import Dict
from app.domain.product import Product


@dataclass
class CartItem:
    product: Product
    quantity: int


class Cart:
    def __init__(self):
        self.items: Dict[int, CartItem] = {}

    def add_product(self, product: Product, quantity: int):
        if quantity<= 0:
            raise ValueError("Cantidad inválida")
        
        if product.id in self.items:
            self.items[product.id].quantity += quantity
        else:
            self.items[product.id] = CartItem(product, quantity)
            

    def remove_product(self, product_id: int):
        if product_id in self.items:
            del self.items[product_id]

    def update_quantity(self, product_id: int, quantity: int):
        if quantity <= 0:
            self.remove_product(product_id)
        elif product_id in self.items:
            self.items[product_id].quantity = quantity

    def is_empty(self):
        return len(self.items) == 0

    def total_price(self):
        return sum(
            item.product.price * item.quantity
            for item in self.items.values()
        )

    def summary(self):
        if self.is_empty():
            return "🛒 El carrito está vacío"

        lines = []
        for item in self.items.values():
            subtotal = item.product.price * item.quantity
            lines.append(
                f"{item.product.name} x {item.quantity} = {subtotal:.2f}€"
            )
        lines.append(f"Total: {self.total_price():.2f}€")
        return "\n".join(lines)
