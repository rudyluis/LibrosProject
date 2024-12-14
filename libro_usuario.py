from conexion import obtener_conexion

# Relacionar libro con usuario
def insertar_libro_usuario(id_libro, id_usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO libro_usuario (id_libro, id_usuario)
        VALUES (%s, %s)
    """
    cursor.execute(consulta, (id_libro, id_usuario))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Relación libro-usuario insertada correctamente.")

# Eliminar relación libro-usuario
def eliminar_libro_usuario(id_libro_usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "DELETE FROM libro_usuario WHERE id_libro_usuario = %s"
    cursor.execute(consulta, (id_libro_usuario,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Relación libro-usuario eliminada correctamente.")

# Listar todos los libros asociados a un usuario
def listar_libros_por_usuario(id_usuario):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta = """
        SELECT l.id AS id_libro, l.titulo, l.fechaPublicacion, l.ventas
        FROM libro_usuario lu
        INNER JOIN libro l ON lu.id_libro = l.id
        WHERE lu.id_usuario = %s
    """
    cursor.execute(consulta, (id_usuario,))
    libros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return libros

# Listar todos los usuarios asociados a un libro
def listar_usuarios_por_libro(id_libro):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta = """
        SELECT u.id_usuario, u.nombre, u.apellido, u.nombre_usuario, u.email
        FROM libro_usuario lu
        INNER JOIN usuario u ON lu.id_usuario = u.id_usuario
        WHERE lu.id_libro = %s
    """
    cursor.execute(consulta, (id_libro,))
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios


def listar_usuarios_libro():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta = """
        SELECT lu.id_libro_usuario, u.nombre, u.apellido, u.nombre_usuario, u.email,
        l.titulo, concat(a.nombre,' ',a.apellido) as autor
        FROM libro_usuario lu
        INNER JOIN usuario u ON lu.id_usuario = u.id_usuario
        INNER JOIN libro l on l.id_libro = lu.id_libro
        INNER JOIN autor a on l.id_autor =a.id_autor
      
    """
    cursor.execute(consulta)
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios
