import functools
import math
def convertStringtoList(masses):
    massList = masses.strip().replace(" ", "").split(",")
    return list(map(lambda mass: int(mass), massList))

def getFuelAmount(masses):
    if isinstance(masses, str):
        masses = convertStringtoList(masses)
    totalFuel = functools.reduce(lambda acc, mass: acc + ((math.floor(mass/3))-2), masses)
    return totalFuel

if __name__=="__main__":
    module = [12, 14, 1969, 100756]
    module2 = "12, 14, 1969, 100756"
    print("total Amount Of Fuel: ", getFuelAmount(module))
