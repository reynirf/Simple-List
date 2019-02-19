import SimpleList

def main():
    _list = SimpleList(True) # if true, window will be cleared on init   
    data = _list.choose_one(
        'Choose an acion', # question
        ['Register user', 'Edit user', 'Find user'], # alteratives  
        'answer', # key to access answer - default: 'answer'
        True, # also get index of the answer? default: False
        'Logout' # go back button? default: Fasle
    )
    user_options(data, main)

def user_options(data, came_from):
    if data['answer'] == 'Register user':
        _list = SimpleList(True)
        data = _list.choose_one(
            'Choose an acion', # question
            ['alternative 1', 'alternative 2', 'alternative 3'],  
            'answer',
            False, 
            'Go back' 
        )
        
        if data['answer'] == 'Go back':
            return came_from()

        _list.delete_last_lines(7)

        print(_list.color.return_colored("ENTER USER & PASS: ", "blue"))
        print()
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # ... more code ...

        # push to database or store in file

        
    elif data['answer'] == 'Edit user':
        _list = SimpleList(True)
        data = _list.choose_one(
            'Choose an acion', # question
            ['alternative 1', 'alternative 2', 'alternative 3'],  
            'answer',
            False, 
            'Go back' 
        )

        # ... code ...


    elif data['answer'] == 'Find user':
        _list = SimpleList(True)
        data = _list.choose_one(
            'Choose an acion', # question
            ['alternative 1', 'alternative 2', 'alternative 3'],  
            'answer',
            False, 
            'Go back' 
        )

        # ... code ...

main()