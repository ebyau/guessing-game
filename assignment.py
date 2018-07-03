import random


def correct_number_wrong_position():
    first_list = list(range(10))
    random.shuffle(first_list)
    digits = (first_list[:3])
    print(digits)

    while True:
        entry = input("Please enter a 3 digit number")
        present = []
        c = 0

        if len(entry) != 3:
            print("Please enter a 3 digit number")
            continue

        try:
            int(entry)/2
            entries = list(entry)
            for x in entries:
                if int(x) in digits:
                    print(f"{x} is present")
                    present.append(int(x))
                else:
                    pass


            if len(present) == 0:
                print("Nope")
                continue
            else:
                for i in present:
                    index_entries = entries.index(i)
                    index_digits = digits.index(i)
                    if index_digits == index_entries:
                        print(f"{i} is in the right position")
                        c += 1
                    else:
                        print(f"{i} is in the wrong position")

            if c == 3:
                print(f"{entry} is the correct number")
                again = input("Do you want to play again")
                if again == "yes":
                    correct_number_wrong_position()
                else:
                    print("Thanks bye")
                    break
            else:
                continue
        except ValueError:
            print("Please enter a 3 digit number")
            continue





correct_number_wrong_position()
