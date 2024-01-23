def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)

# Örnek kullanım:
sayi = int(input("Lütfen sayı giriniz: "))

print(faktoriyel(sayi))