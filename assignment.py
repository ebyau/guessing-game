import random


def play_mind_game():
    first_list = list(range(10))
    random.shuffle(first_list)
    digits = (first_list[:3])
    print(digits)
    lives = 5

    while True:
        entry = input("hello there! please any 3 digit number")
        present = []
        c = 0
        lives -= 1
        print(f"{lives} chances left")
        if lives == 0:
            print(f"thanks for trying")
            break
        else:
            continue

        if len(entry) != 3:
            print("Only 3 digit numbers allowed")
            continue

        try:
            int(entry) / 3
            entries = list(entry)
            for x in entries:
                if int(x) in digits:
                    print(f"{x} is a close")
                    present.append(int(x))
                else:
                    pass

            if len(present) == 0:
                print("Nope")
                continue
            else:
                for i in present:
                    index_entries = entries.index(str(i))
                    index_digits = digits.index(i)
                    if index_digits == index_entries:
                        print(f"{i} is a match ")
                        c += 1
                    else:
                        print(f"but {i} is in the wrong position")
                        continue

            if c == 3:
                print(f"{entry} is the correct number")
                again = input("Do you want to play again")
                if again == "yes":
                    play_mind_game()
                else:
                    print("Thanks bye see ya!")
                    break
            else:
                continue
        except ValueError:
            print("Only 3 digit numbers are allowed")
            continue


play_mind_game()
