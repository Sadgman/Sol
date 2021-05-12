import os
import sqlite3

nanombre = sqlite3.connect("users.db")

cursor = nanombre.cursor()


cursor.execute("CREATE TABLE PERSONA(COMPAÑIA VARCHAR ,"
               "NOMBRE VARCHAR UNIQUE , CONTRASEÑA INTEGER)")

nanombre.close()