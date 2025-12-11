# ============================
#           IF / ELSE
# ============================

# Se usan para tomar decisiones en el código.

# ----------------------------
#        IF (si)
# ----------------------------
# Ejecuta un bloque de código solo si la condición es True.

edad = 20

if edad >= 18:
    print("Sos mayor de edad")   # Se ejecuta si la condición es True

# ----------------------------
#        ELSE (si no)
# ----------------------------
# Se ejecuta si el if anterior NO se cumple.

edad = 15

if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")   # Se ejecuta porque el if es False

# ----------------------------
#        ELIF (si no, si...)
# ----------------------------
# Permite evaluar más condiciones sin crear múltiples if.

nota = 75

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")           # Se ejecuta este
else:
    print("Reprobado")

# ----------------------------
#     ESTRUCTURA GENERAL
# ----------------------------
if condicion:
    # código si es True
elif otra_condicion:
    # código si la primera no se cumplió
else:
    # código si ninguna condición fue True