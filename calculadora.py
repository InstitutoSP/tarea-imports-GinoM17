import funcionescalc as fn

x=input("ingresar una funcion suma,resta,multiplicar,dividir: ")
x1=int(input("ingresar el primer numero"))
x2=int(input("ingresar el primer numero"))

if x == "suma":
  s=suma(x1,x2)
  print("el resultado es",s)

elif x== "resta":
  r=resta(x1,x2)
  print("el resultado es",r)

elif x== "multiplicar":
  m=multiplicar(x1,x2)
  print("el resultado es",m)

elif x== "dividir":
  d=dividir(x1,x2)
  print("el resultado es",d)


