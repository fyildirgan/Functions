# Return: Fonksiyon çıktılarını girdi olarak kullanmak
#def calculate(varm, moisture, charge):
#    print((varm + moisture)/charge)
# Eğer böyle bir işlem yapmaya çalışırsak Error alırız sebebi calculate olan kısım NoneType olduğundan bir integer değer ile çarpamayacağımızı söyler.
#calculate(98, 12, 78) * 10

def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)
    return (varm + moisture)/charge

calculate(98, 12, 78) * 10
y = calculate(98, 12, 78) * 10
def matrix(ayi, boga, aslan):
    ayi = ayi * 2
    boga = boga * 2
    aslan = aslan * 2
    output = (ayi + boga) / aslan
    print(ayi, boga, aslan, output)
    return ayi, boga, aslan, output

matrix(98, 12, 78)
print(type(matrix(98, 12, 78)))
ayi, boga, aslan, output = matrix(98, 12, 78)