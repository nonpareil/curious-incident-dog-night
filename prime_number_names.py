import string


def get_letter_number(letter):
    alpha_dict = dict(zip(string.ascii_letters, [ord(i) % 32 for i in string.ascii_letters]))
    return alpha_dict[letter]


def check_name():
    while True:
        user_name = input(
            "Enter your first and last name to see if it is a prime number. Enter 'quit' when you are finished: ")
        if user_name == "quit":
            break
        name_letters = list(user_name.replace(' ', ''))
        name_total = 0
        for n in name_letters:
            letter_num = get_letter_number(n)
            name_total += letter_num

        if name_total > 1:
            for i in range(2, name_total):
                if (name_total % i) == 0:
                    print("Your name is {} letters long, it is not a prime number.").format(name_total)
                    break
            else:
                print("Your name is {} letters long, it is a prime number.").format(name_total)
        else:
            print("Your name is not a prime number.")


check_name()
