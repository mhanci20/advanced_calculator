#!/usr/bin/env python3

import math

def calculator():
    print("Gelişmiş Hesap Makinesi")
    print("Seçenekler")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üs Alma")
    print("6. Karekök Alma")
    print("7. Faktöriyel")
    print("8. Sinüs")
    print("9. Kosinüs")
    print("10. Tanjant")

    choice = input("işlem numarasını seçin")

    if choice in ['1', '2', '3', '4', '5']:
       num1 = float(input("Birinci sayıyı girin: "))
       num2 = float(input("İkinci sayıyı girin:  "))

       if choice == '1':
          print("Sonuç:", num1 + num2)
       elif choice == '2':
            print("Sonuç:", num1 - num2)
       elif choice == '3':
            print("Sonuç:", num1 * num2)
       elif choice == '4':
            print("Sonuç:", num1 / num2)
       elif choice == '5':
            print("Sonuç:", math.pow(num1, num2))

    elif choice == '6':
        num = float(input("Karekök almak istediğiniz sayıyı girin: "))
        print("Sonuç:", math.sqrt(num))

    elif choice == '7':
        num = float(input("Faktöriyelini almak istediğiniz sayıyı girin: "))
        print("Sonuç:", math.factorial(num))

    elif choice in ['8', '9', '10']:
        angle = float(input("Açıyı derece cinsinden girin: "))
        radians = math.radians(angle)

        if choice == '8':
           print("Sonuç (sin):", math.sin(radians))
        if choice == '9':
           print("Sonuç (cos):", math.cos(radians))
        if choice == '10':
           print("Sonuç (tan):", math.tan(radians))

    else:
        print("Geçersiz seçim!")

calculator()
