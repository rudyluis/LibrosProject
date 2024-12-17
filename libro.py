#from conn import obtener_conexion
import mysql.connector
from mysql.connector import Error
import streamlit as st
from conexion import obtener_conexion

#Insertar Libro
def insertar_libro(titulo, fecha_publicacion, ventas, stock, id_autor):
    conexion= obtener_conexion()
    cursor = conexion.cursor()
    consulta="""
            INSERT INTO libro (titulo, fecha_publicacion,ventas, stock, id_autor)
            VALUES(%s,%s,%s,%s,%s)
    """
    cursor.execute(consulta, (titulo,fecha_publicacion,ventas,stock,id_autor))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Libro insertado correctamente")

#Modificar Libro
def modificar_libro(id_libro, titulo, fecha_publicacion, ventas, stock, id_autor):
    conexion= obtener_conexion()
    cursor = conexion.cursor()
    campos=[]
    valores=[]
    campos.append("titulo = %s")
    campos.append("fecha_publicacion = %s")
    campos.append("ventas = %s")
    campos.append("stock = %s")
    campos.append("id_autor = %s")

    valores.append(titulo)
    valores.append(fecha_publicacion)
    valores.append(ventas)
    valores.append(stock)
    valores.append(id_autor)

    consulta=f"UPDATE libro set {', '.join(campos)} where id_libro =%s"
    valores.append(id_libro)
    cursor.execute(consulta,valores)
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Libro actualizado correctamente")

# Eliminar Libro
def eliminar_libro(id_libro):
    conexion= obtener_conexion()
    cursor = conexion.cursor()
    consulta="DELETE FROM libro WHERE id_libro= %s"
    cursor.execute(consulta, (id_libro,))
    conexion.commit()
    cursor.close()
    conexion.close()
    print("Libro eliminado correctamente")

#Listar Libro

def listar_libros():
    conexion= obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    consulta="""
    Select l.id_libro,
            l.titulo,
            l.fecha_publicacion,
            l.ventas,
            l.stock,
            concat(a.nombre ,' ', a.apellido) as autor_libro
        from libro l 
    inner join autor a on a.id_autor=l.id_autor;"""
    cursor.execute(consulta)
    libros= cursor.fetchall()
    cursor.close()
    conexion.close()
    return libros



def main():
    st.title("Gestion de Libros")
    menu =["Ver Libros", "Registrar Libros", "Editar Libros", "Eliminar Libro"]
    opcion = st.sidebar.selectbox("Menu", menu)
    if opcion == "Ver Libros":
        st.subheader("Lista de Libros")

        conexion= obtener_conexion()
        libros= listar_libros()
        st.write(libros)
        #3if libros:
          #3  st.write(libros)
        #3else:
        st.info("No hay libros")
    #return 0

# ejecutar APP
if __name__ == "__main__":
    main()