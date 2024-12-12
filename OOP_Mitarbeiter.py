from collections import Counter


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender)
        self.abteilung = abteilung
        abteilung.add_mitarbeiter(self)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender, abteilung)
        if abteilung.leiter is not None:
            print(f"Abteilungsleiter {abteilung.leiter.name} ist bereits für die Abteilung {abteilung.name} eingetragen.")
        else:
            abteilung.set_leiter(self)



class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter):
        self.leiter = leiter

    def mitarbeiteranzahl(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def anzahl_mitarbeiter(self):
        return sum(abt.mitarbeiteranzahl() for abt in self.abteilungen)

    def anzahl_abteilungsleiter(self):
        return sum(1 for abt in self.abteilungen if abt.leiter != None)

    def anzahl_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        if self.abteilungen != None:
            return None
        groessteabt = self.abteilungen[0]
        for abt in self.abteilungen:
            if abt.mitarbeiteranzahl() > groessteabt.mitarbeiteranzahl():
                groessteabt = abt
        return groessteabt

    def geschlechter_prozentanteil(self):
        counter = Counter(m.gender for abt in self.abteilungen for m in abt.mitarbeiter)
        total = sum(counter.values())
        return {
            'M': (counter['M'] / total * 100) if total else 0,
            'F': (counter['F'] / total * 100) if total else 0
        }


firma = Firma("RubnerGmbH")
entwicklung = Abteilung("Entwicklung")
it = Abteilung("IT")
firma.add_abteilung(entwicklung)
firma.add_abteilung(it)
m1 = Mitarbeiter("Max Mustermann", "M", entwicklung)
m2 = Mitarbeiter("Anna Schmidt", "F", entwicklung)
m3 = Mitarbeiter("Lukas Meier", "M", it)
m4 = Mitarbeiter("Eva Müller", "F", it)
leiter_entwicklung = Abteilungsleiter("Peter Lange", "M", entwicklung)
leiter_marketing = Abteilungsleiter("Maria Schulz", "F", it)
leiter_marketing_probe = Abteilungsleiter("Rächer", "F", it)

print(f"Anzahl der Mitarbeiter: {firma.anzahl_mitarbeiter()}")
print(f"Anzahl der Abteilungsleiter: {firma.anzahl_abteilungsleiter()}")
print(f"Anzahl der Abteilungen: {firma.anzahl_abteilungen()}")
groesste_abteilung = firma.groesste_abteilung()
print(f"Größte Abteilung: {groesste_abteilung.name} mit {groesste_abteilung.mitarbeiteranzahl()} Mitarbeitern")
prozentanteile = firma.geschlechter_prozentanteil()
print(f"Geschlechterverteilung: {prozentanteile}")
print(it.leiter.name)
