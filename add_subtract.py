# Toplama ve  çıkarma oparatörünü kullanmadan toplama ve çıkarma işlemi gerçekleştirme. 

def add(a, b):
    while b != 0:
        carry = a & b 
        a = a ^ b
        b = carry << 1
    return a

def subtract(a, b):
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a

# Örnek Kullanım:
num1 = 15
num2 = 4

result_add = add(num1, num2)
result_subtract = subtract(num1, num2)

print("Toplama Sonucu:", result_add)
print("Çıkarma Sonucu:", result_subtract)
