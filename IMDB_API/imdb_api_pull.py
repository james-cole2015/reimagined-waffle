import random
import imdb

ia = imdb.IMDb()

def choose_show():
    welcome_msg = 'What show are you interested in? '
    usr_choice = input(welcome_msg)
    global results, usr_input
    results = ia.search_movie(usr_choice)
    usr_input = usr_choice

def get_show_id():
    for show in results:
        if show['kind'] == 'tv series':
            tv_show_ID = show.movieID
            break
    print(f'{show} - {tv_show_ID}')
    global show_name,usr_show
    show_name = ia.get_movie(tv_show_ID)
    usr_show = usr_input

def get_random_episode():
    ia.update(show_name,'episodes')
    episode_list = []
    season_count = show_name['number of seasons']
    num_of_seasons = season_count
    while season_count != 0:
        episode = show_name['episodes'][season_count].values()
        episode_list.append(episode)
        season_count -= 1
    episode_count = len(episode_list)

    ep_list = []


    episode_count -= 1
    while episode_count != -1:
        for episode in episode_list[episode_count]:
            ep_list.append(episode)
        episode_count -= 1

    return ep_list, num_of_seasons

def print_results():
    episode_list, num_of_seasons = get_random_episode()
    ep_num = len(episode_list)
    msg1 = f'There are {ep_num} episodes in the TV series {usr_show}'
    msg2 = f'There are {num_of_seasons} seasons in {usr_show}'
    random_ep = random.choice(episode_list)
    msg3 = f'Here is your random {usr_show.title()} episode: {random_ep}'
    print(msg1)
    print(msg2)
    print(msg3)


    
def get_cast():
    cast = show_name['cast']
    for actor in cast[:10]:
        print(actor)

def get_plot_outline():
    plot = show_name['plot outline']
    print(plot)

def main_func():
    choose_show()
    get_show_id()
    print('Choose an option: ')
    print("Type 'q' or 'quit' to exit")
    usr_choice = input('a) Get a random episode\nb) Get Cast Information ' \
    '\nc) Get Plot outline\n')
    if usr_choice == 'a':
        get_random_episode()
        print_results()
    if usr_choice == 'b':
        get_cast()
    if usr_choice == 'c':
        get_plot_outline()


main_func()