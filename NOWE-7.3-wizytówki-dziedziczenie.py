from faker import Faker
fake = Faker(['pl_PL'])

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, e_mail):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.e_mail = e_mail
    
    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.telefon} {self.e_mail}'
    
    def contact(self):
        print(f'Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}')

    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, e_mail, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, e_mail)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def __str__(self):
        return f'{super().__str__()} {self.stanowisko} {self.firma} {self.telefon_sluzbowy}'
    
    def contact(self):
        print(f'Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}')

    @property
    def label_length(self):
        return len(self.imie) + len(self.nazwisko)

def create_contacts(rodzaj, ilosc):
    contacts = []
    for _ in range(ilosc):
        if rodzaj == 'base':
            person = BaseContact(imie=fake.first_name(), nazwisko=fake.last_name(), telefon=fake.phone_number(), e_mail=fake.email())
        elif rodzaj == 'business':
            person = BusinessContact(imie=fake.first_name(), nazwisko=fake.last_name(), telefon=fake.phone_number(), e_mail=fake.email(),
                                     stanowisko=fake.job(), firma=fake.company(), telefon_sluzbowy=fake.phone_number())
        else:
            raise ValueError("Niepoprawny rodzaj wizytówki. Wprowadź 'base' lub 'business'.")
        contacts.append(person)
    return contacts

wygenerowane_podstawowe = create_contacts('base', 5)
wygenerowane_firmowe = create_contacts('business', 5)

print("Wygenerowane wizytówki podstawowe:")
for contact in wygenerowane_podstawowe:
    print(contact)
    print(f'Długość imienia i nazwiska: {contact.label_length}')
    contact.contact()

print("\nWygenerowane wizytówki firmowe:")
for contact in wygenerowane_firmowe:
    print(contact)
    print(f'Długość imienia i nazwiska: {contact.label_length}')
    contact.contact()
