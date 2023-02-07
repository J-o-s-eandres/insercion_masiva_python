from mysql.connector import Error
import mysql.connector
from radom_data import data
import time

# print(data)

try:
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="",
        db="inserpy"
    )

    if connection.is_connected():
        # print("Ok")
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO person (id, name , company, job, email, phone, mac_address)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""", data)

        # print(cursor.rowcount)#cantidad de filas afectadas
        # print(len(data)) # longitud de la data
        time.sleep(5)
        if (len(data)==cursor.rowcount):#si todo va bien (la cantidad de filas y la longitud de la data son exactamente igual)
            connection.commit()#confirmar los cambios
            print("{} rows inserted".format(len(data)))

        else:
            connection.rollback()# si la cantidad de filas afectadas y la longitud de la data no sean iguales regresamos la bd a un estado anterior antes de que se hiciera la acción 'insertar' en nuestro caso

except Error as ex:
    print("Error during connection: {}".format(ex))

finally:
    if connection.is_connected():
        connection.close()
        print("Connection Closed")