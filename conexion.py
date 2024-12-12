import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
            host="autorack.proxy.rlwy.net",  # Usa la IP si el DNS falla
            user="root",
            password="sijpXgRGVhlXlEUXQuLQNMQOrdadHmGQ",
            database="railway",
            port=54237,
            connection_timeout=30
    )
    print(conexion)
    return conexion