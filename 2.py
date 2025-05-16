# hojasdevida.py (asumiendo que este archivo maneja la lógica de las hojas de vida)

def buscar_hoja_de_vida(hojas_de_vida, criterio, valor):
    """
    Busca hojas de vida dentro de la lista 'hojas_de_vida'
    por el 'criterio' (nombre, documento, correo) y 'valor' de búsqueda.
    """
    resultados = []
    for hv in hojas_de_vida:
        if criterio == "nombre" and valor.lower() in hv["datos_personales"]["nombre"].lower():
            resultados.append(hv)
        elif criterio == "documento" and valor == hv["datos_personales"]["documento"]:
            resultados.append(hv)
        elif criterio == "correo" and valor.lower() == hv["datos_personales"]["correo"].lower():
            resultados.append(hv)
    return resultados

def filtrar_hojas_de_vida(hojas_de_vida, filtros):
    """
    Filtra hojas de vida según los 'filtros' proporcionados (años_experiencia, formacion, habilidades).
    """
    resultados = []
    for hv in hojas_de_vida:
        cumple_filtros = True
        if "años_experiencia" in filtros and hv["experiencia_profesional"]["duracion"] < filtros["años_experiencia"]:
            cumple_filtros = False
        if "formacion" in filtros and filtros["formacion"] not in [f["titulo"].lower() for f in hv["formacion_academica"]]:
            cumple_filtros = False
        if "habilidades" in filtros and not all(h in hv["habilidades"] for h in filtros["habilidades"]):
            cumple_filtros = False
        if cumple_filtros:
            resultados.append(hv)
    return resultados

def visualizar_hoja_de_vida(hoja_de_vida, seccion=None):
    """
    Muestra la 'hoja_de_vida' en formato legible. 
    Si se especifica 'seccion', muestra solo esa parte.
    """

    if seccion:
        if seccion in hoja_de_vida:
            print(f"--- {seccion.capitalize()} ---")
            for clave, valor in hoja_de_vida[seccion].items():
                print(f"{clave.capitalize()}: {valor}")
        else:
            print(f"Error: Sección '{seccion}' no encontrada en la hoja de vida.")
    else:
        print("--- Hoja de Vida Completa ---")
        for seccion, detalles in hoja_de_vida.items():
            print(f"\n--- {seccion.capitalize()} ---")
            if isinstance(detalles, list):  # Para formación, experiencia, etc.
                for item in detalles:
                    for clave, valor in item.items():
                        print(f"{clave.capitalize()}: {valor}")
            elif isinstance(detalles, dict): # Para datos personales
                for clave, valor in detalles.items():
                    print(f"{clave.capitalize()}: {valor}")
            else: # Para habilidades
                print(detalles)

# Ejemplo de uso (en main.py o donde se gestione el flujo principal)
if __name__ == '__main__':
    # Datos de ejemplo (reemplazar con la lógica de carga de datos)
    hojas_de_vida_ejemplo = [
        {   
            "datos_personales": {"nombre": "Juan Perez", "documento": "123456", "correo": "juan@example.com"},
            "formacion_academica": [{"institucion": "Universidad X", "titulo": "Ingeniero"}, {"institucion": "Instituto Y", "titulo": "Master"}],
            "experiencia_profesional": {"empresa": "Empresa A", "cargo": "Desarrollador", "funciones": "Programar", "duracion": 5},
            "referencias": [],
            "habilidades": ["Python", "Java", "SQL"]
        },
        {
            "datos_personales": {"nombre": "Ana Gomez", "documento": "654321", "correo": "ana@example.com"},
            "formacion_academica": [{"institucion": "Universidad Z", "titulo": "Licenciado"}],
            "experiencia_profesional": {"empresa": "Empresa B", "cargo": "Analista", "funciones": "Análisis de datos", "duracion": 2},
            "referencias": [],
            "habilidades": ["SQL", "Estadística", "R"]
        }
    ]

    # Buscar por nombre
    resultados_nombre = buscar_hoja_de_vida(hojas_de_vida_ejemplo, "nombre", "Juan")
    print("Resultados de búsqueda por nombre:")
    for resultado in resultados_nombre:
        visualizar_hoja_de_vida(resultado)

    # Filtrar por años de experiencia
    resultados_experiencia = filtrar_hojas_de_vida(hojas_de_vida_ejemplo, {"años_experiencia": 3})
    print("\nResultados de filtro por experiencia (> 3 años):")
    for resultado in resultados_experiencia:
        visualizar_hoja_de_vida(resultado)

    # Visualizar una sección específica
    print("\nVisualizar solo datos personales de Ana Gomez:")
    visualizar_hoja_de_vida(resultados_nombre[0], "datos_personales")
