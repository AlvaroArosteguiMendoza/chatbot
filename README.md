■ Chatbot Carrito con LangGraph
Este proyecto es un chatbot de línea de comandos que simula un carrito de compra utilizando una
máquina de estados construida con LangGraph.
Características
- Máquina de estados con LangGraph
- Carrito persistente en memoria
- Confirmación sí / no al finalizar
- Cancelar no borra el carrito
- CLI simple y robusto
- Tests automáticos con Pytest

  
Instalación
git clone https://github.com/AlvaroArosteguiMendoza/chatbot-carrito-langgraph.git
cd chatbot-carrito-langgraph
Crear entorno virtual - Windows
python -m venv venv
venv\Scripts\activate
Crear entorno virtual - Linux / Mac
python -m venv venv
source venv/bin/activate
Instalar dependencias
pip install langgraph pytest

Ejecutar el chatbot
python -m app.cli

Comandos disponibles
productos
añadir <id> <cantidad>
quitar <id> <cantidad>
carrito
finalizar
salir


Ejemplo de uso
> productos
1 - Camiseta azul (19.99€)
> añadir 1 2
Camiseta azul x 2 = 39.98€
> finalizar
¿Confirmas? (si/no): si
■ Pedido confirmado


Ejecutar tests
pytest -v


Estructura del proyecto
app/
■■■ cli.py
■■■ domain/
■ ■■■ cart.py
■ ■■■ product.py
■■■ graph/
 ■■■ shopping_graph.py
test/
■■■ test_cart.py

Arquitectura
Usuario → Parser → Estado → LangGraph → Nodo → Respuesta → CLI

Autor
Proyecto desarrollado por Álvaro como práctica de arquitectura limpia, state machines, LangGraph
y testing en Python.

