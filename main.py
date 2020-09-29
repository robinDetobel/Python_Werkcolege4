import maths as m
import words as w
'''
aantal = int(input("Hoeveel getallen wilt u weergeven? "))
print(m.fibonacci(aantal))


print(m.grootste_reeks(5,7,8,6,1,4,7,25,4,7,36,58))

aantal = int(input("Hoeveel getallen wilt u weergeven? "))
print(m.facrotial(aantal))
'''

tekst = input("Geef de tesk in die u wilt onderzoeken: ")
letter = input("geef de letter of her woord dat u zoekt: ")
print(w.finder(tekst, letter))

print(w.keer_om(input("Geef de tekst die u wilt omdraaien: ")))