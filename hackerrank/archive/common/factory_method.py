# class FrenchLocalizer:
#     def __init__(self):
#         self.translations = {
#             "car": "voiture",
#             "bike": "bicyclette",
#             "cycle": "cyclette"
#         }

#     def localize(self, msg):
#         return self.translations.get(msg)


# class SpanishLocalizer:
#     def __init__(self):
#         self.translations = {
#             "car": "coche",
#             "bike": "bicicleta",
#             "cycle": "ciclo"
#         }
    
#     def localize(self, msg):
#         return self.translations.get(msg)


# class EnglishLocalizer:
#     def localize(self, msg):
#         return msg



# if __name__ == "__main__":
#     f = FrenchLocalizer()
#     s = SpanishLocalizer()
#     e = EnglishLocalizer()

#     print(e.localize("car"))


class FrenchLocalizer:
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }

    def localize(self, msg):
        return self.translations.get(msg)


class SpanishLocalizer:
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }
    
    def localize(self, msg):
        return self.translations.get(msg)


class EnglishLocalizer:
    def localize(self, msg):
        return msg


def Factory(language="English"):
    localizers = {
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
        "French": FrenchLocalizer
    }

    return localizers[language]()


if __name__ == "__main__":
    f = Factory("French")
    s = Factory("Spanish")
    e = Factory("English")

    print(f.localize("car"))


