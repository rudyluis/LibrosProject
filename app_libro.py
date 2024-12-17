import streamlit as st
import pandas as pd
from libro import insertar_libro, modificar_libro, eliminar_libro, listar_libros
import mysql.connector
from mysql.connector import Error
from conn import obtener_conexion


def main():
    st.title("Gestion de Libros")
    menu =["Ver Libros", "Registrar Libros", "Editar Libros", "Eliminar Libro"]
    opcion = st.sidebar.selectbox("Menu", menu)
    if opcion == "Ver Libros":
        st.subheader("Lista de Libros")
        libros=listar_libros()
        if libros:
            st.write(libros)
        else:
            st.info("No hay libros")
    return 0

# ejecutar APP
if __name__ == "__main__":
    main()