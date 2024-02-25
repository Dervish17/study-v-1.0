def future(*mass,**const):
    mass_sum = sum(mass)
    constants_product = 1
    for value in const.values():
        constants_product *= value
    if mass_sum * constants_product > VIN:
        return "ACCELERATION"
    elif mass_sum * constants_product < VIN:
        return "DECELERATION"
    else:
        return "UNCHANGED"


VIN = 540
mass = [1, 2, 3, 4, 5]
const = {'e0': 9, 'mu0': 4}
print(future(*mass, **const))
