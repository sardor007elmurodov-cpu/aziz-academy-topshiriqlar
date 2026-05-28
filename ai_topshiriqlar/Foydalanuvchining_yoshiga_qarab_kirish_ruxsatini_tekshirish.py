# Foydalanuvchining yoshiga qarab kirish ruxsatini tekshirish
# Kurs: IT Dasturlash
# Mavzu: Mantiqiy operatorlar: and, or, not
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
yosh = int(input())
if yosh > 18 or yosh < 7:
    if yosh > 18:
        ortacha_ball = int(input())
        if ortacha_ball > 80:
            print("Kirish ruxsati berildi. Maxsus imtiyozlar berildi")
        else:
            print("Kirish ruxsati berildi")
    else:
        print("Kirish ruxsati berildi")
else:
    print("Kirish ruxsati berilmadi")