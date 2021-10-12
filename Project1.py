print('Random Food Generator Project version 1')

#Putting my lists here
Menu_Types = ["Pizza", "Chinese", "Spanish", "Fast Food","Sushi"]
Pizza_List = ["Check E Cheese", "Dominos", "Pizza Hut", "Two Italian Guys"]
Chinese_List = ["Five Star", "Great Wall", "Great Asian Wok", "Dragon Chinese"]
Spanish_List = ["Mi Casa", "La Isla", "La Cuevna Restaurant"]
Fast_Food_List = ["McDonalds", "Taco Bell", "Wendys", "Burger King", "Panera", "Popeyes"] 
Sushi_List = ["Mirakuya", "Hana Sushi and Haibachi", "Five Star"]

print('''
                    Menu
---------------------------------------
''')

print(', '.join(Menu_Types))
decision = input("What kind of food do you want? ")
print(decision+'?')

if decision in ['Pizza', 'pizza']:
    print("Here are your pizza options:",','.join(Pizza_List))
if decision in ['Chinese', 'chinese']:
    print("Here are your Chinese food options:",','.join(Chinese_List))
if decision in ['Spanish', 'spanish']:
    print("Here are your Spanish food options:",','.join(Spanish_List))
if decision in ['Fast Food', 'fast food']:
    print("Here are your fast food options:",','.join(Fast_Food_List))
if decision in ['Sushi', 'sushi']:
    print("Here are your sushi options:",','.join(Sushi_List))
else:
    exit()
