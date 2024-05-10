from config import *

def three_months_paymant(desired_car):
    return f'Carro comprado no cartão de crédito em 3 (três) vezes. {available_cars.get(desired_car.value)}' 