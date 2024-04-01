import random
import string as st


print("\n*** Password Generator v.1.0 ***\n")


class Data:
    def __init__(self, digits, upper, lower):
        self.digits = st.digits
        self.upper = st.ascii_uppercase
        self.lower = st.ascii_lowercase

    def create_password(self, length):
        while True:
            length = input("=> Enter the password length: ")
            if length.isdigit():
                length = int(length)
                for _ in range(length):
                    combination = self.digits + self.upper + self.lower
                    random_combination = random.choice(combination)
                    print(random_combination, end='')
                print("\n")
                break
            else:
                print("\nIncorrect password length. Please enter an whole number!\n")


data = Data(0, 0, 0)
data.create_password(12)
