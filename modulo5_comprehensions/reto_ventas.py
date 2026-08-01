# Reto Módulo 5: Analizador de Ventas con las 3 Comprehensions

ventas = [
    {"producto": "laptop",   "categoria": "tecnología", "unidades": 20, "precio": 800},
    {"producto": "teclado",  "categoria": "tecnología", "unidades": 50, "precio": 25},
    {"producto": "mouse",    "categoria": "tecnología", "unidades": 30, "precio": 15},
    {"producto": "monitor",  "categoria": "tecnología", "unidades": 10, "precio": 200},
    {"producto": "escritorio", "categoria": "mobiliario", "unidades": 5, "precio": 350},
    {"producto": "silla",    "categoria": "mobiliario", "unidades": 15, "precio": 90},
]

# 1. List comp: valor_total (unidades * precio) por cada producto
valores_totales = [item["unidades"] * item["precio"] for item in ventas]

# 2. List comp con filtro: productos con valor_total > 1000
productos_alto_valor = [
    item["producto"] for item in ventas
    if item["unidades"] * item["precio"] > 1000
]

# 3. Dict comp: nombre -> {valor, unidades}
producto_info = {
    item["producto"]: {"valor": item["unidades"] * item["precio"], "unidades": item["unidades"]}
    for item in ventas
}

# 4. Dict comp con filtro: ranking_premium (precio > 50), ordenado por valor desc
premium = {
    item["producto"]: item["unidades"] * item["precio"]
    for item in ventas if item["precio"] > 50
}
ranking_premium = dict(sorted(premium.items(), key=lambda x: x[1], reverse=True))

# 5. Set comp: categorías únicas y productos baratos (precio <= 50)
categorias_unicas = {item["categoria"] for item in ventas}
productos_baratos = {item["producto"] for item in ventas if item["precio"] <= 50}

# 6. Combinar las tres: resumen_formateado + gran_total
resumen_formateado = [
    f"{item['producto']}: ${item['unidades'] * item['precio']}" for item in ventas
]
gran_total = sum(valores_totales)


# --- Impresión del reporte ---
print("--- Valores Totales por Producto ---")
print(valores_totales)

print("\n--- Productos de Alto Valor (> $1000) ---")
print(productos_alto_valor)

print("\n--- Información por Producto ---")
print(producto_info)

print("\n--- Ranking Premium (precio > $50), ordenado desc ---")
print(ranking_premium)

print("\n--- Categorías Únicas ---")
print(categorias_unicas)

print("\n--- Productos Baratos (precio <= $50) ---")
print(productos_baratos)

print("\n--- Resumen Formateado ---")
for linea in resumen_formateado:
    print(linea)

print(f"\nGran total: ${gran_total}")