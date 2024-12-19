from conexion import obtener_conexion

# Insertar autor
def insertar_autor(nombre, apellido, seudonimo, genero, fecha_nacimiento, pais_origen):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO autor (nombre, apellido, seudonimo, genero, fecha_nacimiento, pais_origen)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(consulta, (nombre, apellido, seudonimo, genero, fecha_nacimiento, pais_origen))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Autor insertado correctamente.")

# Modificar autor
def modificar_autor(id_autor, nombre=None, apellido=None, seudonimo=None, genero=None, fecha_nacimiento=None, pais_origen=None):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    campos = []
    valores = []

    if nombre:
        campos.append("nombre = %s")
        valores.append(nombre)
    if apellido:
        campos.append("apellido = %s")
        valores.append(apellido)
    if seudonimo:
        campos.append("seudonimo = %s")
        valores.append(seudonimo)
    if genero:
        campos.append("genero = %s")
        valores.append(genero)
    if fecha_nacimiento:
        campos.append("fecha_nacimiento = %s")
        valores.append(fecha_nacimiento)
    if pais_origen:
        campos.append("pais_origen = %s")
        valores.append(pais_origen)

    if campos:
        consulta = f"UPDATE autor SET {', '.join(campos)} WHERE id_autor = %s"
        valores.append(id_autor)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Autor modificado correctamente.")
    else:
        print("No se proporcionaron datos para modificar.")

    cursor.close()
    conexion.close()

# Eliminar autor
def eliminar_autor(id_autor):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "DELETE FROM autor WHERE id_autor = %s"
    cursor.execute(consulta, (id_autor,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Autor eliminado correctamente.")


# Listar todos los autores
def listar_autores():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta = "SELECT *, concat(nombre,' ', apellido) as nombre_autor FROM autor"
    cursor.execute(consulta)
    autores = cursor.fetchall()
    cursor.close()
    conexion.close()
    return autores
