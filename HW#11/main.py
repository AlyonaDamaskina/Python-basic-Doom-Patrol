from user_functions import *
import logging

logging.basicConfig(filename='user_app.log', level=logging.DEBUG)

while True:
    print("1. Adding New User\n"
          + "2. TAKE ALL\n"
          + "3. Searching\n"
          + "4. Update user's id\n"
          + "5. Exit"
          )
    try:
        menu_flag = int(input("Please enter a value: "))
    except ValueError:
        print("WRONG LETTERS VALUE")
        logging.warning('choosing the letters')
        continue
    if menu_flag == 1:
        logging.info("Adding New User")
        user_add()
    elif menu_flag == 2:
        logging.info("TAKE All!")
        try:
            get_all()
        except FileNotFoundError:
            logging.error('ERROR: File not found')
            create_file()
            get_all()
    elif menu_flag == 3:
        logging.info("the program is looking for...")
        what_to_search = input('enter right parameter for searching ')
        search_str = input('Searching ')
        try:
            search_by(search_str, what_to_search)
        except FileNotFoundError:
            logging.error('ERROR: File not found')
            create_file()
            search_by(search_str, what_to_search)

    elif menu_flag == 4:
        logging.info("PLEASE, update the value")
        try:
            update_user()
        except FileNotFoundError:
            logging.error('ERROR: File not found')
            create_file()
            update_user()
    elif menu_flag == 5:
        break