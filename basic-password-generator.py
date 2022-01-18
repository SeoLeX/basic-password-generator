import random
import string

print("Merhaba! SeoLeX'in şifre üreticine hoşgeldin.")

length = int(input("\nOluşturmak istediğin şifrenin karakter sayısını gir! \n"))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbol = string.punctuation

all = lower + upper + number + symbol

temp = random.sample(all,length)

password ="".join(temp)

print(password)