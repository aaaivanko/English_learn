import random
from constants import english_mn


def months_program():
    print(f"Welcome to the months program."
          f"\nHere I would like to check your knowledge of english months. ")
    active = True

    while active:
        random_number = random.randint(1, 12)
        random_eng_month = english_mn[random_number]
        user_answer = input(f"Please write name of number that is {random_number}: "
                            f"\n If you want to finish the program please press `q`: ")
        if user_answer != 'q':
            if random_eng_month.lower() != user_answer.lower():
                print(f"Sorry, your answer {user_answer} is wrong"
                      f"\n The correct answer is: {random_eng_month}. Please rty again.")
            else:
                print(f"Your answer {user_answer} is correct it's indeed {random_number} month")
        else:
            active = False
            return f"Thank you for the game. Goodbuy!"


print(months_program())



