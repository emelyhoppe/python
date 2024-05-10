from config import *

def six_months_paymant(desired_car):
    return f'Carro comprado no cartão de crédito em 6 (seis) vezes. {available_cars.get(desired_car).value}' 