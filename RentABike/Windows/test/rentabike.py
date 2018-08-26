class Rent():

    def __init__(self, bikes, mod, time_rent, isFamilyRental):
        self.bikes = bikes
        self.mod = mod
        self.time_r = time_rent
        self.var = isFamilyRental
    def rent_cost (self):
        type = {'1':5, '2':20, '3':60}
        if (self.bikes >= 3 and self.bikes <= 5) and self.var == False:
	        return (self.bikes*type[self.mod]*self.time_r)*0.7
        else:
            return self.bikes*type[self.mod]*self.time_r

	def __str__(self):
		return rent_cost()
