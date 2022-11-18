import random

random_int = random.randint(0,101)
input_int = None
counter = 0

while random_int != input_int:
    input_int = input("Proszę wprowadzić liczbę całkowitą od 0 do 101: ")
    if input_int.isdecimal():
        input_int = int(input_int)
        if  random_int == input_int:
            print("Brawo!")
        elif input_int > random_int:
            print("Ta liczba jest za duża, spróbuj jeszcze raz!")
        elif input_int < random_int:
            print("Ta liczba jest za mała, spróbuj jeszcze raz!")   
    else:
        print("Proszę podać liczbę całkowitą od 0 do 101.")
    counter += 1

print(f"Udało Ci się zgadnąć w {counter} próbach")