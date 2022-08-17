# Fonksiyonların Statement/Body Bölümü
# def function_name(parameters/arguments):
#       statements (function body) - gövdesi
def say_hi():
    print("Merhaba")
    print("Hi")
    print("Hello")
say_hi()

# Argüman girerek bir örnek;
def say_hi1(string):
    print(string)
    print("Hi")
    print("Hello")
say_hi1("fakoo")

def multiplication(a, b):
    c = a * b
    print(c)

multiplication(10, 9)

# Girilen değerleri bir liste içinde saklayacak bir fonksiyon.
list_store = []
# Bütün çalışma içerisinde erişilebilen değişkenlere global etki alanındaki değişkenler denir.
# Sadece ilgili döngü, fonksiyon, if yapıları içerisinde oluşturulan ve bu etki alanları içerinde kalan değişkenlere local değişkenler denir.
def add_element(c, d):
    f = c * d
    list_store.append(f)
    print(list_store)

add_element(1, 8)
add_element(18, 8)
add_element(180, 10)
