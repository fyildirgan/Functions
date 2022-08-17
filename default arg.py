# Ön tanımlı Argümanlar/Parametreler(Default Parameters/Arguments)
def divide(a, b):
    print(a / b)

divide(1, 2)


def divide1(c, d=1):
    print(c / d)

divide1(1)

# Eğer kullanıcı değer girmeyi unutursa ya da istemezse bu durumda eklediğimiz stringi yazdırır.
# Eğer girmek istediği değer varsa say_hi() içine istediğini yazabilir.
def say_hi(string="Merhaba"):
    print(string)
    print("Hello")
    print("Hi")

say_hi()
say_hi("Selam")

