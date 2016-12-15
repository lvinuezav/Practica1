from ubidots import ApiClient
import random
import time

api = ApiClient(token='aw3vYXYy13i9xVl75Zt1jQAsQpde8j')
my_variable = api.get_variable('5848c8d47625422c4ec9767e')

dato = 100

while dato > 50:
    dato = random.randrange(40, 80)
    print (dato)
    new_value = my_variable.save_value({'value': dato})
    time.sleep(2)