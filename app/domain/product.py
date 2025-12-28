from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float
    category: str | None = None


CATALOG = [
    Product(1, "Camiseta azul", 19.99, "ropa"),
    Product(2, "Camiseta roja", 18.99, "ropa"),
    Product(3, "Pantalón negro", 39.99, "ropa"),
    Product(4, "Zapatillas deportivas", 59.99, "calzado"),
    Product(5, "Gorra", 14.99, "accesorios"),
]


def list_products() -> list[Product]:
    return CATALOG


def get_product_by_id(product_id: int) -> Product | None:
    for product in CATALOG:
        if product.id == product_id:
            return product
    return None
