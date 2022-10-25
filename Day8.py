# def greet():
#     print("Welcome")
#     print("To This")
#     print("World")
# greet()

#function that allow for input
# def greet(name):
#     print(f"Welcome {name}")
#     print("To This")
#     print("World")
# greet("punit")

# def greet_with(name, location):
#     print(f"What is it like in {location} ?")
#     print(f"Hello {name}!")
#
# greet_with(name ="Punit", location="Delhi")


#Paint the wall
# import math
# test_h = int(input("Height of the wall:"))
# test_w = int(input("Width of the wall:"))
# Coverage = 5
#
# def paint_area(height, width, cover):
#     area = height * width
#     number_of_cans = math.ceil(area / cover)
#     print(f"You need {number_of_cans} no of cans")

# paint_area(height=test_h, width=test_w, cover = Coverage)

#Prime number
# number = int(input("Enter no to check"))
# def prime_checker():
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
# prime_checker()



#Caeser cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(starting_text, shift_amount, direction):
    our_text = ""

    for letter in starting_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift_amount
                # new_letter = alphabet[new_position]
                # our_text += new_letter
            elif direction == "decode":
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            our_text += new_letter
        else:
            our_text +=letter
    print(f"You {direction}d text is here:{our_text}")
#
#
#
should_continue = True
while should_continue:
    direction = input("Type 'encode' to Encrypt and 'decode' to Decrypt:\n")
    text = input("Enter your Messege here:\n").lower()
    shift = int(input("Type the Shift number:\n"))
    shift = shift % 26
    caeser(starting_text= text, shift_amount=shift, direction=direction)
    result = input("Type yes to continue and no to exit")
    if result == "no":
        should_continue = False



# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"Your Cipher Text is: {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text =""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"Your Cipher Text is: {plain_text}")

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(cipher_text=text, shift_amount=shift)
