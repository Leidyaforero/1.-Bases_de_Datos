import mysql.connector # type: ignore
from datetime import datetime





# Conectar a la base de datos
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # Cambia por tu usuario de MySQL
        password="1234",       # Cambia por tu contraseña de MySQL
        database="LosDesterrados"
    )

# Funciones CRUD para la tabla Cultivo
def insert_cultivo(id_cultivo, tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO Cultivo (id_cultivo, tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado) VALUES (%s, %s, %s, %s, %s)"
    values = (id_cultivo, tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Cultivo insertado.")

def fetch_cultivo():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cultivo")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_cultivo(id_cultivo, tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE Cultivo SET tipo_planta = %s, fecha_siembra = %s, estado_crecimiento = %s, rendimiento_esperado = %s WHERE id_cultivo = %s"
    values = (tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado, id_cultivo)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Cultivo actualizado.")

def delete_cultivo(id_cultivo):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Cultivo WHERE id_cultivo = %s", (id_cultivo,))
    conn.commit()
    conn.close()
    print("Cultivo eliminado.")

# Funciones CRUD para la tabla Insumo
def insert_insumo(id_insumo, tipo_insumo, cantidad_disponible, fecha_caducidad):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO Insumo (id_insumo, tipo_insumo, cantidad_disponible, fecha_caducidad) VALUES (%s, %s, %s, %s)"
    values = (id_insumo, tipo_insumo, cantidad_disponible, fecha_caducidad)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Insumo insertado.")

def fetch_insumo():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Insumo")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_insumo(id_insumo, tipo_insumo, cantidad_disponible, fecha_caducidad):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE Insumo SET tipo_insumo = %s, cantidad_disponible = %s, fecha_caducidad = %s WHERE id_insumo = %s"
    values = (tipo_insumo, cantidad_disponible, fecha_caducidad, id_insumo)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Insumo actualizado.")

def delete_insumo(id_insumo):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Insumo WHERE id_insumo = %s", (id_insumo,))
    conn.commit()
    conn.close()
    print("Insumo eliminado.")

# Funciones CRUD para la tabla Cliente
def insert_cliente(id_cliente, nombre, correo, telefono):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO Cliente (id_cliente, nombre, correo, telefono) VALUES (%s, %s, %s, %s)"
    values = (id_cliente, nombre, correo, telefono)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Cliente insertado.")

def fetch_cliente():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Cliente")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_cliente(id_cliente, nombre, correo, telefono):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE Cliente SET nombre = %s, correo = %s, telefono = %s WHERE id_cliente = %s"
    values = (nombre, correo, telefono, id_cliente)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Cliente actualizado.")

def delete_cliente(id_cliente):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Cliente WHERE id_cliente = %s", (id_cliente,))
    conn.commit()
    conn.close()
    print("Cliente eliminado.")

# Funciones CRUD para la tabla Venta
def insert_venta(id_venta, cliente_id, fecha_venta, total):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO Venta (id_venta, cliente_id, fecha_venta, total) VALUES (%s, %s, %s, %s)"
    values = (id_venta, cliente_id, fecha_venta, total)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Venta insertada.")

def fetch_venta():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Venta")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_venta(id_venta, cliente_id, fecha_venta, total):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE Venta SET cliente_id = %s, fecha_venta = %s, total = %s WHERE id_venta = %s"
    values = (cliente_id, fecha_venta, total, id_venta)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Venta actualizada.")

def delete_venta(id_venta):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Venta WHERE id_venta = %s", (id_venta,))
    conn.commit()
    conn.close()
    print("Venta eliminada.")

# Funciones CRUD para la tabla Detalle_Venta

def insert_detalle_venta(id_detalle, venta_id, cultivo_id, cantidad, subtotal):
    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO Detalle_Venta (id_detalle, venta_id, cultivo_id, cantidad, subtotal) VALUES (%s, %s, %s, %s, %s)"
    values = (id_detalle, venta_id, cultivo_id, cantidad, subtotal)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Detalle de venta insertado.")

def fetch_detalle_venta():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Detalle_Venta")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def update_detalle_venta(id_detalle, venta_id, cultivo_id, cantidad, subtotal):
    conn = connect_db()
    cursor = conn.cursor()
    query = "UPDATE Detalle_Venta SET venta_id = %s, cultivo_id = %s, cantidad = %s, subtotal = %s WHERE id_detalle = %s"
    values = (venta_id, cultivo_id, cantidad, subtotal, id_detalle)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    print("Detalle de venta actualizado.")

def delete_detalle_venta(id_detalle):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Detalle_Venta WHERE id_detalle = %s", (id_detalle,))
    conn.commit()
    conn.close()
    print("Detalle de venta eliminado.")

# Menú principal
def main():
    print("CRUD de la base de datos LosDesterrados")
    print("Este script permite hacer operaciones CRUD en las tablas Cultivo, Insumo, Cliente, Venta y Detalle_Venta.")
    
    while True:
        print("\n--- Opciones de CRUD ---")
        print("1. **Cultivo**")
        print("   1. Insertar Cultivo")
        print("   2. Consultar Cultivo")
        print("   3. Actualizar Cultivo")
        print("   4. Eliminar Cultivo")
        print("5. **Insumo**")
        print("   5. Insertar Insumo")
        print("   6. Consultar Insumo")
        print("   7. Actualizar Insumo")
        print("   8. Eliminar Insumo")
        print("9. **Cliente**")
        print("   9. Insertar Cliente")
        print("  10. Consultar Cliente")
        print("  11. Actualizar Cliente")
        print("  12. Eliminar Cliente")
        print("13. **Venta**")
        print("  13. Insertar Venta")
        print("  14. Consultar Venta")
        print("  15. Actualizar Venta")
        print("  16. Eliminar Venta")
        print("17. **Detalle Venta**")
        print("  17. Insertar Detalle Venta")
        print("  18. Consultar Detalle Venta")
        print("  19. Actualizar Detalle Venta")
        print("  20. Eliminar Detalle Venta")
        print("21. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        # Operaciones de Cultivo
        if opcion == "1":
            id_cultivo = int(input("ID del Cultivo: "))
            tipo_planta = input("Tipo de Planta: ")
            fecha_siembra = input("Fecha de Siembra (YYYY-MM-DD): ")
            estado_crecimiento = input("Estado de Crecimiento: ")
            rendimiento_esperado = float(input("Rendimiento Esperado: "))
            insert_cultivo(id_cultivo, tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado)

        elif opcion == "2":
            fetch_cultivo()

        elif opcion == "3":
            id_cultivo = int(input("ID del Cultivo a actualizar: "))
            tipo_planta = input("Nuevo Tipo de Planta: ")
            fecha_siembra = input("Nueva Fecha de Siembra (YYYY-MM-DD): ")
            estado_crecimiento = input("Nuevo Estado de Crecimiento: ")
            rendimiento_esperado = float(input("Nuevo Rendimiento Esperado: "))
            update_cultivo(id_cultivo, tipo_planta, fecha_siembra, estado_crecimiento, rendimiento_esperado)

        elif opcion == "4":
            id_cultivo = int(input("ID del Cultivo a eliminar: "))
            delete_cultivo(id_cultivo)

        # Operaciones de Insumo
        elif opcion == "5":
            id_insumo = int(input("ID del Insumo: "))
            tipo_insumo = input("Tipo de Insumo: ")
            cantidad_disponible = float(input("Cantidad Disponible: "))
            fecha_caducidad = input("Fecha de Caducidad (YYYY-MM-DD): ")
            insert_insumo(id_insumo, tipo_insumo, cantidad_disponible, fecha_caducidad)

        elif opcion == "6":
            fetch_insumo()

        elif opcion == "7":
            id_insumo = int(input("ID del Insumo a actualizar: "))
            tipo_insumo = input("Nuevo Tipo de Insumo: ")
            cantidad_disponible = float(input("Nueva Cantidad Disponible: "))
            fecha_caducidad = input("Nueva Fecha de Caducidad (YYYY-MM-DD): ")
            update_insumo(id_insumo, tipo_insumo, cantidad_disponible, fecha_caducidad)

        elif opcion == "8":
            id_insumo = int(input("ID del Insumo a eliminar: "))
            delete_insumo(id_insumo)

        # Operaciones de Cliente
        elif opcion == "9":
            id_cliente = int(input("ID del Cliente: "))
            nombre = input("Nombre del Cliente: ")
            correo = input("Correo del Cliente: ")
            telefono = input("Teléfono del Cliente: ")
            insert_cliente(id_cliente, nombre, correo, telefono)

        elif opcion == "10":
            fetch_cliente()

        elif opcion == "11":
            id_cliente = int(input("ID del Cliente a actualizar: "))
            nombre = input("Nuevo Nombre del Cliente: ")
            correo = input("Nuevo Correo del Cliente: ")
            telefono = input("Nuevo Teléfono del Cliente: ")
            update_cliente(id_cliente, nombre, correo, telefono)

        elif opcion == "12":
            id_cliente = int(input("ID del Cliente a eliminar: "))
            delete_cliente(id_cliente)

        # Operaciones de Venta
        elif opcion == "13":
            id_venta = int(input("ID de la Venta: "))
            cliente_id = int(input("ID del Cliente: "))
            fecha_venta = input("Fecha de Venta (YYYY-MM-DD HH:MM:SS): ")
            total = float(input("Total de la Venta: "))
            insert_venta(id_venta, cliente_id, fecha_venta, total)

        elif opcion == "14":
            fetch_venta()

        elif opcion == "15":
            id_venta = int(input("ID de la Venta a actualizar: "))
            cliente_id = int(input("Nuevo ID del Cliente: "))
            fecha_venta = input("Nueva Fecha de Venta (YYYY-MM-DD HH:MM:SS): ")
            total = float(input("Nuevo Total de la Venta: "))
            update_venta(id_venta, cliente_id, fecha_venta, total)

        elif opcion == "16":
            id_venta = int(input("ID de la Venta a eliminar: "))
            delete_venta(id_venta)

        # Operaciones de Detalle Venta
        elif opcion == "17":
            id_detalle = int(input("ID del Detalle de Venta: "))
            venta_id = int(input("ID de la Venta: "))
            cultivo_id = int(input("ID del Cultivo: "))
            cantidad = float(input("Cantidad: "))
            subtotal = float(input("Subtotal: "))
            insert_detalle_venta(id_detalle, venta_id, cultivo_id, cantidad, subtotal)

        elif opcion == "18":
            fetch_detalle_venta()

        elif opcion == "19":
            id_detalle = int(input("ID del Detalle de Venta a actualizar: "))
            venta_id = int(input("Nuevo ID de la Venta: "))
            cultivo_id = int(input("Nuevo ID del Cultivo: "))
            cantidad = float(input("Nueva Cantidad: "))
            subtotal = float(input("Nuevo Subtotal: "))
            update_detalle_venta(id_detalle, venta_id, cultivo_id, cantidad, subtotal)

        elif opcion == "20":
            id_detalle = int(input("ID del Detalle de Venta a eliminar: "))
            delete_detalle_venta(id_detalle)

        # Salir
        elif opcion == "21":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()



