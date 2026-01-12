from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float


PRODUCTS = [
    Product(1, "Camiseta azul", 19.99),
    Product(2, "Camiseta roja", 18.99),
    Product(3, "Pantalón negro", 39.99),
    Product(4, "Zapatillas deportivas", 59.99),
    Product(5, "Gorra", 14.99),
]


def list_products():
    return PRODUCTS


def get_product_by_id(product_id: int):
    for p in PRODUCTS:
        if p.id == product_id:
            return p
    return None
