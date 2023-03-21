class Data:
    database = None
    email_connected = None
    drill_pos = 0
    drill_counter = 0

  
    @classmethod 
    def set_email_connected(cls, email_connected):

        cls.email_connected = email_connected


    @classmethod 
    def set_database(cls, database):
        cls.database = database

    @classmethod 
    def set_drill_pos(cls, drill_pos):
        cls.drill_pos = drill_pos

    @classmethod 
    def set_drill_counter(cls, drill_counter):
        cls.drill_counter = drill_counter


    

    
        

    

    
