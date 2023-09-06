def main():
    session = create_database()

    while True:
        choice = main_menu()

        if choice == 'V':
            view_records(session)
        elif choice == 'A':
            name = input("Enter the product name: ")
            try:
                price = float(input("Enter the product price: "))
                quantity = int(input("Enter the product quantity: "))
                add_item(session, name, price, quantity)
            except ValueError:
                print("Invalid input. Please enter a valid price and quantity.")
        elif choice == 'B':
            export_to_csv(session)
        elif choice == 'Q':
            break
        else:
            print("Oh no, invalid choice ! Please try again")

if __name__ == '__main__':
    main()
