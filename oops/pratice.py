class Account:
    def __init__(self, acc, holder_name, balance):
        self.acc_no = acc
        self.holder_name = holder_name
        self.balance = balance

    def debit(self, amount):
        if amount > self.balance:
            print(f"❌ Insufficient balance! Available balance: ₹{self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"✅ ₹{amount:.2f} debited. New balance: ₹{self.balance:.2f}")

    def credit(self, amount):
        self.balance += amount
        print(f"✅ ₹{amount:.2f} credited. New balance: ₹{self.balance:.2f}")

    def display_balance(self):
        print(f"📄 Account Number: {self.acc_no}")
        print(f"👤 Account Holder: {self.holder_name}")
        print(f"💰 Current Balance: ₹{self.balance:.2f}")


def main():
    print("="*40)
    print("🏦 Welcome to the Bank Account Management System")
    print("="*40)

    acc = input("Enter your Account Number: ")
    holder_name = input("Enter Account Holder's Name: ")

    while True:
        try:
            balance = float(input("Enter your Initial Balance (₹): "))
            break
        except ValueError:
            print("⚠️ Please enter a valid number for balance.")

    acc1 = Account(acc, holder_name, balance)
    print("\n✅ Account created successfully!\n")

    # Menu-driven operations
    while True:
        print("\n-------- MENU --------")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        print("----------------------")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: ₹"))
                acc1.credit(amt)
            except ValueError:
                print("⚠️ Invalid amount.")
        
        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: ₹"))
                acc1.debit(amt)
            except ValueError:
                print("⚠️ Invalid amount.")
        
        elif choice == "3":
            acc1.display_balance()

        elif choice == "4":
            print("\n👋 Thank you for banking with us. Goodbye!")
            break

        else:
            print("⚠️ Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
