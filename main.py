import combine

default_combine = combine.Сombine()
acros_combine = combine.Сombine(volume = 5,
                                fuel_consumption = 10,
                                power = 500,
                                price = 10000,
                                kind = 'Combine for harvesting legumes',
                                size = 7)
vector_combine = combine.Сombine(volume = 8,
                                 power = 5000,
                                 kind = 'Beet-Growing Combine',)

print(default_combine)
print(acros_combine)
print(vector_combine)