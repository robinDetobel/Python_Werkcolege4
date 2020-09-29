import maths as m
import words as w
import regular_expressions as r
'''
aantal = int(input("Hoeveel getallen wilt u weergeven? "))
print(m.fibonacci(aantal))


print(m.grootste_reeks(5,7,8,6,1,4,7,25,4,7,36,58))

aantal = int(input("Hoeveel getallen wilt u weergeven? "))
print(m.facrotial(aantal))


tekst = input("Geef de tesk in die u wilt onderzoeken: ")
letter = input("geef de letter of her woord dat u zoekt: ")
print(w.finder(tekst, letter))

print(w.keer_om(input("Geef de tekst die u wilt omdraaien: ")))
'''

if r.hoofletter_naam(input("Geef een naam in: ")):
    print("naam is toegestaan")
else:
    print("naam moet met een hoofdletter starten")


if r.telnr_correct(input("Geef een telefoonnummer in: ")):
    print("nummer is toegestaan")
else:
    print("nummer moet met een 0 starten en 10 cijfers lang zijn")


if r.ww_nummer(input("Geef een wachtwoord in: ")):
    print("watchwoord is toegestaan")
else:
    print("watchwoord moet minstens 1 cijfer bevatten")


if r.email_valid(input("Geef een email in: ")):
    print("email is toegestaan")
else:
    print("email moet 1 @ bevatten en een punt hebben na de @")

