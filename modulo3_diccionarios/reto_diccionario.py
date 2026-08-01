# Reto Módulo 3: Análisis de Ventas por Región
# Dict anidado: { region: { "Q1": valor, "Q2": valor, "Q3": valor, "Q4": valor } }

ventas_por_region = {
    "Norte":  {"Q1": 12000, "Q2": 15000, "Q3": 13500, "Q4": 18000},
    "Sur":    {"Q1": 9000,  "Q2": 9500,  "Q3": 11000, "Q4": 10500},
    "Este":   {"Q1": 14000, "Q2": 13000, "Q3": 16000, "Q4": 17500},
    "Oeste":  {"Q1": 8000,  "Q2": 8700,  "Q3": 9200,  "Q4": 9800},
}


def calcular_totales_por_region():
    """Calcula el total anual de cada región con items() y sum(values())."""
    return {region: sum(trimestres.values()) for region, trimestres in ventas_por_region.items()}


def region_mayor_ventas(totales):
    """Usa max() con key=lambda para encontrar la región con mayores ventas."""
    return max(totales.items(), key=lambda item: item[1])


def acumular_por_trimestre():
    """Acumula ventas por trimestre con iteración anidada."""
    acumulado = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
    for region, trimestres in ventas_por_region.items():
        for trimestre, valor in trimestres.items():
            acumulado[trimestre] += valor
    return acumulado


def generar_porcentajes(totales):
    """Genera porcentajes con dict comprehension sobre el gran total."""
    gran_total = sum(totales.values())
    return {region: round(valor / gran_total * 100, 1) for region, valor in totales.items()}


def imprimir_reporte(totales, porcentajes):
    """Imprime reporte ordenado de mayor a menor con sorted() + items()."""
    print("--- Reporte de Ventas por Región ---")
    for region, total in sorted(totales.items(), key=lambda item: item[1], reverse=True):
        print(f"{region}: ${total} ({porcentajes[region]}%)")


# --- Prueba del sistema ---
totales = calcular_totales_por_region()
print(f"Totales por región: {totales}\n")

region_top, valor_top = region_mayor_ventas(totales)
print(f"Región con mayores ventas: {region_top} (${valor_top})\n")

acumulado_trimestral = acumular_por_trimestre()
print(f"Ventas acumuladas por trimestre: {acumulado_trimestral}\n")

porcentajes = generar_porcentajes(totales)
imprimir_reporte(totales, porcentajes)