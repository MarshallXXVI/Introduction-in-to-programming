from dataclasses import dataclass


@dataclass
class Fahrzeug:
    Zustand: int
    Neupreis: int
    Leergewicht: int
    Baujahr: int

    def __post_init__(self):
        assert(self.Zustand) >= 0, "Zustand +" + str(self.Zustand) + "% muss zwischen 0% und 100% liegen."
        assert(self.Zustand) <= 100 
        assert(self.Neupreis) >= 0
        assert(self.Leergewicht) > 0
        assert(self.Baujahr) > 0

    def gewicht(self) -> int:
        return int(self.Leergewicht)

    def maut(self) -> int:
        raise NotImplementedError

    def alter(self) -> int:
        if self.Baujahr > 2021:
            return 0
        else:
            return 2021 - self.Baujahr

    def markwert(self) -> int:
        result = int(((self.Zustand - (5 * self.alter())) / 100) * self.Neupreis)
        if result < 0:
            return 0
        else:
            return result


@dataclass
class Kraftfahrzeug(Fahrzeug):
    Leistung: int
    Anzahl_Sitzplätze: int

    def __post_init__(self):
        super().__post_init__()
        assert(self.Leistung) > 0
        assert(self.Anzahl_Sitzplätze) > 0

    def plaetze(self) -> int:
        return self.Anzahl_Sitzplätze

    def maut(self) -> int:
        return round(self.gewicht() / 5,) + (self.plaetze() * 25)


@dataclass
class Bus(Kraftfahrzeug):
    Anzahl_Stehplätze: int

    def __post_init__(self):
        super().__post_init__()
        assert(self.Anzahl_Stehplätze) <= self.Anzahl_Sitzplätze

    def plaetze(self) -> int:
        return super().plaetze() + self.Anzahl_Stehplätze


@dataclass
class Fahrrad(Fahrzeug):
    rahmengroesse: int

    def __post_init__(self):
        super().__post_init__()
        assert(self.rahmengroesse) > 0

    def markwert(self) -> int:
        return int(super().markwert() / 2)

    def maut(self) -> None:
        return None


@dataclass
class PKW(Kraftfahrzeug):
    pass


@dataclass
class LKW(Kraftfahrzeug):
    Zuladung: int

    def __post_init__(self):
        super().__post_init__()
        assert(self.Zuladung) > 0
        assert(self.Zuladung) < (2 * self.Leergewicht)

    def maut(self) -> int:
        return super().maut() * 2


print(Bus(25, 100000, 2500, 1995, 200, 80, 40))
print(Fahrrad(100, 500, 10, 2019, 55))
print(PKW(95, 20000, 1200, 2016, 90, 5))
print(LKW(65, 150000, 3200, 1991, 280, 3, 4600))