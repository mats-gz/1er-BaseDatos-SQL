import mysql.connector

# Establecer conexión
mydb = mysql.connector.connect(
    host="bvs2k5leykzck1tysgjc-mysql.services.clever-cloud.com",
    user="uot7hnrvgt0sxwxz",
    password="",
    database="bvs2k5leykzck1tysgjc"
)

# Crear un cursor
mycursor = mydb.cursor()

# Ejecutar consulta y Obtener resultados
mycursor.execute("SELECT * FROM Colegio")
resultados = mycursor.fetchall()

# Iterar sobre los resultados
for fila in resultados:
    print(fila)

# Ingresar valores en una tabla y Confirmar cambios
mycursor.execute("INSERT INTO Colegio (Nombre_Colegio, Dirección_Colegio, Teléfono_Colegio, Correo_Electrónico_Colegio, Alumnos_Colegio, Finanzas_Colegio) VALUES (%s, %s, %s, %s, %s, %s)", ("Renault", "Rivadavia 938", 1234567890, "itr@gmail.com", 1000, "Desconocido"))
mydb.commit()
print(mycursor.rowcount, "registro insertado.")

# Eliminar datos de una tabla y Confirmar cambios
sql = "DELETE FROM Colegio WHERE Nombre_Colegio = %s"
valores = ("Renault", )
mycursor.execute(sql, valores)
mydb.commit()
print(mycursor.rowcount, "registro(s) eliminado(s).")