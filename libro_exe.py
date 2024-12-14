from libro import insertar_libro, modificar_libro, eliminar_libro, listar_libros

##titulo=input("Titulo Libro")
##fecha_publicacion= input("Fecha Publicacion (YYYY-MM-DD):")
##ventas = int(input("Numero de Ventas:"))
##id_autor = int(input("Id del autor:"))
##stock = 300
##insertar_libro(titulo,fecha_publicacion,ventas,stock,id_autor)
##id_libro= 58
#modificar_libro(id_libro, titulo, fecha_publicacion, ventas, stock, id_autor)

##eliminar_libro(id_libro)
libros=listar_libros()
for libro in libros:
    print(libro)