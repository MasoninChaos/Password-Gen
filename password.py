import random
import pyperclip
method = input("Is the user on the phone? (Y/N)")
alphabet = ['a', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
alphabetNato = ['Alpha', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'Indigo', 'Juliet', 'Lima', 'Mike', 'Oscar',  'Quebec', 'Romeo', 'Sierra', 'Tango', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
SpecialA = ['!', '£', '$','*']
SpecialANato = ['Exclamation Mark', 'Pound Sign', 'Dollar Sign','Asterisk']
capitals = ['A', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
NumbersNato = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
randomA = random.choices(population= alphabet, k=7)
RandomB = random.choices(population= SpecialA, k=1) 
RandomC = random.choices(population= capitals, k=1)
RandomD = random.choices(population=  numbers, k=2)
passwordtest = (randomA + RandomB + RandomC + RandomD)

print(''.join(map(str, passwordtest))) 

pyperclip.copy(''.join(map(str, passwordtest)))
pyperclip.paste()
passwordtest



#TEST TEST TEST