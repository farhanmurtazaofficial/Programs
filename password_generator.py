import random
import string
class Password_Generator:
    uppercase_letter = random.choice(string.ascii_uppercase)
    lowercase_letter = random.choice(string.ascii_lowercase)
    digits = random.randint(1,9)
    special_character = random.choice(string.punctuation)
    def __init__(self,length):
        self.total_length = length
    def generate_passwrod(self):
        all_char = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
        remaing_chars = self.total_length -4 
        remaining_charcter = "".join(random.choice(all_char) for _ in range(remaing_chars))
        pasword_list = list(self.uppercase_letter + self.lowercase_letter + str(self.digits) + self.special_character + remaining_charcter)
        random.shuffle(pasword_list)
        strong_password = "".join(pasword_list)
        return strong_password

while True:
        user_condition = input("doyou want to add the length of the password y/n:")
        is_yes=user_condition.lower().strip()=="y"
        is_no = user_condition.lower().strip()=="n"
        if is_yes:
            myobj = Password_Generator(int(input("Please enter the length of the password,But default is 4.")))
            result = myobj.generate_passwrod()
            print(result)
        elif is_no:
            print("Good Bye")
            break
        else:
            print("please enter the write option y/n")
            continue