# Función para calcular el promedio de las notas de un estudiante
def calcular_promedio(notas):
    notas = [int(nota) for nota in notas]
    promedio = sum(notas) / len(notas)
    return promedio

# Lista de alumnos y sus notas en el formato dado
datos_alumnos = [
    "Juan,98,87,89,90",
    "Jose,90,43,20,40",
    "Pedro,70,80,89,90"
]

# Diccionario para almacenar los promedios
promedios = {}

# Calcular el promedio para cada alumno
for dato in datos_alumnos:
    partes = dato.split(',')
    nombre = partes[0]
    notas = partes[1:]
    promedio = calcular_promedio(notas)
    promedios[nombre] = promedio

# Guardar los promedios en un archivo de texto
with open("promedios.txt", "w") as archivo:
    for nombre, promedio in promedios.items():
        archivo.write(f"{nombre}={promedio}\n")

print("Promedios guardados en 'promedios.txt'")
