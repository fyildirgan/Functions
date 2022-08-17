# Ne zaman fonksiyon yazma ihtiyacımız olur?
# varm, moisture, charge
#print((56 + 15) / 80)
#print((17 + 45) / 70)
#print((52 + 45) / 80)
# Don't repeat your self(DRY) presinsibi der ki;
# Birbirini tekrar eden görevler söz konusu olduğunda fonksiyon yazma ihtiyacı kendisi hissettirecektir.
def calculate(varm, moisture, charge):
    print((varm + moisture)/charge)

calculate(98, 12, 78)

