import mysql.connector

conexion = mysql.connector.connect(
    user="root", password="n0m3l0",
    host="localhost",
    database="alumno"
)
k = 1
con = conexion.cursor()
con.execute("select * from alumnobatiz")
rs = con.fetchall()
for i in rs:
    bol = i[0]
    nom = i[1]
    appat = i[2]
    apmat = i[3]
    tel = i[4]
    print(k, "° El alumno: ",  nom, " ", appat, " ", apmat, "\n"
          "De numero de boleta:", bol,  "\n"
          "Con numero telefonico: ", tel)
    k += 1

conexion.close()
