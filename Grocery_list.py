walker = 0
<<<<<<< HEAD
best_so_far_name = None
best_so_far_cost = None
heaviest_so_far_weight = None
heaviest_so_far_name = None
new_entry_name = None
program_on = True

=======
best_so_far_name = 0
best_so_far_cost = 0
heaviest_so_far_weight = 0
heaviest_so_far_name = 0
decide = input("What do you want to do with the list.\nsearch/highest price/heaviest/display items/: ")
>>>>>>> aebc96a3a22a222cdb01e1022b4d172f583cc77f
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
#new system
item_1 = [2.5, 1]
item_2 = [1, 1]
item_3 = [5, .5]
item_4 = [4, .5]
item_5 = [10, 20]
item_6 = [30, 3]
item_7 = [2, 0.5]
item_8 = [60, 0.5]
item_9 = [5, 1]
item_10 = [1285.35, 1]
item_11 = [0,0]
#grocery list names and stat lists
grocery_list = ['apple', 'bannana', 'salt', 'pepper', 'watermelon',
    'wine', 'snickers', 'cavliar', 'sunscreen','gold']
grocery_stats = [apple, bannana, salt, pepper, watermelon,
    wine, snickers, cavliar, sunscreen, gold]
grocery_items = [item_1, item_2, item_3, item_4, item_5,
	item_6,item_7,item_8,item_9,item_10,item_11]
grocery_dict = {'apple': item_1, 'bannana': item_2, 'salt': item_3, 'pepper': item_4, 'watermelon': item_5,
    'wine': item_6,'snickers': item_7, 'cavliar': item_8, 'sunscreen': item_9, 'gold': item_10,
	new_entry_name: item_11
}
#starting program based on user's decision
while program_on:
	grocery_items = [item_1, item_2, item_3, item_4, item_5,
		item_6, item_7, item_8, item_9, item_10, item_11]
	decide = input("What do you want to do with the list.\nChoices: search/highest price/heaviest\ndisplay items/search stats/new entry: ")
	if decide == 'search stats':
		search_stat = input("What item do you want to get info on?: ")
		print('-------------------')
		print(search_stat)
		print('weight: '+str(grocery_dict[search_stat][0])+' lbs')
		print('Cost: $'+str(grocery_dict[search_stat][1]))
		print('-------------------')
	elif decide == 'search':
		walker = 0
		search = input("What do you want to check for on your list?: ")
		for i in range(len(grocery_list)):
			if grocery_list[walker] == search:
				print("You have that item on your list.")
				break
			else: walker = walker + 1
			if walker == len(grocery_list):
				print("That item is not on your list")
	elif decide == 'highest price':
		walker = 0
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
	    	#if grocery_dict[walker][1] > heaviest_so_far_weight:
	        if grocery_stats[walker][1] > heaviest_so_far_weight:
	            heaviest_so_far_weight = grocery_stats[walker][1]
	            heaviest_so_far_name = grocery_list[walker]
	        walker = walker + 1
	        if walker == len(grocery_list):
	            print(heaviest_so_far_name+" is the heaviest item.")
	            break
	    walker = 0
	elif decide == 'display items':
	    print('-------------------')
	    for i in range(len(grocery_list)):
	        if grocery_stats[walker][0] > 0 and grocery_stats[walker][1] > 0:
	        	print(grocery_list[walker]+'\nCost: $'+str(grocery_stats[walker][0])
	            	+'\nWeight: '+str(grocery_stats[walker][1])+' lbs'+'\n-------------------')
	        walker += 1
	    walker = 0
	elif decide == 'new entry':
		new_entry_name = input("What do you want to add?: ")
		item_11[0] = input("How much does it cost: ")
		item_11[1] = input("How much does it weight?: ")
		print("Added item to list")
	else:
	    print("Invalid input")
