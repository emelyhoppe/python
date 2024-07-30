def area_circulo():
    pi = 3.14
    raio = float(input("digite o raio do seu círculo: "))

    areaCirculo = pi * (raio * raio)

    print (f"O valor da área do seu círuclo é igual a: {areaCirculo}")
    print("Agora vamo calcular a área de um quadrado")

def area_quadrado():
    base = float(input("digite o valor da base: "))
    altura = float(input("digite o valor da altura: "))

    areaQuadrado = base * altura

    print (f"O valor da área do seu quadrado é igual a: {areaQuadrado}")
    print("Agora vamo calcular a área de um triangulo")

def area_triangulo():
    base = float(input("digite o valor da base: "))
    altura = float(input("digite o valor da altura: "))

    areaTriangulo = (base * altura) / 2

    print (f"O valor da área do seu triangulo é igual a: {areaTriangulo}")

area_circulo()
area_quadrado()
area_triangulo()