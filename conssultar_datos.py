import pyodbc

# Configuración de la conexión
def conectar():
    try:
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-INURI1V;"  # Cambia esto al nombre de tu servidor
            "DATABASE=LosDesterrados;"
            "Trusted_Connection=yes;"
        )
        print("Conexión exitosa.")
        return conexion
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None

# Función para insertar en la tabla Cultivos
def insertar_cultivo(tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado):
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
    INSERT INTO Cultivos (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado)
    VALUES (?, ?, ?, ?)
    """
    cursor.execute(query, (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado))
    conexion.commit()
    print("Cultivo insertado correctamente.")
    cursor.close()
    conexion.close()

# Función para consultar todos los cultivos
def consultar_cultivos():
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Cultivos"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row.id_cultivo}, Tipo: {row.tipo_planta}, Fecha: {row.fecha_siembra}, Estado: {row.estado_crecimiento}, Rendimiento: {row.rendimiento_esperado}")
    cursor.close()
    conexion.close()

# Función para insertar en la tabla Clientes
def insertar_cliente(nombre, correo, telefono):
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
    INSERT INTO Clientes (nombre, correo, telefono)
    VALUES (?, ?, ?)
    """
    cursor.execute(query, (nombre, correo, telefono))
    conexion.commit()
    print("Cliente insertado correctamente.")
    cursor.close()
    conexion.close()

# Función para consultar todos los clientes
def consultar_clientes():
    conexion = conectar()
    cursor = conexion.cursor()
    query = "SELECT * FROM Clientes"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row.id_cliente}, Nombre: {row.nombre}, Correo: {row.correo}, Teléfono: {row.telefono}")
    cursor.close()
    conexion.close()

# Ejemplo de uso
if __name__ == "__main__":
    # Insertar un nuevo cultivo
    insertar_cultivo("Maíz", "2024-10-28", "Creciendo", 1500.50)

    # Consultar todos los cultivos
    consultar_cultivos()

    # Insertar un nuevo cliente
    insertar_cliente("Juan Pérez", "juan.perez@example.com", "555123456")

    # Consultar todos los clientes
    consultar_clientes()

