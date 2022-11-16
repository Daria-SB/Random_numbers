import random

random_int = random.randint(0,101)
input_int = None
counter = 0
while random_int != input_int:
    input_int = int(input("Proszę wprowadzić liczbę od 0 do 101: "))
    if  random_int == input_int:
        print("Brawo!")
    elif input_int > random_int:
        print("Ta liczba jest za duża, spróbuj jeszcze raz!")
    elif input_int < random_int:
        print("Ta liczba jest za mała, spróbuj jeszcze raz!")
    counter += 1

print(f"Udało Ci się zgadnąć w {counter} próbach")
