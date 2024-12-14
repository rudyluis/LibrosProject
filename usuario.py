from conexion import obtener_conexion

# Insertar usuario
def insertar_usuario(nombre, apellido, nombre_usuario, email):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO usuario (nombre, apellido, nombre_usuario, email)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(consulta, (nombre, apellido, nombre_usuario, email))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Usuario insertado correctamente.")

# Modificar usuario
def modificar_usuario(id_usuario, nombre=None, apellido=None, nombre_usuario=None, email=None):
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
    if nombre_usuario:
        campos.append("nombre_usuario = %s")
        valores.append(nombre_usuario)
    if email:
        campos.append("email = %s")
        valores.append(email)

    if campos:
        consulta = f"UPDATE usuario SET {', '.join(campos)} WHERE id_usuario = %s"
        valores.append(id_usuario)
        cursor.execute(consulta, valores)
        conexion.commit()
        print("Usuario modificado correctamente.")
    else:
        print("No se proporcionaron datos para modificar.")

    cursor.close()
    conexion.close()

# Eliminar usuario
def eliminar_usuario(id_usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "DELETE FROM usuario WHERE id_usuario = %s"
    cursor.execute(consulta, (id_usuario,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Usuario eliminado correctamente.")

# Buscar usuarios por nombre de usuario
def buscar_usuarios_por_nombre_usuario(nombre_usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta = "SELECT * FROM usuario WHERE nombre_usuario LIKE %s"
    cursor.execute(consulta, (f"%{nombre_usuario}%",))
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios

# Listar todos los usuarios
def listar_usuarios():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta = "SELECT * FROM usuario"
    cursor.execute(consulta)
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios
