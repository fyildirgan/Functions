# Fonksiyonlar ( Functions): Belirli görevleri yerine getirmek için yazılan kod parçalarıdır.
# Fonksiyon Okuryazarlığı
print("a", "b")
# help(print) diyerek ulaşabiliyoruz.
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# file: a file like object; defaults to the current sys.stdout
# sep: string inserted between values, default the space
# end: string appended after the last value, default the stream
# flush: whether to forcibly flush the stream.
# Type: builtin_function_or_method
# Boşluk yerine başka bir şey ekleyebiliyoruz.
print("a", "b", sep="__")
help(print)


# Fonksiyon Tanımlama
def calculate(x):
    print(x * 2)


calculate(5)
# İki argümanlı/parametreli bir fonksiyon tanımlayalım.
def summer(arg1, arg2):
    print(arg1 + arg2)


summer(7, 8)




