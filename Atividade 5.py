class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor):
        self.motor = motor


motor_gasolina = Motor("Gasolina", 150)
motor_eletrico = Motor("Elétrico", 200)
motor_diesel = Motor("Diesel", 180)


carro1 = Carro(motor_gasolina)
carro2 = Carro(motor_eletrico)
carro3 = Carro(motor_diesel)


print(f"Carro 1 tem um motor {carro1.motor.tipo} de {carro1.motor.potencia} cavalos de potência")
print(f"Carro 2 tem um motor {carro2.motor.tipo} de {carro2.motor.potencia} cavalos de potência")
print(f"Carro 3 tem um motor {carro3.motor.tipo} de {carro3.motor.potencia} cavalos de potência")