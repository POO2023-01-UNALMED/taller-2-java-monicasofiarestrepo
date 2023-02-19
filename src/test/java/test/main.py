class Auto: 
    cantidadCreados = 0 

    def __init__(self, modelo, asientos, marca, motor, registro, precio):
        self.modelo = modelo
        self.asientos = asientos
        self.marca = marca
        self.motor = motor 
        self.registro = registro
        self.precio= precio
        
        def CantidadAsientos(self):
            numeroAsientos = 0
            for asiento in self.asientos: 
                if isinstance(asiento, asientos): #isinstance(object, type) returns a boolean when the object is in the type
                    numeroAsientos += 1
            return (CantidadAsientos)
        
        def VerificarIdentidad(self): 
            if self.motor.registro != self.registro: 
                return "Las piezas no son originales"
            if self.asiento.registro != self.registro:
                return "Las piezas no son originales"
            else:
                return "Auto Original"
            return(VerificarIdentidad)

class Asiento: 
    def _init_ (self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

        def CambiarColor(self,colores):
            colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
            if color in colores: 
                self.color = color
            return(CambiarColor)

class Motor: 
    def _init_(self,numeroCilinros, tipo, registro):
        self.numeroCilindros = numeroCilinros
        self.tipo = tipo
        self.registro = registro

        def cambiarRegistro (self, registro):
            registronuevo = int(input())
            if registronuevo != registro:
                self.registro = registronuevo
            #return(cambiarRegistro)      

        def asignarTipo(self, tipo):
            tipos =["electrico", "gasolina"]
            tiponuevo = str(input())
            if tiponuevo in tipos:
                self.tipo = tiponuevo
            

    

