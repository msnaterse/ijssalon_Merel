prijzen = {
    "Aarbei" : 3,
    "Vanille" : 4,
    "Chocolade" : 5 
}
aanbieding = prijzen["Aarbei"] * 0.8

reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[:63]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = ["Vandaag", "in", "de", "aanbieding", ":", "vanille", "ijs", ",", "1", "liter", "-", "slechts", "€", {aanbieding} ]

for el in reclame_tekst4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())