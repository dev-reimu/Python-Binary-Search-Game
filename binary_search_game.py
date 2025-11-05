import random

def binary_search(array, n):
    low = array[0]
    high = len(array) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if array[mid] < n: low = mid + 1
        elif array[mid] > n: high = mid - 1
        else: return mid
    return -1

game_list = [ ]
game_list_length = random.randrange(8, 32, 4)
for i in range(game_list_length):
    n = random.randint(1, 256)
    while n in game_list:
        n = random.randint(1, 64)
    game_list.append(n)
game_list.sort()

choices = 8
find_number = random.choice(game_list)
find_number_position = binary_search(game_list, find_number)

print("A sorted list of " + str(game_list_length) + " elements has been generated.")
print("Use a \"Binary Search\" approach to find the position of number " + str(find_number) + ".")
print("You have " + str(choices) + " choices in total. Running out of choices means you lose the game.")
print("\nGood hunting, Stalker.")

def end_game(state: False):
    if state: print("You win!")
    else: print("You lose, as expected.")
    exit()

while choices > 0:
    print()
    choices -= 1
    user_picked_index = int(input("Pick a position: "))
    print()
    print("Number at position " + str(user_picked_index) + " is " + str(game_list[user_picked_index]) + ".")
    if user_picked_index is find_number_position:
        end_game(True)
    if choices > 1: print("You have " + str(choices) + " choices left.")
    elif choices == 1: print(" - C a r e f u l   n o w . . .")
    else: end_game(False)

