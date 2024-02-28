class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI


class Empleado(Persona):
    def __init__(self, nombre, edad, DNI, anio_ingreso):
        super().__init__(nombre, edad, DNI)
        self.anio_ingreso = anio_ingreso


class Empleado_comision(Empleado):
    def __init__(self, nombre, edad, DNI, anio_ingreso, salario_minimo, clientes_captados, ganacia_por_cliente):
        super().__init__(nombre, edad, DNI, anio_ingreso)
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.anio_ingreso = anio_ingreso
        self.salario_minimo = salario_minimo
        self.clientes_captados = clientes_captados
        self.ganacia_por_cliente = ganacia_por_cliente

    def mostrarSalario(self):
        return (self.clientes_captados*self.ganacia_por_cliente) if (self.clientes_captados*self.ganacia_por_cliente) < self.salario_minimo else self.salario_minimo


class Empleado_fijo(Empleado):
    def __init__(self, nombre, edad, DNI, anio_ingreso, salario_fijo, salario_porcentaje,):
        super().__init__(nombre, edad, DNI, anio_ingreso)
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.anio_ingreso = anio_ingreso
        self.salario_fijo = salario_fijo
        self.salario_pocentaje = salario_porcentaje

    def mostrarSalario(self):
        if (self.anio_ingreso < 2):
            return self.salario_fijo
        elif (self.anio_ingreso > 5):
            return float(self.salario_fijo)*0.10
        else:
            return float(self.salario_fijo)*0.5


def empleadoConMasClientes(listaEmpleados):
    if not listaEmpleados:
        return None
    empleado_con_mas_clientes = max(
        listaEmpleados, key=lambda emp: emp.clientes_captados)

    return empleado_con_mas_clientes


SALARIO_MINIMO = 200000
GANANCIA_POR_CLIENTE = 10000

listaEmpleadosComision = [
    Empleado_comision("EmpleadoComision1", "36", 12345671, 2010,
                      SALARIO_MINIMO, 5, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision2", "30", 12345672, 2011,
                      SALARIO_MINIMO, 4, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision3", "36", 12345673, 2010,
                      SALARIO_MINIMO, 3, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision4", "35", 12345674, 2015,
                      SALARIO_MINIMO, 2, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision5", "38", 12345675, 2010,
                      SALARIO_MINIMO, 6, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision6", "46", 12345676, 2011,
                      SALARIO_MINIMO, 7, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision7", "26", 12345677, 2015,
                      SALARIO_MINIMO, 8, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision8", "56", 12345678, 2010,
                      SALARIO_MINIMO, 9, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision9", "53", 12345679, 2011,
                      SALARIO_MINIMO, 10, GANANCIA_POR_CLIENTE,),
    Empleado_comision("EmpleadoComision10", "33", 12345610, 2015,
                      SALARIO_MINIMO, 12, GANANCIA_POR_CLIENTE,),
]

empleado_con_mas_clientes = empleadoConMasClientes(listaEmpleadosComision)

print(f"El empleado con mayor clientes es: {empleado_con_mas_clientes.nombre}")
