class ContactManager:
    def __init__(self):
        self.contacts: dict[str, list[str]] = {}

    def create_contact(self, name: str, phone_numbers: list[str]):
        if name in self.contacts:
            return None
        self.contacts[name] = phone_numbers
        return {name: phone_numbers}

    def add_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste.")
        if phone_number in self.contacts[contact_name]:
            raise ValueError("Numero già esistente.")
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def remove_phone_number(self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste.")
        if phone_number not in self.contacts[contact_name]:
            raise ValueError("Numero non trovato.")
        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name not in self.contacts:
            raise ValueError("Il contatto non esiste.")
        if old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Vecchio numero non trovato.")
        index = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number
        return {contact_name: self.contacts[contact_name]}

    def list_contacts(self):
        return list(self.contacts.keys())

    def list_phone_numbers(self, contact_name: str):
        if contact_name in self.contacts:
            return self.contacts[contact_name]
        else:
            return "Errore: il contatto non esiste."

    def search_contact_by_phone_number(self, phone_number: str):
        found_contacts = [name for name, numbers in self.contacts.items() if phone_number in numbers]
        if found_contacts:
            return found_contacts
        else:
            return "Nessun contatto trovato con questo numero di telefono."
