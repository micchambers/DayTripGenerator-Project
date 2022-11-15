import random
print('')
print('')

# satisfied = False

destination_list = ['ATL', "LA", "NYC",]
transportation_list = ["driving", "taking the train", "biking"]
entertainment_list = ["read Hunter x Hunter (peak)", "go to the opera", "watch a Kung Fu movie"]
restaurant_list = ['BGR Grille', "Willy's Mexicana Grill", "Slim & Husky's Pizza Beeria"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item


def repick_item(list):
    satisfied = False
    while satisfied == False:
        chosen_item = random_item_picker(list)
        answer = input(f"Are you satisfied with '{chosen_item}'? Y or N? ")
        if answer == "Y":
            satisfied = True
    return(chosen_item)


def run_trip_generator(list_1, list_2, list_3, list_4):
    chosen_dest = repick_item(list_1)
    chosen_trans = repick_item(list_2)
    chosen_ent = repick_item(list_3)
    chosen_rest = repick_item(list_4)
    print(f"On your trip, you will be going to {chosen_dest}, travelling by {chosen_trans}, stopping to {chosen_ent} and having dinner at {chosen_rest}.")
    

        
        

    # chosen_dest = random_item_picker(list_1)
    # print(f"Your chosen destination is {chosen_dest}")
    # chosen_trans = random_item_picker(list_2)
    # print(f"Your chosen transportation is {chosen_trans}")
    # chosen_ent = random_item_picker(list_3)
    # print(f"Your chosen entertainment is {chosen_ent}")
    # chosen_rest = random_item_picker(list_4)
    # print(f"Your chosen restaurant is {chosen_rest}")
    

run_trip_generator(destination_list, transportation_list, entertainment_list, restaurant_list)





print('')