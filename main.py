from classes import Jar


def main():
    first_menu = \
        """
        ************************
        [1] Set jar capacity
        [2] Add Cookies*
        [3] Exit

        *Default capacity = 12
        ***********************\n
        """

    second_menu = \
        """
        ************************
        [1] Add Cookies
        [2] Remove Cookies
        [3] Check Jar
        [4] Exit
        ***********************\n
        """

    print(first_menu)
    while True:
        try:
            choice = input("Choice: ")          
            if choice == "1":
                jar = Jar(get_cap())
                print(f"Jar capacity set to {jar.capacity}\n")
                break
            elif choice == "2":
                jar = Jar()
                print(f"Jar capacity set to {jar.capacity}\n")
                jar.deposit(add_c())
                break
            elif choice == "3":
                print("Goodbye!")
                return
            else:
                print("Invalid Choice")
        except ValueError as e:
            print(e)
            print(jar)

    while True:
        try:
            print(second_menu)
            choice = input("Choice: ")
            if choice == "1":
                jar.deposit(add_c())
            elif choice == "2":
                jar.withdraw(take_c())
            elif choice == "3":
                print(f"You have {jar.cookies} cookies.")
            elif choice == "4":
                print("Goodbye!")
                return
            else:
                print("Invalid Choice")
        except ValueError as e:
            print(e)
            print(jar)




def get_cap():
    return int(input("What capacity is your jar: "))

def add_c():
    return int(input("How many cookies you want to add: "))

def take_c():
    return int(input("How many cookies you want to take: "))


if __name__ == "__main__":
    main()