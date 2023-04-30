import csv

def generate_list_games(filename):

    main_list = []

    file_in = open(filename, encoding='UTF-8', errors='replace')

    file_in.readline()
    file_in = csv.reader(file_in)

    for line in file_in:
        if ";" in line[5]:
            line[5] = line[5].split(";")
        else:
            line[5] = [line[5]]
        if ";" in line[6]:
            line[6] = line[6].split(";")
        else:
            line[6] = [line[6]]
        if ";" in line[7]:
            line[7] = line[7].split(";")
        else:
            line[7] = [line[7]]
        if ";" in line[8]:
            line[8] = line[8].split(";")
        else:
            line[8] = [line[8]]
        if ";" in line[10]:
            line[10] = line[10].replace(";",",")
        
        
        
        main_list.append(line)

    return main_list


def print_menu(menu_list):

    print("\n"*5)
    for i in range(0, len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')


def get_menu_selection(menu_list):

    possible_choice_values = []
    for i in range(0, len(menu_list)):
        possible_choice_values.append(str(i+1))

    choice = input("Type number to choose ... ")

    while choice not in possible_choice_values:
        print("Incorrect selection")
        print("\n"*30)
        
        print_menu(menu_list)
        choice = input("Type number to choose ...")

    return int(choice)


def get_all_possible_genres(list_of_games):

    genres = []
    
    for game in list_of_games:
        for genre in game[6]:
            if genre not in genres:
                genres.append(genre)

    genres.sort()
    return genres


def print_genres(list_genres):

    print("\n\nAll genres available are:")
    print("-"*20)

    for item in list_genres:
        print(f'{item:<30}')
    
    print("\n") 


def get_valid_genre(list_genres):

    genre = input("What genre would you like to filter for?")
    while genre not in list_genres:
        genre = input("Sorry that genre name is not valid. Please try again")
    
    return genre


def filter_all_listings(list_of_games, genre):

    sub_list = []

    for item in list_of_games:
        if genre in item[6]:
            sub_list.append(item)

    return sub_list



def get_valid_listing(list_games):

    possible_choice_values = []
    for i in range(0, len(list_games)):
        possible_choice_values.append(str(i+1))
    
    choice = input("Which listing would you like to choose?")

    while choice not in (possible_choice_values):
        choice = input("Invalid choice. Try another number")

    choice = int(choice) - 1

    return list_games[choice]



def print_listings_table(list_games):

    for i in range(0, len(list_games)):
        game = list_games[i]
        s = f"{i+1:<3} {game[0]:<30}"
        print(s)


def print_game_details(some_game):

    s = "\n"
    s += some_game[0]+"\n"+f"Released on: {some_game[1]}\n"
    s+= f"With a metacritic score of {some_game[2]}\n"
    s+= f"Rated {some_game[3]}\n"
    s+=f"With an average of {some_game[4]} hours of playtime.\n\n"
    if len(some_game[5])>=1:
        s+= 'Playable on:\n'
        for platform in some_game[5]:
            s+= platform+"\n"
        
    
        
    print(s)


def main():
    main_game_list = generate_list_games(r"C:\Users\Administrator\Downloads\Archive\video_game_data.csv")
    
    all_genres = get_all_possible_genres(main_game_list)

    menu_items = ['See All Listings', 'Find game by genre', 'TBD', 'TBD', 'TBD', 'Exit']
    
    print_menu(menu_items)
    choice = get_menu_selection(menu_items)
    
    while 0 < choice and choice < len(menu_items):

        ##See all listings
        if choice == 1:
            print_listings_table(main_game_list)

        #Find listing by Genre
        elif choice == 2:
            print_genres(all_genres)
            genre = get_valid_genre(all_genres)

            sub_list_genres = filter_all_listings(main_game_list, genre)
            print_listings_table(sub_list_genres)

            current_game = get_valid_listing(sub_list_genres)
            
            print_game_details(current_game)
            
        elif choice == 3:
            pass

        elif choice == 4:
            pass

        elif choice == 5:
            pass
            

        print_menu(menu_items)
        choice = get_menu_selection(menu_items)
        

    print("\n\nGood bye!")
    
#Name,Release Date,Metacritic Score,ESRB Rating,Playtime,Platforms,Genres,Stores,Developers,Background Image,Description




main()

