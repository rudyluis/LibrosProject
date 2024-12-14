from autor import listar_autores, insertar_autor

autores=listar_autores()
print(autores)


nombre = input("Nombre: ")
apellido = input("Apellido: ")
seudonimo = input("Seudónimo: ")
genero = input("Género: ")
fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
pais_origen = input("País de origen: ")
insertar_autor(nombre, apellido, seudonimo, genero, fecha_nacimiento, pais_origen)