# 1. Clases Empleado, Gerente, Desarrollador
class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        return f"{self.nombre} está trabajando en el departamento {self.departamento}."


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo=None):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo if equipo else []

    def trabajar(self):
        return f"{self.nombre} está supervisando al equipo en {self.departamento}."

    def supervisarAEquipo(self):
        return f"{self.nombre} está supervisando a {len(self.equipo)} empleados."


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguajeDeProgramacion):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        return f"{self.nombre} está programando en {self.lenguajeDeProgramacion}."

    def escribirCodigo(self):
        return f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}."


# 2. Clases FiguraGeométrica, Triángulo, Cuadrado
class FiguraGeometrica:
    def calcularArea(self):
        pass


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado


# 3. Clases Electrodoméstico, Lavadora, Refrigerador
class Electrodomestico:
    def __init__(self, marca, modelo, consumoEnergetico):
        self.marca = marca
        self.modelo = modelo
        self.consumoEnergetico = consumoEnergetico

    def encender(self):
        return f"El electrodoméstico {self.marca} {self.modelo} está encendido."


class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, capacidad):
        super().__init__(marca, modelo, consumoEnergetico)
        self.capacidad = capacidad

    def encender(self):
        return f"La lavadora {self.marca} {self.modelo} ha iniciado el ciclo de lavado."

    def iniciarCicloDeLavado(self):
        return f"La lavadora está lavando con capacidad de {self.capacidad} kg."


class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumoEnergetico, tieneCongelador):
        super().__init__(marca, modelo, consumoEnergetico)
        self.tieneCongelador = tieneCongelador

    def encender(self):
        return f"El refrigerador {self.marca} {self.modelo} está regulando la temperatura."

    def regularTemperatura(self):
        return f"El refrigerador está funcionando. ¿Congelador activo?: {self.tieneCongelador}"


# 4. Clases Usuario, Administrador, Cliente
class Usuario:
    def __init__(self, nombreDeUsuario, contrasena):
        self.nombreDeUsuario = nombreDeUsuario
        self.contrasena = contrasena

    def iniciarSesion(self, usuario, contrasena):
        if self.nombreDeUsuario == usuario and self.contrasena == contrasena:
            return f"Inicio de sesión exitoso para {usuario}."
        else:
            return "Credenciales incorrectas."


class Administrador(Usuario):
    def gestionarUsuarios(self):
        return f"El administrador {self.nombreDeUsuario} está gestionando usuarios."


class Cliente(Usuario):
    def realizarCompra(self):
        return f"El cliente {self.nombreDeUsuario} está realizando una compra."