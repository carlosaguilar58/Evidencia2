class Triangulo:

    def inicializar(self):
        self.lado1=int(input("Ingresa el primer lado de el triangulo:"))
        self.lado2=int(input("Ingresa el segundo lado de el triangulo:"))
        self.lado3=int(input("Ingresa el tercer lado de el triangulo:"))

    def imprimir(self):
        print("Valores de los lados del triangulo")
        print("Lado 1",self.lado1)
        print("Lado 2",self.lado2)
        print("Lado 3",self.lado3)

    def lado_mayor(self):
        print("Lado mayor")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1)
        else:
            if self.lado2>self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def es_equilatero(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")
#Variables principales
triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()