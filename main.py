import random
print('')
print('')

satisfied = False

destination_list = ['ATL', "LA", "NYC",]
transportation_list = ["driving", "taking the train", "biking"]
entertainment_list = ["read Hunter x Hunter (peak)", "go to the opera", "watch a Kung Fu movie"]
restaurant_list = ['BGR Grille', "Willy's Mexicana Grill", "Slim & Husky's Pizza Beeria"]

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def run_trip_generator(list_1, list_2, list_3, list_4):
    chosen_dest = random_item_picker(list_1)
    print(f"Your chosen destination is {chosen_dest}")
    chosen_trans = random_item_picker(list_2)
    print(f"Your chosen transportation is {chosen_trans}")
    chosen_ent = random_item_picker(list_3)
    print(f"Your chosen entertainment is {chosen_ent}")
    chosen_rest = random_item_picker(list_4)
    print(f"Your chosen restaurant is {chosen_rest}")

# run_trip_generator(destination_list, transportation_list, entertainment_list, restaurant_list)

while satisfied == False:
    run_trip_generator(destination_list, transportation_list, entertainment_list, restaurant_list)
    print('')
    x = input("Are you satisifed with your trip? Y or N ")
    if x == "Y":
        break



print('')
print('')