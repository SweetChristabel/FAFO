def eat_breakfast(startervalue: int, name: str):
    import time
    cheese = startervalue
    print(f"{cheese} slices of cheese in {name}'s fridge.")
    print(f"{cheese} slices of cheese!")
    print("A new day dawns, time to eat breakfast.")
    cheese -= 1
    print(f"{cheese} slices of cheese in {name}'s fridge.")
    print("And so it goes.")
    time.sleep(0.5)
    if cheese > 0:
        eat_breakfast(cheese, name)
    else:
        print("Oh no! we're all out of cheese. Time to get some more!")
        buy_cheese(name)

def buy_cheese(name: int):
    cont = input("Do we buy more cheese? Y/N: ")
    if cont == "Y":
        print("How much cheese?")
        cheese = input_reasonable_number()
        eat_breakfast(cheese, name)
    elif cont == "N":
        return
    else:
        print("Bruh.")
        buy_cheese(name)


def input_reasonable_number():
    number = int(input("Type a number between 1 and 100: "))
    if number < 1 or number > 100:
            print("Bruh.")
            number = input_reasonable_number()
    return number
        

def main():
    slices = input_reasonable_number()
    name = input("Type your name: ")
    eat_breakfast(slices, name)
    print("Thank you for eating cheese and helping Simona practice recursive functions. Have a cheesy day.")

main()
