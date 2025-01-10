name = input("Name please: ")
print(f"{name} Welcome to the Tic Tac Toe game")
play_or_not = input("Do you want play the game?, y or n ")
if play_or_not == 'n':
    print('Ok, have a nice day')
else:

    tic = [" | | "
        "_ _ _ "
        " | | "
        "_ _ _ "
        " | | "]
    print(tic)