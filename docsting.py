# Docstring: Fonksiyonlarımıza herkesin anlayabileceği ortak bir dil ile bilgi notu ekleme yoludur.
def summer(arg1, arg2):
# İlk bölümde fonksiyonun ne yaptığı bilgisi yazılır.
# 2. bölümde bu argümanların tipleri yazabiliriz.
# İstediğimiz kısımlara bilgi girebilmekteyiz.
    """
    Sum of two numbers
    Parameters/Args
    :param arg1: int, float
    :param arg2: int, float
    :return:
        int, float
    """
    print(arg1 + arg2)
help(summer)
summer(1, 3)