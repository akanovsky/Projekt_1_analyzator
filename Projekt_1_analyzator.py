#definice promennych

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = [["bob","123"],["ann","pass123"],["mike","password123"],["liz","pass123"]]

ODDELOVAC = "-" * 50

nr_capital = 0 #slova s velkym prvnim pismenem
nr_up = 0 #slova napsana velkymi pismeny
nr_low = 0 #slova napsana malymi pismeny
nr_numbers = 0 #cisla
sum_numbers = 0 #soucet cisel
len_words = {}
text_l = []

#hlavni telo programu

#prihlaseni do programu

print (ODDELOVAC)
print ("Text analyser")
print(ODDELOVAC)
jmeno = input("username : ")
heslo = input("password : ")
# vyhodnoceni pristupovych udaju
if [jmeno,heslo] in uzivatele:
    stav_ok = True
    print(ODDELOVAC)
    print (f"Welcome to the app, {jmeno} ")

else:
    print("unregistered user, terminating the program..")
    exit()



print("We have 3 texts to be analyzed.")
print(ODDELOVAC)

#vyber textu
cislo_textu = input ("Enter a number btw. 1 and 3 to select: ")
if cislo_textu in ("1","2","3"):
    print(ODDELOVAC)
else:
        print("Unknown text identification, terminating the program...")
        exit()
#analyza vybraneho textu
cislo_textu = int(cislo_textu) - 1
vybrany_text = TEXTS[cislo_textu].replace("\n", " ") #odstraneni koncu radku


text_l = vybrany_text.split(" ") #prevod textu do listu
vybrany_text_ocisteny = []
for i in text_l:
     if i != "":
        vybrany_text_ocisteny.append(i.strip(",.''")) #odstraneni nevhodnych znaku

#analyza pismen a cisel
for i in vybrany_text_ocisteny:
    if i.istitle():
        nr_capital += 1
    if i.isupper() and i.isalpha():
        nr_up += 1
    if i.islower():
        nr_low += 1
    if i.isnumeric():
        nr_numbers += 1
        sum_numbers += int(i)
    x=len(i)
    len_words[x] = len_words.get(x,0) + 1


print(f"There are {len(vybrany_text_ocisteny)} words in selected text.")
print(f"There are {nr_capital} titlecase words.")
print(f"There are {nr_up} uppercase words.")
print(f"There are {nr_low} lowercase words.")
print(f"There are {nr_numbers} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}.")
print(ODDELOVAC)
print("LEN |     OCCURENCES      |NR.")
print(ODDELOVAC)
len_words = dict(sorted(len_words.items()))
for key in len_words:
    print(" " * (2-len(str(key))),key,"|","*" * len_words.get(key)," " * (18-len_words.get(key)) ,"|",len_words.get(key))
