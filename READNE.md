# 🛒 Chatbot Carrito con LangGraph

Este proyecto es un chatbot de línea de comandos que simula un **carrito de compra** utilizando una **máquina de estados** construida con **LangGraph**.

El usuario puede navegar por productos, añadir y quitar artículos, ver el carrito y completar o cancelar un pedido sin perder su estado.

---

## 🚀 Características

- Máquina de estados con LangGraph
- Carrito persistente
- Confirmación sí / no al finalizar
- Cancelar no borra el carrito
- CLI simple y robusto
- Tests automáticos con Pytest

---

## 📦 Requisitos

- Python 3.10+
- pip
- Entorno virtual recomendado

---

## 🔧 Instalación

Clona el repositorio:

```bash
git clone https://github.com/AlvaroArosteguiMendoza/chatbot-carrito-langgraph.git
cd chatbot-carrito-langgraph
Crea y activa un entorno virtual:

Si es en Windows:
python -m venv venv
venv\Scripts\activate

Si es en Linux / Mac
python -m venv venv
source venv/bin/activate


Instala dependencias:

pip install langgraph pytest

▶️ Ejecutar el chatbot

python -m app.cli


Aparecerá:

🛒 CHATBOT CARRITO DE COMPRA
────────────────────────────────
>

💬 Comandos disponibles
Comando	Descripción
productos	Muestra todos los productos
añadir <id> <cantidad>	Añade productos al carrito
quitar <id> <cantidad>	Quita unidades o elimina un producto
carrito	Muestra el carrito
finalizar	Inicia el proceso de compra
salir	Cierra el programa
🧪 Ejemplo de uso
> productos
1 - Camiseta azul (19.99€)

> añadir 1 2
Camiseta azul x 2 = 39.98€

> quitar 1 1
Camiseta azul x 1 = 19.99€

> finalizar
¿Confirmas? (si/no): no
❌ Pedido cancelado. Carrito conservado.

> carrito
Camiseta azul x 1 = 19.99€

> finalizar
¿Confirmas? (si/no): si
✅ Pedido confirmado

🧪 Ejecutar los tests

Desde la raíz:

pytest -v


Salida esperada:

5 passed


Los tests verifican:

Añadir productos

Eliminar productos

Actualizar cantidades

Calcular total

Eliminar cuando la cantidad es 0

🗂 Estructura del proyecto
app/
├── cli.py
├── domain/
│   ├── cart.py
│   └── product.py
└── graph/
    └── shopping_graph.py

test/
└── test_cart.py

🧠 Arquitectura

El sistema funciona como una máquina de estados:

Usuario → Parser → Estado → LangGraph → Nodo → Respuesta → CLI


LangGraph controla las transiciones entre:

Añadir

Quitar

Mostrar

Checkout

Confirmación

Cancelación

Salida





Proyecto desarrollado por Álvaro como práctica de:

    Arquitectura limpia

    State machines

    LangGraph

    Testing en Python