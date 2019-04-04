class Сombine:

    number_of_treated_fields = 0

    def __init__(self,
                 volume = 0,
                 fuel_consumption = 0,
                 power = 0,
                 price = 0,
                 kind = None,
                 size = 0):
        self.volume = volume
        self.fuel_consumption = fuel_consumption
        self.power = power
        self.price = price
        self.kind = kind
        self.size = size
        Сombine.number_of_treated_fields += 1

    def __del__(self):
        print('combine {} has been deleted'.format(self.volume))

    @staticmethod
    def get_number_of_treated_fields():
        return Сombine.number_of_treated_fields

    def __str__(self):
        return ('volume = {} kg, fuel consumption = {} L, power = {} horsepower, price = {} $, ' +
                'kind = {}, size = {} meters cubic').format(self.volume, self.fuel_consumption,
                                                          self.power, self.price,
                                                          self.kind, self.size)
