import pandas as pd
import csv

def extraer_nombres_desde_csv(archivo_csv):
    """
    Extrae los nombres de las personas que comentaron desde un archivo CSV
    La clase que contiene los nombres es _ap3a
    """
    nombres = []
    
    try:
        # Intentar leer el archivo CSV
        df = pd.read_csv(archivo_csv)
        
        # Buscar columnas que puedan contener los nombres
        # Primero, buscar columnas que coincidan con el patrón de la clase
        for columna in df.columns:
            if '_ap3a' in str(columna).lower() or 'nombre' in str(columna).lower() or 'user' in str(columna).lower():
                print(f"Columna encontrada: {columna}")
                # Extraer los nombres, eliminando valores nulos
                nombres_columna = df[columna].dropna().astype(str).tolist()
                nombres.extend(nombres_columna)
        
        # Si no se encontraron nombres, buscar en todas las columnas
        if not nombres:
            print("Buscando en todas las columnas...")
            for _, fila in df.iterrows():
                for valor in fila:
                    if isinstance(valor, str) and valor.strip():
                        # Asumir que podría ser un nombre
                        nombres.append(valor.strip())
        
        # Eliminar duplicados y limpiar los nombres
        nombres = list(set([nombre.strip() for nombre in nombres if nombre and nombre.strip()]))
        
        print(f"Se encontraron {len(nombres)} nombres únicos.")
        
        # Guardar los nombres en un archivo de texto
        with open('lista_nombres.txt', 'w', encoding='utf-8') as f:
            for nombre in nombres:
                f.write(nombre + '\n')
        
        print("Lista de nombres guardada en 'lista_nombres.txt'")
        
        return nombres
        
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return []

def realizar_sorteo(nombres):
    """Realiza un sorteo aleatorio de la lista de nombres"""
    import random
    
    if not nombres:
        print("No hay nombres para realizar el sorteo.")
        return None
    
    ganador = random.choice(nombres)
    print(f"\n🎉 ¡El ganador del sorteo es: {ganador}! 🎉")
    print(f"De un total de {len(nombres)} participantes.")
    
    # Guardar el resultado del sorteo
    with open('resultado_sorteo.txt', 'w', encoding='utf-8') as f:
        f.write(f"Ganador del sorteo: {ganador}\n")
        f.write(f"Total de participantes: {len(nombres)}\n")
        f.write(f"Lista completa de participantes:\n")
        for nombre in sorted(nombres):
            f.write(f"- {nombre}\n")
    
    return ganador

# Ejemplo de uso
if __name__ == "__main__":
    archivo_csv = input("Ingrese el nombre del archivo CSV: ")
    nombres = extraer_nombres_desde_csv(archivo_csv)
    
    if nombres:
        print("\nLista de personas que comentaron:")
        for i, nombre in enumerate(nombres, 1):
            print(f"{i}. {nombre}")
        
        # Preguntar si se desea realizar un sorteo
        respuesta = input("\n¿Desea realizar un sorteo? (s/n): ")
        if respuesta.lower() == 's':
            realizar_sorteo(nombres)