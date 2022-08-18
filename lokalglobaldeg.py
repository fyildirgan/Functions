# Lokal & Global Değişkenler ( Local & Global Variables)
list_store = [1, 2]         #Global etki alanı
def add_element(a, b):
    c = a * b               #Local etki alanı
    list_store.append(c)
    print(list_store)       #Bu duruma local etki alanından global etki alanını etkilemek denir.

add_element(1, 9)