import pgzrun
import random

HEIGHT = 600
WIDTH = 800

center_x = WIDTH // 2
center_y = HEIGHT // 2

final_level = 7
current_level = 1
start_speed = 10

game_over = False
game_complete = False

item_options= ["bag","car","headphones","phone","table"]

items = []

animations = []

def display_message(main_msg,sub_msg):
    screen.draw.text(main_msg,fontsize = 50,centre = (center_x,center_y),color = "orange")
    screen.draw.text(sub_msg,fontsize = 30,center = (center_x,center_y + 50),color = "orange")

def get_options_to_create(number_of_extra_items):
    items_to_create = ["cake"]
    for i in range(number_of_extra_items):
        random_item = random.choice(item_options)
        items_to_create.append(random_item)
    return items_to_create

def create_actors(items_to_create):
    actors = []
    for item in items_to_create:
        new_actor = Actor(item)
        actors.append(new_actor)
    return actors
    
def layout_actors(actors_to_position):
    number_of_gaps = len(actors_to_position) + 1
    gap_size = WIDTH // number_of_gaps
    random.shuffle(actors_to_position)
    for index,item in enumerate(actors_to_position):
        
        

def make_items(number_of_extra_items):
    items_to_create = get_options_to_create(number_of_extra_items)
    new_items = create_actors(items_to_create)
    layout_actors(new_items)

def update():
    global items 
    if len(items) == 0:
        items = make_items(current_level)

def draw():
    global items,current_level,game_complete,game_over
    screen.clear()
    screen.blit("background",(0,0))
    if game_over:
        display_message("GAME OVER","Try again")
    elif game_complete:
        display_message("YOU HAVE WON","Congradulations")
    else:
        for item in items:
            item.draw()
            



pgzrun.go()

