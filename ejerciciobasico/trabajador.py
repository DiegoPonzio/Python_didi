nombre = input("Ingrese el numbre del empleado: ")
sueldon = int(input("Ingrese el pago por hora: "))
horas = int(input("Ingrese las horas extras del empleado: "))
hijos = int(input("Ingrese el numero de hijos del empleado: "))

pagoe = sueldon*(0.5 * horas)
hijos = sueldon+(0.5*hijos)
pagot = sueldon+hijos

print("El nombre del empleado es: ", nombre)
print("Su sueldo por hora normal es de: ", sueldon)
print("Su sueldo por trabajar ", horas, " horas es de: ", pagoe)
print("Su sueldo + la bonificacion por hijos es de: ", hijos)
print("Su sueldo todal es de: ", pagot)