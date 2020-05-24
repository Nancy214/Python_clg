#Constructor and destructor
class Vehicle: 

    def __init__(self): 
        print('Vehicle created.')

    def __del__(self): 
        print('Destructor called, Vehicle deleted.')
        
def run():
    print('Vehicle running')
    obj = Vehicle()
    return obj
  
obj = run() 
del obj
