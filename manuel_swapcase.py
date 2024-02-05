def manual_swapcase(s):
    # Yeni bir string oluşturmak için boş bir string başlatıyoruz.
    result = ""
    
    # Stringdeki her karakteri kontrol ediyoruz.
    for char in s:
        # Eğer karakter küçük harf ise, büyük harfe çeviriyoruz.
        if char.islower():
            result += char.upper()
        # Eğer karakter büyük harf ise, küçük harfe çeviriyoruz.
        elif char.isupper():
            result += char.lower()
        # Harf değilse, olduğu gibi bırakıyoruz.
        else:
            result += char
    return result

# Fonksiyonu test ediyoruz.
input_str = "Hello, World!"
print(manual_swapcase(input_str))  # Output: "hELLO, wORLD!"
