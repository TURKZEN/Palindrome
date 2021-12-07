print("""
----------------------------
|     Palindrom Kelime      |
----------------------------

Çıkmak için [q] tuşuna basınız.
""")

while True:
    kelime = input("Kelimeyi Giriniz : ")
    if kelime=="q":
        break
    elif kelime[::-1] == kelime:
        print("Kelime Palindromdur")
    else:
        print("Kelime Palindrom değildir.")
    