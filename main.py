import random as r

meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": " Risa intensa",
            "Fail": "fracaso",
            "Red flag": " Se usa como una alerta cuando alguien tiene actitudes consideradas negativas",
            "Green falg": "Una persona con actitudes o rasgos positivos que pueden indicar que una relación potencial será sana",
            "Cancelad@": "Atacar o descalificar los puntos de vista de otra persona",
            "Petite": "Algo pequeño o ser pequeño",
            "POV": "Punto de vista o desde la perspectiva de alguien",
            "SIMP": "referirse a una persona que está desesperado por la atención y el afecto de otra persona",
            }

print(meme_dict.keys())
word= input("Escribe una palabra que no entiendas o escribe sorprendeme: ").upper()

if word in meme_dict.keys():
    print("El significado es:", meme_dict[word])
elif word == "SORPRENDEME":
    wordr = worder.choice(list(meme_dict.keys()))
    print("La palabra est", wordr, "y el significado es:", meme_dict[wordr])
else:
    print("Esta palabra aún no se ha agregado al diccionario")
