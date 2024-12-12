import random
#import pyperclip
from dataclasses import dataclass
#method = input("Is the user on the phone? (Y/N)")
alphabet = ['a', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
alphabetNato = ['Alpha', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'Indigo', 'Juliet', 'Lima', 'Mike', 'Oscar',  'Quebec', 'Romeo', 'Sierra', 'Tango', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
SpecialA = ['!', '£', '$','*']
SpecialANato = ['Exclamation Mark', 'Pound Sign', 'Dollar Sign','Asterisk']
capitals = ['A', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
NumbersNato = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']


class CharecterB: 
    def __init__(self, lower, upper, nato): 
        self.lower = lower 
        self.upper = upper 
        self.nato = nato 
    def printlower(self): 
    
        return self.lower
    def printupper(self):
        return self.upper 
    def printnato(self):
        return self.nato


charactersA = [
CharecterB("a", "A", "Alpha"),
CharecterB("d", "D", "Delta"),
CharecterB("e", "E", "Echo"),
CharecterB("f", "F", "Foxtrot"),
CharecterB("g", "G", "Golf"),
CharecterB("h", "H", "Hotel"),
CharecterB("i", "I", "Indigo"),
CharecterB("j", "J", "Juliet"),
CharecterB("l", "L", "Lima"),
CharecterB("m", "M", "Mike"),
CharecterB("o", "O", "Oscar"),
CharecterB("q", "Q", "Quebec"),
CharecterB("r", "R", "Romeo"),
CharecterB("s", "S", "Sierra"),
CharecterB("t", "T", "Tango"),
CharecterB("v", "V", "Victor"),
CharecterB("w", "W", "Whiskey"),
CharecterB("x", "X", "X-ray"),
CharecterB("y", "Y", "Yankee"),
CharecterB("z", "Z", "Zulu"),
]
#turn into class V
class CharecterC: 
    def __init__(self, Number, Written): 
        self.number = Number
        self.written = Written
        
    def printnumber(self): 
        return self.number
    def printwritten(self):
        return self.written 

NumbersA = [
CharecterC("0", "Zero"),
CharecterC("1", "One"),
CharecterC("2", "Two"),
CharecterC("3", "Three"),
CharecterC("4", "Four"),
CharecterC("5", "Five"),
CharecterC("6", "Six"),
CharecterC("7", "Seven"),
CharecterC("8", "Eight"),
CharecterC("9", "Nine"),
]
#Turn into class V
class CharecterD: 
    def __init__(self, Symbol, SWritten): 
        self.Symbol = Symbol
        self.SWritten = SWritten
        
    def printSymbol(self): 
    
        return self.Symbol
    def printSWritten(self):
        return self.SWritten 
SpecialAN = [
CharecterD("!", "Exlamation Mark"),        
CharecterD("£", "Pound Sign"),
CharecterD("$", "Dollar Sign"),
CharecterD("*", "Asterisk"),
]



#randoma = random.choices(population= charactersA, k=7)
#RandomB = random.choices(population= SpecialAN, k=1) 

#RandomC = random.choices(population= capitals, k=1)
#RandomD = random.choices(population=  NumbersA, k=2) 


#Loop over each with new classes to build string 
randomA = random.choices(population= charactersA, k=7)
RandomB = random.choices(population= NumbersA, k=1) 
RandomC = random.choices(population= SpecialAN, k=1)
#RandomD = random.choices(population=  CharecterD, k=2)
passwordtest = (randomA + RandomB + RandomC)

#print(''.join(map(str, passwordtest))) 

#pyperclip.copy(''.join(map(str, passwordtest)))
#pyperclip.paste()
#passwordtest

#Generate hte password from the classes
for c in randomA:
    print(c.printlower(),end= "")

for c in RandomB:
    print(c.printnumber(),end= "")

for c in RandomC:
    print(c.printSymbol(),end= "")
print("   - ")


#Write out the password for the operator 
for c in randomA:
    print(c.printnato(),end= " ") 
for c in RandomB:
    print(c.printwritten(),end= " ")
for c in RandomC:
    print(c.printSWritten(),end= " ")


#print(passwordtest)


#TEST TEST TEST