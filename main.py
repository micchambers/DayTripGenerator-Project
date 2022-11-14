import random
print('')
print('')


destination_list = ['ATL', "LA", "NYC",]
transportation_list = ["driving", "taking the train", "biking"]
entertainment_list = ["read Hunter x Hunter (peak)", "go to the opera", "watch a Kung Fu movie"]
restaurant_list = ['BGR Grille', "Willy's Mexicana Grill", "Slim & Husky's Pizza Beeria"]


def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def run_trip_generator(list_1, list_2, list_3, list_4):
    chosen_dest = random_item_picker(list_1)
    chosen_trans = random_item_picker(list_2)
    chosen_ent = random_item_picker(list_2)
    chosen_rest = random_item_picker(list_3)
    print(f"On today's trip, you'll be going to {chosen_dest} by {chosen_trans}, stopping to {chosen_ent} and to eat at {chosen_rest}")
    


run_trip_generator(destination_list, transportation_list, entertainment_list, restaurant_list)



print('')
print('')