import mysql.connector
from mysql.connector import Error
import streamlit as st
def obtener_conexion():
        # Intentar establecer la conexión
        connect = mysql.connector.connect(
            host="autorack.proxy.rlwy.net",  # Usa la IP si el DNS falla
            user="root",
            password="sijpXgRGVhlXlEUXQuLQNMQOrdadHmGQ",
            database="railway",
            port=54237,
            connection_timeout=300
        )
        return connect