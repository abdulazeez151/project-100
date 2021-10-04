class Atm():
    def __init__(self, CardNumber, Pin):
        self.CardNumber = CardNumber
        self.Pin = Pin

    def BalanceInquiry(self):
        print("Your Balance Is : $ 200")

    def CashWithDrawl(self, amount):
        new_amount = 200-amount
        print("You WithDrawed : " + str(amount) + ". Your Remaining Balance Is : " + str(new_amount))

def main():
    name = input("Hello! What is your name?")
    print("Hello, " + name)
    cardNumber = input("Insert Your CardNumber : ")
    pin = input("Enter Your Pin : ")
    new_user = Atm(cardNumber, pin)

    print("Choose Your Activity")
    print("1. Balance Inquiry")
    print("2.Cash WithDrawl")
    activity = int(input("Enter Activity Choice: "))

    if (activity == 1):
        new_user.BalanceInquiry()
    elif (activity == 2):
        amount = int(input("Enter the Amount : "))
        new_user.CashWithDrawl(amount)
    else:
        print("Enter A Valid Number")

if __name__ == "__main__":
    main()