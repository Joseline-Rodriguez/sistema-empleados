# Sistema de gestión de empleados con herencia

# Clase base: Empleado
class Empleado:
    def _init_(self, nombre, id, salario_base):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def _str_(self):
        return f"Empleado: {self.nombre} | ID: {self.id} | Salario base: ${self.salario_base}"

# Subclase: Desarrollador
class Desarrollador(Empleado):
    def _init_(self, nombre, id, salario_base, lenguajes_programacion):
        super()._init_(nombre, id, salario_base)
        self.lenguajes_programacion = lenguajes_programacion

    def calcular_salario(self):
        return self.salario_base * 1.20  # Bono del 20%

    def _str_(self):
        lenguajes = ", ".join(self.lenguajes_programacion)
        return (f"Desarrollador: {self.nombre} | ID: {self.id} | Salario base: ${self.salario_base} "
                f"| Lenguajes: {lenguajes}")

# Subclase: Gerente
class Gerente(Empleado):
    def _init_(self, nombre, id, salario_base, equipo):
        super()._init_(nombre, id, salario_base)
        self.equipo = equipo  # Lista de empleados

    def calcular_salario(self):
        return self.salario_base + 1000  # Bono fijo

    def _str_(self):
        equipo_str = "\n    ".join(str(e) for e in self.equipo)
        return (f"Gerente: {self.nombre} | ID: {self.id} | Salario base: ${self.salario_base}\n"
                f"  Equipo:\n    {equipo_str}")

# Subclase: Interno
class Interno(Empleado):
    def calcular_salario(self):
        return self.salario_base * 0.70  # Reducción del 30%

    def _str_(self):
        return f"Interno: {self.nombre} | ID: {self.id} | Salario base: ${self.salario_base}"

# ------------------------------
# Prueba del sistema (actividades)
# ------------------------------

# Crear desarrolladores
dev1 = Desarrollador("Ana", 101, 3000, ["Python", "JavaScript"])
dev2 = Desarrollador("Luis", 102, 3200, ["Java", "C++"])

# Crear gerente con los desarrolladores en su equipo
gerente = Gerente("Carlos", 201, 5000, [dev1, dev2])

# Crear interno
interno = Interno("Sofía", 301, 2000)

# Lista de empleados
empleados = [dev1, dev2, gerente, interno]

# Imprimir información y salario final de cada uno
for empleado in empleados:
    print(empleado)
    print(f"Salario final: ${empleado.calcular_salario():.2f}")
    print("-" * 50)
