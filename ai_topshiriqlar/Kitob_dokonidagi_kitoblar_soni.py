# Kitob do'konidagi kitoblar soni
# Kurs: IT Dasturlash
# Mavzu: Dict comprehensions – mapping va filtrlash
# Ball: 100
# Aziz Academy — AI Topshiriq

# starter Python code
n = int(input())
d = {}
for i in range(n):
    kitob = input().split()
    nomi = kitob[0]
    narxi = int(kitob[1])
    janri = kitob[2]
    if janri not in d:
        d[janri] = {'qimmat': 0, 'arzon': 0}
    if narxi > 20000:
        d[janri]['qimmat'] += 1
    else:
        d[janri]['arzon'] += 1
print(d)