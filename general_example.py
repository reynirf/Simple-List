from simple_lists import SimpleList

_list = SimpleList(True)   

data = _list.choose_one(
    'how old?', # question
    [18,19,20], # alteratives  
    'answer', # key to access answer - default: 'answer'
    True, # also get index of the answer? default: False
    'Go back' # go back button? default: Fasle
)
print(data)

print()
print()
print()
print()


pizzas = ["Classic", "Italian", "Vegan", "Pan"]  
print("Types of pizzas")
print("-"*30)
for pizza in pizzas:  
    print(pizza)

_list.single_list('Go back')

_list.clear_window()


# run some other code after 'go back'...