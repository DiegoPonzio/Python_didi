sueldo = int(input("Ingrese el sueldo del empleado $"))

if sueldo < 4000:
    sueldo = sueldo+sueldo*0.15
else:
    sueldo = sueldo+sueldo*0.08

print("EL sueldo del empleado con el aumento es de $", sueldo)
