# Fonksiyon İçerisinde Fonksiyon Çağırmak
def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


def standardization(a, p):
    print(a * 10 / 100 * p * p)
    return a * 10 / 100 * p * p


standardization(45, 1)


#def all_calculation(varm, moisture, charge, p):
#    a = calculate(varm, moisture, charge)
#    b = standardization(a, p)
#    print(b * 10)


#all_calculation(1, 3, 5, 12)


def all_calculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 19, 12)