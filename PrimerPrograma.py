class Persona:

    def inicializar(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def imprimir(self):
        print("Nombre",self.nombre)
        print("Edad",self.edad)

    def mayor_edad(self):
        if self.edad>=18:
            print("La persona es mayor de edad")
        else:
            print("La persona no es mayor de edad")
#Variables principales
persona1=Persona()
persona1.inicializar("Carlos",19)
persona1.imprimir()
persona1.mayor_edad()