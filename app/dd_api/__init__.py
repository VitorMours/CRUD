import requests

#request = requests.get('https://api.open5e.com/')
#print(request.json())

class CharacterCreator:

    # Class Variables
    online_file = "https://media.wizards.com/2022/dnd/downloads/DnD_5E_CharacterSheet_FormFillable.pdf"

    def __init__(self, *args):
        print(args[0])
        character_dict_values = args[0]
        try:
            self.character_name = character_dict_values["name"]
            self.character_class = character_dict_values["class"]
            self.character_level = character_dict_values["level"]
            self.character_background = character_dict_values["background"]
            self.character_race = character_dict_values["race"]
            self.character_alignment = character_dict_values["alignment"]
            self.character_experience = character_dict_values["experience"]
            self.player_name = character_dict_values["player_name"]
        except KeyError as e:
            print(f"Faltou o preenchimento ou foi preenchido co a chave errada o valor: {e}")
