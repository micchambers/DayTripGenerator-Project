import random

import main

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item

def run_trip_generator(list_1, list_2, list_3, list_4):
    chosen_dest = random_item_picker(list_1)
    chosen_trans = random_item_picker(list_2)
    chosen_ent = random_item_picker(list_2)
    chosen_rest = random_item_picker(list_3)
    return("On today's trip, you'll be going to {} by {}, stopping to {} and to eat at {}")
    

