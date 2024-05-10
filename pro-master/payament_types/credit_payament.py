from config import *
from time_payment.in_time import *
from time_payment.three_months_paymant import *
from time_payment.six_months_paymant import *
from time_payment.nine_months_paymant import *
from time_payment.twelve_months_paymant import *

def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return in_time()
    elif(time_option == 2):
        return three_months_paymant()
    elif(time_option == 3):
        return six_months_paymant()
    elif(time_option == 4):
        return nine_months_paymant()
    elif(time_option == 5):
        return twelve_months_paymant()
    