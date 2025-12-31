import data_fetcher
import movie_storage_sql as storage
import random

def main():

    while True:
        movies = storage.list_movies()
        print_menu()

        user_input = input("Enter choice (1-9 or '0' to quit): ").strip().lower()

        if user_input == "0":
            print("See you next time!")
            break

        if user_input == "1":
            command_list_movies()

        elif user_input == "2":
            command_add_movie(movies)

        elif user_input == "3":
            command_delete_movie(movies)

        elif user_input == "4":
            command_update_movie(movies)

        elif user_input == "5":
            print_stats(movies)

        elif user_input == "6":
            random_movie(movies)

        elif user_input == "7":
            search_movie(movies)

        elif user_input == "8":
            movies_sorted_by_rating(movies)

        elif user_input == "9":
            generate_website(movies)
        else:
            print("Please try it again.")

def print_menu():
    print("""
  ********** My Movies Database **********

Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update rating movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Generate Website
""")

def command_list_movies():
    movies_dict = storage.list_movies()
    print(f"\nNumber of total movies: {len(movies_dict)}\n")
    for title, data in movies_dict.items():
        print(f"{title}: {data['year']}, {data['rating']}")
    print()

def command_add_movie(movies_dict):
    new_movie = input("Enter movie name: ").strip()
    if new_movie in movies_dict:
        print(f"Movie '{new_movie}' already exists.")
    else:
        movie_data = data_fetcher.movie_fetcher(new_movie)
        if movie_data:
            storage.add_movie(movie_data)

def command_delete_movie(movies_dict):
    movie_name = input("Enter the movie name to be deleted: ").strip().lower()
    found = False

    for title in movies_dict:
        if title.lower() == movie_name:
            storage.delete_movie(title)
            #del movies_dict[title]
            print(f"Movie '{title}' deleted.")
            found = True
            break

    if not found:
        print(f"Can not find your Movie '{movie_name}' in Database.")

def command_update_movie(movies_dict):
    movie_name = input("Enter movie name to update: ").strip().lower()
    found = False

    for title in movies_dict:
        if title.lower() == movie_name:
            try:
                new_rating = float(input("Enter new rating (0-10): "))
                if 0 <= new_rating <= 10:
                    storage.update_movie(title, new_rating)
                    print(f"Rating for '{title}' updated to {new_rating}.")
                else:
                    print("Rating must be between 0 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            found = True
            break
    if not found:
        print(f"Movie '{movie_name}' not found.")


def print_stats(movies_dict):
    if not movies_dict:
        print("No movies to show statistics for.")
        return

    print("\n********** Movie Statistics **********")

    total_movies = 0
    total_rating = 0
    highest_rating = -1
    lowest_rating = 11
    highest_rated_movie = ""
    lowest_rated_movie = ""


    for movie in movies_dict:
        data = movies_dict[movie]
        if data["rating"] == "N/A":
            print("Attention: Movie '" + movie + "' without rating not included in the statistics.")
            continue
        total_movies += 1
        total_rating += data['rating']

        if data['rating'] > highest_rating:
            highest_rating = data['rating']
            highest_rated_movie = movie

        if data['rating'] < lowest_rating:
            lowest_rating = data['rating']
            lowest_rated_movie = movie

    if total_movies > 0:
        average_rating = total_rating / total_movies

        print(f"Total movies: {total_movies}")
        print(f"Average rating: {average_rating:.2f}")
        print(f"Highest rated: {highest_rated_movie} ({highest_rating})")
        print(f"Lowest rated: {lowest_rated_movie} ({lowest_rating})\n")
    else:
        print("No movies to show statistics for.")

def random_movie(movies_dict):
    if not movies_dict:
        print("No movies available.")
        return
    movie = random.choice(list(movies_dict.items()))
    print(f"\n Random Choice: {movie[0]} — Rating: {movie[1]['rating']}, Year: {movie[1]['year']}\n")

def search_movie(movies_dict):
    keyword = input("Enter search keyword: ").strip().lower()
    found = False
    for title, data in movies_dict.items():
        if keyword in title.lower():
            print(f"{title}: {data['rating']}, {data['year']}")
            found = True
    if not found:
        print(f"No movies found with keyword '{keyword}'.")


def movies_sorted_by_rating(movies_dict):
    if not movies_dict:
        print("No movies to sort.")
        return

    print("\n********** Movies Sorted by Rating **********")

    movie_list = list(movies_dict.items())

    for i in range(len(movie_list)):
        for j in range(i + 1, len(movie_list)):
            if movie_list[i][1]['rating'] < movie_list[j][1]['rating'] :
                movie_list[i], movie_list[j] = movie_list[j], movie_list[i]

    for title, data in movie_list:
        print(f"{title}: {data['rating']}, {data['year']}")
    print()

def generate_website(movies_dict):
    if not movies_dict:
        print("No movies available.")
        return
    with open("_static/index_template.html", "r") as fileindex_template:
        index_template = fileindex_template.read()
    movies_output = ""

    for title, data in movies_dict.items():
        movies_output += f"""
            <li> 
                <div class="movie"> <img class="movie-poster" src="{data["poster"]}" title="">
                <div class="movie-title">{title}</div>
                <span class="movie-year">{data["year"]}</span> </div>
            </li>
        """
    result = index_template.replace("__TEMPLATE_MOVIE_GRID__", movies_output)
    with open("_static/index.html", "w") as file:
        file.write(result)

if __name__ == "__main__":
    main()