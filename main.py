from datetime import datetime


class CardType:
    def __init__(self, name: str) -> None:
        self.name = name


class Card:
    def __init__(self, name: str, number: int, cvv: int, expary_date: datetime, money: float, type: CardType):
        self.name = name
        self.number = number
        self.cvv = cvv
        self.expary_date = expary_date
        self.money = money
        self.type = type


class AloqaBankCard(Card):
    pass


class NBUBankCard(Card):
    pass


class SQBBankCard(Card):
    pass


class Account:
    __cards: list[Card] = []

    def __init__(self, first_name: str, last_name: str, phone: str) -> None:
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.phone = phone
    
    def add_card(self, card: Card) -> None:
        self.__cards.append(card)

    def get_balans(self) -> float:
        s = 0
        for card in self.__cards:
            s += card.money
        return s

    def transfer_money(self, from_card: Card, to_card: Card, amount: float) -> bool:
        if from_card.money >= amount:
            from_card.money -= amount
            to_card.money += amount
            return True
        return False


types = [CardType("Humo"), CardType("Uzcard"), CardType("Visa")] 

account = Account("Ali", "Vali", "+998881234567")
c1 = AloqaBankCard('Oylik', 2345123451234123, 566, datetime(2029, 12, 12), 100, types[0])
c2 = SQBBankCard('Bussiness', 4132413241234, 435, datetime(2030, 12, 12), 50, types[2])

account.add_card(c1)
account.add_card(c2)

print("1. Aloqa Bank Kartasi: ", c1.money)
print("2. SQB Bank Kartasi: ", c2.money)
print(f"Jami Balans: {account.get_balans()}")

d = float(input("Qancha pul otkazmoqchisiz? "))

source_card_choice = int(input("Qaysi kartadan pul o'tkazmoqchisiz (1 - Aloqa, 2 - SQB): "))

if source_card_choice == 1 and c1.money >= d:
    target_card_choice = int(input("Pulni qaysi kartaga o'tkazmoqchisiz (1 - Aloqa, 2 - SQB): "))
    if target_card_choice == 1:
        print("Xatolik! O'zingizdan o'zingizga pul o'tkazolmasiz.")
    elif target_card_choice == 2:
        if account.transfer_money(c1, c2, d):
            print("otkazma muvaffaqiyatli amalga oshirildi")
        else:
            print("Balansda yetarli mablag' yo'q")
if source_card_choice == 1 and c1.money >= d:
    target_card_choice = int(input("Pulni qaysi kartaga o'tkazmoqchisiz (1 - Aloqa, 2 - SQB): "))
    if target_card_choice == 1:
        print("Xatolik! O'zingizdan o'zingizga pul o'tkazolmasiz.")
    elif target_card_choice == 2:
        if account.transfer_money(c1, c2, d):
            print("otkazma muvaffaqiyatli amalga oshirildi")
        else:
            print("Balansda yetarli mablag' yo'q")
else:
    print("Balansda yetarli mablag' yo'q")

print(f"Jami Balans: {account.get_balans()}")
print("1. Aloqa Bank Kartasi: ", c1.money)
print("2. SQB Bank Kartasi: ", c2.money)
