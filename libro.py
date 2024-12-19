#from conn import obtener_conexion
import mysql.connector
from mysql.connector import Error
import streamlit as st
from conexion import obtener_conexion
import pandas as pd
from autor import listar_autores
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
            concat(a.nombre ,' ', a.apellido) as autor_libro,
            l.id_autor
        from libro l 
    left join autor a on a.id_autor=l.id_autor;"""
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
        if libros:
            libros_df=pd.DataFrame(libros)
            st.write(libros_df)
        else:
            st.info("No hay libros")
    elif opcion == "Registrar Libros":
        st.subheader("Registrar Nuevo Libro")
        with st.form(key="form_registro"):
            titulo = st.text_input("Titulo")
            fecha_publicacion=st.date_input("Fecha de Publicación")  
            ventas= st.number_input("Ventas", min_value=0)
            stock= st.number_input("Stock", min_value=0)
            autores = listar_autores()
            
            opciones_autor={autor['nombre_autor']:autor['id_autor'] for autor in autores}
            autor_seleccionado=st.selectbox("Autor", options=list(opciones_autor.keys()))
            id_autor= opciones_autor[autor_seleccionado]
            #id_autor= st.number_input("id_autor", min_value=0)
            submit_button = st.form_submit_button("Registrar")
            if submit_button:
                insertar_libro(titulo, fecha_publicacion,ventas, stock, id_autor)
                st.success("Libro registrado exitosamente")
    elif opcion =="Editar Libros":
        st.subheader("Editar Libro")
        libros= listar_libros()
        libros_df=pd.DataFrame(libros)
        st.write(libros_df)
        libro_ids =[libro["id_libro"] for libro in libros]
        id_libro=st.selectbox("Selecciona un libro para su edicion", libro_ids)
        
        libro_seleccionado= next((libro for libro in libros if libro["id_libro"]== id_libro), None)
        print(libro_seleccionado)
        with st.form(key="form_edicion"):
            titulo = st.text_input("Titulo", value=libro_seleccionado["titulo"])
            fecha_publicacion=st.date_input("Fecha de Publicación", value=libro_seleccionado["fecha_publicacion"])  
            ventas= st.number_input("Ventas", min_value=0, value= libro_seleccionado["ventas"])
            stock= st.number_input("Stock", min_value=0, value= libro_seleccionado["stock"])
            
            
            ##opciones_autor={autor['nombre_autor']:autor['id_autor'] for autor in autores}
            ##autor_seleccionado=st.selectbox("Autor", options=list(opciones_autor.keys()))
            ##id_autor= opciones_autor[autor_seleccionado]
            id_autor= st.number_input("id_autor", min_value=0, value=libro_seleccionado["id_autor"])
            autores = listar_autores()
            st.write(pd.DataFrame(autores))
            submit_button = st.form_submit_button("Actualizar")
            if submit_button:
                modificar_libro(id_libro, titulo, fecha_publicacion, stock, ventas, id_autor)
                st.warning("Libro actualizado exitosamente!!!")
    elif opcion =="Eliminar Libro":
        st.subheader("Eliminar Libro")
        libros= listar_libros()
        libros_df=pd.DataFrame(libros)
        st.write(libros_df)
        libro_ids =[libro["id_libro"] for libro in libros]
        id_libro=st.selectbox("Selecciona un libro para su eliminacion", libro_ids)

        if st.button("Eliminar Libro"):
            eliminar_libro(id_libro)
            st.error("Libro eliminado correctamente")
    #return 0

# ejecutar APP
if __name__ == "__main__":
    main()