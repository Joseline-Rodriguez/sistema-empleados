# Sistema de gestión de empleados con herencia

class Empleado:
    def __init__(self, nombre, id, salario_base):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f"Empleado: {self.nombre} | ID: {self.id} | Salario base: ${self.salario_base}"

class Desarrollador(Empleado):
    def __init__(self, nombre, id, salario_base, lenguajes_programacion):
        super().__init__(nombre, id, salario_base)
        self.lenguajes_programacion = lenguajes_programacion

    def calcular_salario(self):
        return self.salario_base * 1.20

    def __str__(self):
        lenguajes = ", ".join(self.lenguajes_programacion)
        return (f"Desarrollador: {self.nombre} | ID: {self.id} | Salario base: ${self.salario_base} "
                f"| Lenguajes: {lenguajes}")

class Gerente(Empleado):
    def __init__(self, nombre, id, salario_base, equipo):
        super().__init__(nombre, id, salario_base)
        self.equipo = equipo

    def calcular_salario(self):
        return self.salario_base + 1000

    def __str__(self):
        equipo_str = "\n    ".join(str(e) for e in self.equipo)
        return (f"Gerente: {self.nombre} | ID: {self.id} | Salario base: ${self.salario_base}\n"
                f"  Equipo:\n    {equipo_str}")

class Interno(Empleado):
    def calcular_salario(self):
        return self.salario_base * 0.70

    def __str__(self):
        return f"Interno: {self.nombre} | ID: {self.id} | Salario base: ${self.salario_base}"

dev1 = Desarrollador("Ana", 101, 3000, ["Python", "JavaScript"])
dev2 = Desarrollador("Luis", 102, 3200, ["Java", "C++"])
gerente = Gerente("Carlos", 201, 5000, [dev1, dev2])
interno = Interno("Sofía", 301, 2000)
empleados = [dev1, dev2, gerente, interno]

for empleado in empleados:
    print(empleado)
    print(f"Salario final: ${empleado.calcular_salario():.2f}")
    print("-" * 50)
