# Reto Módulo 4: Tiendas y Recomendaciones de Películas

# --- Parte 1: Catálogos de tiendas ---
tienda_centro = {"laptop", "mouse", "teclado", "monitor", "audífonos"}
tienda_norte  = {"mouse", "teclado", "webcam", "micrófono"}
tienda_sur    = {"laptop", "monitor", "impresora", "tablet"}

catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte).intersection(tienda_sur)

exclusivos_centro = tienda_centro.difference(tienda_norte, tienda_sur)
exclusivos_norte  = tienda_norte.difference(tienda_centro, tienda_sur)
exclusivos_sur    = tienda_sur.difference(tienda_centro, tienda_norte)

centro_norte_disjuntas = tienda_centro.isdisjoint(tienda_norte)

print("--- Catálogos de Tiendas ---")
print(f"Catálogo completo: {catalogo_completo}")
print(f"Productos comunes en las 3 tiendas: {productos_comunes}")
print(f"Exclusivos centro: {exclusivos_centro}")
print(f"Exclusivos norte: {exclusivos_norte}")
print(f"Exclusivos sur: {exclusivos_sur}")
print(f"¿Centro y Norte sin productos en común?: {centro_norte_disjuntas}")


# --- Parte 2: Recomendaciones de películas ---
usuario1 = {"acción", "comedia", "ciencia ficción", "aventura"}
usuario2 = {"drama", "comedia", "romance", "ciencia ficción"}
usuario3 = {"acción", "aventura", "fantasía", "drama"}

generos_comunes    = usuario1 & usuario2 & usuario3
universo_generos   = usuario1 | usuario2 | usuario3
exclusivos_usuario1 = usuario1 - usuario2 - usuario3
diferencia_1_2     = usuario1 ^ usuario2

print("\n--- Recomendaciones de Películas ---")
print(f"Géneros comunes a los 3 usuarios: {generos_comunes}")
print(f"Universo de géneros: {universo_generos}")
print(f"Exclusivos de usuario1: {exclusivos_usuario1}")
print(f"Diferencia simétrica usuario1/usuario2: {diferencia_1_2}")

# --- Parte 3: Subconjunto y resumen final ---
es_subconjunto = generos_comunes <= usuario1

print("\n--- Resumen Final ---")
print(f"¿Géneros comunes es subconjunto de usuario1?: {es_subconjunto}")
print(f"Total de productos en el catálogo: {len(catalogo_completo)}")
print(f"Total de géneros distintos: {len(universo_generos)}")