# To'plamning eng katta elementi
# Kurs: IT Dasturlash
# Mavzu: for sikli va range()
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
n = int(input())
raqamlar = list(map(int, input().split()))
eng_katta = raqamlar[0]
for i in range(1, n):
    if raqamlar[i] > eng_katta:
        eng_katta = raqamlar[i]
print(eng_katta)