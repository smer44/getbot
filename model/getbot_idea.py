

class GetBot:
    
    
    def __init__(self, data_locations, fields, get_functions, put_functions):
        
        self.data_locations = data_locations 
        self.fields = fields 
        self.get_functions = get_functions
        self.put_functions = put_functions 
        #check if all fields are in get_functions and put_functions

        
    def read_location(self, data_location):
        #opening location:
        print('Opening location:', data_location ) 
        data = None # self.open_location(data_location)
        
        for field in self.fields:
            field_value = self.get_functions[field](data)
            self.put_functions[field](field_value)

        #closing location:
            
        
        
            
        