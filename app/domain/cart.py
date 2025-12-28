from dataclasses import dataclass, field
from typing import Dict

from app.domain.product import Product


@dataclass
class CartItem:
    product: Product
    quantity: int


@dataclass
class Cart:
    items: Dict[int, CartItem] = field(default_factory=dict)

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que 0")

        if product.id in self.items:
            self.items[product.id].quantity += quantity
        else:
            self.items[product.id] = CartItem(product, quantity)

    def remove_product(self, product_id: int) -> None:
        if product_id in self.items:
            del self.items[product_id]

    def update_quantity(self, product_id: int, quantity: int) -> None:
        if quantity <= 0:
            self.remove_product(product_id)
        elif product_id in self.items:
            self.items[product_id].quantity = quantity

    def total_price(self) -> float:
        return sum(
            item.product.price * item.quantity
            for item in self.items.values()
        )

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def summary(self) -> str:
        if self.is_empty():
            return "El carrito está vacío"

        lines = []
        for item in self.items.values():
            lines.append(
                f"{item.product.name} x {item.quantity} = "
                f"{item.product.price * item.quantity:.2f}€"
            )
        lines.append(f"Total: {self.total_price():.2f}€")
        return "\n".join(lines)
