from dominio.Pelicula import Pelicula
from servicio.catalago_peliculas import CatalagoPeliculas as cp

opcion = None
while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar pelicula')
        print('3. Eliminar catalogo de peliculas')
        print('4. Salir')
        opcion = int(input('Escribe tu opcion: '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_pelicula()
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
else:
    print('Salimos del progroma...')