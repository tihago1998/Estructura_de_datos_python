# Reto Módulo 2: Sistema de Catálogo de Películas
# Catálogo: tupla de tuplas (titulo, director, año, puntuacion)

catalogo = (
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Parasite", "Bong Joon-ho", 2019, 8.6),
    ("Coco", "Lee Unkrich", 2017, 8.4),
    ("Whiplash", "Damien Chazelle", 2014, 8.5),
)


def mostrar_catalogo():
    """Desempaqueta cada película en un bucle e imprime su información."""
    for titulo, director, año, puntuacion in catalogo:
        print(f"{titulo} ({año}) - Dir: {director} - Puntuación: {puntuacion}")


def separar_primera():
    """Usa * para separar la primera película del resto."""
    primera, *resto = catalogo
    print(f"Primera película: {primera}")
    print(f"Resto del catálogo: {resto}")
    return primera, resto


def buscar_por_director(nombre_director):
    """Devuelve una tupla con las películas que coinciden con el director."""
    coincidencias = tuple(
        pelicula for pelicula in catalogo if pelicula[1] == nombre_director
    )
    return coincidencias


def obtener_estadisticas():
    """Retorna (min, max, promedio) de las puntuaciones."""
    puntuaciones = [pelicula[3] for pelicula in catalogo]
    return min(puntuaciones), max(puntuaciones), sum(puntuaciones) / len(puntuaciones)


# --- Prueba del sistema ---
mostrar_catalogo()
print()

separar_primera()
print()

resultado = buscar_por_director("Christopher Nolan")
print(f"Películas de Christopher Nolan: {resultado}")
print()

minima, maxima, promedio = obtener_estadisticas()
print(f"Puntuación mínima: {minima}")
print(f"Puntuación máxima: {maxima}")
print(f"Promedio: {promedio:.2f}")