walker = 0
best_so_far_name = 0
best_so_far_cost = 0
heaviest_so_far_weight = 0
heaviest_so_far_name = 0
#Danke meme test incoming

decide = input("What do you want to do with the list.\nsearch/highest price/heaviest/display items/: ")
#Grocery list stats [cost, weight(lbs)]
apple = [2.5, 1]
bannana = [1, 1]
salt = [5, .5]
pepper = [4, .5]
watermelon = [10, 20]
wine = [30, 3]
snickers = [2, 0.5]
cavliar = [60, 0.5]
sunscreen = [5, 1]
gold = [1285.35, 1]
#grocery list names and stat lists
grocery_list = ['apple', 'bannana', 'salt', 'pepper', 'watermelon',
    'wine', 'snickers', 'cavliar', 'sunscreen','gold']
grocery_stats = [apple, bannana, salt, pepper, watermelon,
    wine, snickers, cavliar, sunscreen, gold]
#starting program based on user's decision
if decide == 'search':
    search = input("What do you want to check for on your list?: ")
    for i in range(len(grocery_list)):
        if grocery_list[walker] == search:
            print("You have that item on your list.")
            break
        else: walker = walker + 1
        if walker == len(grocery_list):
            print("That item is not on your list")
elif decide == 'highest price':
    for i in range(len(grocery_list)):
        if grocery_stats[walker][0] > best_so_far_cost:
            best_so_far_cost = grocery_stats[walker][0]
            best_so_far_name = grocery_list[walker]
        walker += 1
        if walker == len(grocery_list):

            print(best_so_far_name+" is the most expensive item.")
            break
elif decide == 'heaviest':
    for i in range(len(grocery_list)):
        if grocery_stats[walker][1] > heaviest_so_far_weight:
            heaviest_so_far_weight = grocery_stats[walker][1]
            heaviest_so_far_name = grocery_list[walker]
        walker = walker + 1
        if walker == len(grocery_list):
            print(heaviest_so_far_name+" is the heaviest item.")
            break
elif decide == 'display items':
    print('-------------------')
    for i in range(len(grocery_list)):
        print(grocery_list[walker]+'\nCost: $'+str(grocery_stats[walker][0])
            +'\nWeight: '+str(grocery_stats[walker][1])+' lbs'+'\n-------------------')
        walker += 1
else:
    print("Invalid input")
