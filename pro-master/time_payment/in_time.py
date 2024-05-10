from config import*

def in_time(desired_car):
    return  f'Carro comprado à vista {available_cars.get(desired_car).value}'