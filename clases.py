class Persona:
    nombre = ""
    edad = 0
    pais = ""

    def __init__(self, nombre, edad, pais):
        self.nombre= nombre
        self.edad=edad
        self.pais=pais


    def saludar (self):
        print("hola mi nombre es: {}" .format(self.nombre))






    def despedir(self):
        print('hasta pronto volvere: {}' .format(self.nombre))


    def comprar(self):
        print('puedo comprar x cosa')



    #crear instancia de la clase persona
jonatan = Persona('jonatan mideros', '31' , 'ecuador')

print(jonatan.nombre)
print(jonatan.edad)
print(jonatan.pais)
jonatan.saludar()
jonatan.comprar()
jonatan.despedir()



class Estudiante(Persona):
    colegio=""
    def __init__(self, nombre, edad, pais, colegio):
        Persona.__init__(self, nombre,edad,pais)
        self.colegio = colegio

    def get_colegio(self):
        print('su colegio es: {}' .format(self.colegio))

andrea = Estudiante('andrea', 25, 'chile', 'seminario')
andrea.saludar()
andrea.comprar()
andrea.despedir()
andrea.get_colegio()




class Universidad(Estudiante):
    programa = ""
    def __init__(self, nombre, edad, pais, colegio, programa):
        Estudiante.__init__(self, nombre, edad, pais, colegio )
        self.programa = programa

    def get_programa(self):
        print('su programa es: {}' .format(self.programa))


cesmag = Universidad('carlos',  41, 'Guayana', 'escuela del rock', 'grafico ')

cesmag.saludar()
cesmag.comprar()
cesmag.despedir()
cesmag.get_colegio()
cesmag.get_programa()


class Cargo:
    cargo = ""

    def __init__(self, cargo):
        self.cargo = cargo


    def get_cargo(self):
        print('su cargo es: {}' .format(self.cargo))



class Trabajador(Persona, Cargo):
    sueldo = 0

    def __init__(self, nombre, edad, pais, cargo, sueldo):
        Persona.__init__(self, nombre, edad, pais)
        Cargo.__init__(self,cargo)
        self.sueldo= sueldo


    def get_sueldp(self):
        print('su salario es de : {}' .format(self.sueldo))

diana = Trabajador('diana' , 32, 'chile', 'albañil', 25000000)
diana.saludar()
diana.comprar()
diana.despedir()