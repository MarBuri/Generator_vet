import random
import os

def generate_lorem_ipsum(paragraf, min_slabik, max_slabik, min_slov, max_slov):
    samohlasky = "aeiyou"
    souhlasky = "bcdfghjklmnprstvz"

    def vytvor_slovo():
        slabiky_počet = random.randint(min_slabik, max_slabik)
        slovo = ''
        for i in range(slabiky_počet):
            if i % 2 == 0:
                slovo += random.choice(souhlasky)
            else:
                slovo += random.choice(samohlasky)
        return slovo.capitalize()

    def vytvor_vetu():
        slov_pocet = random.randint(min_slov, max_slov)
        veta = ' '.join([vytvor_slovo() for _ in range(slov_pocet)])
        return veta + '.'

    lorem_text = ''
    for _ in range(paragraf): 
        paragraf = ' '.join([vytvor_vetu() for _ in range(vety_v_paragraf)])
        lorem_text += paragraf.capitalize() + '\n\n'

    return lorem_text

while True:
    os.system('cls')
    num_paragraf = input("Zadejte počet odstavců (číslo): ")
    min_slabik_na_slovo = input("Zadejte minimální počet slabik na slovo (číslo): ")
    max_slabik_na_slovo = input("Zadejte maximální počet slabik na slovo (číslo): ")
    min_slov_na_vetu = input("Zadejte minimální počet slov na větu (číslo): ")
    max_slov_na_vetu = input("Zadejte maximální počet slov na větu (číslo): ")
    vety_v_paragraf = input("Zadejte počet paragrafů:")

    num_paragraf = int(num_paragraf)
    min_slabik_na_slovo = int(min_slabik_na_slovo)
    max_slabik_na_slovo = int(max_slabik_na_slovo)
    min_slov_na_vetu = int(min_slov_na_vetu)
    max_slov_na_vetu = int(max_slov_na_vetu)
    vety_v_paragraf = int(vety_v_paragraf)
    os.system('cls')
        
    lorem = generate_lorem_ipsum(
        paragraf=num_paragraf,
        min_slabik=min_slabik_na_slovo,
        max_slabik= max_slabik_na_slovo,
        min_slov=min_slov_na_vetu,
        max_slov=max_slov_na_vetu
        )
    print(lorem)
    input("Opakovat akci znova?")
