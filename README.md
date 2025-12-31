# Movie-Project
This Movies Database is a console-based Python application for managing a personal movie collection.
Users can add, delete, update, search, and analyze movies, as well as generate a simple static website from the stored data.
---
Features:
- List all movies
- Add movies automatically (fetches year, rating, poster, etc.)
- Delete movies
- Update movie ratings
- View movie statistics
- Get a random movie recommendation
- Search movies by title
- Sort movies by rating
- Generate a static HTML website
---
Requirements:
- Python 3.8+
- ---
The following Python modules:
- random (standard library)
- data_fetcher (custom module)
- movie_storage_sql (custom module)
---
Installation & Usage:
- Clone or download the project files
- Make sure all required modules are available

Start the application:
- python main.py
---
Menu Overview:

After starting the program, the following menu is displayed:

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

Enter the number corresponding to the desired action.

---
Functionality Details:

List Movies
- Displays all movies in the database along with their release year and rating.
---
Add Movie
- Enter the movie title
- Movie details are fetched using data_fetcher.movie_fetcher()
- The movie is stored in the database
---
Delete Movie
- Removes a movie by title (case-insensitive)
---
Update Movie Rating
- Enter a new rating between 0 and 10
- Invalid input is handled gracefully
---
Statistics

Displays:
- Total number of rated movies
- Average rating
- Highest-rated movie
- Lowest-rated movie
- Movies without a rating ("N/A") are excluded from the statistics.
---
Random Movie
- Randomly selects and displays a movie from the database.
---
Search Movie
- Search movies by a keyword in the title
- Displays all matching movies
---
Movies Sorted by Rating
- Sorts movies in descending order by rating
- Uses a custom sorting algorithm
---
Generate Website
- Creates a static HTML website using a template
- The file _static/index_template.html is used
- Output is saved as _static/index.html
---
Generated Website

The generated website includes:
- Movie poster images
- Movie titles
- Release years

The resulting index.html can be opened directly in a web browser.

---

Notes

- Movies without ratings are ignored in statistical calculations
- All database logic is handled in movie_storage_sql

This project is intended for educational purposes

---
API Key Configuration

This project uses an external movie API (e.g. OMDb API) to automatically fetch movie data such as:
- Release year
- Rating
- Poster image

To use this feature, an API key is required.

---
How to Get an API Key

- Visit the website of the movie API provider (for example, OMDb API)
- Create an account if required
- Generate a personal API key
---

Author

Created as a Python learning project.
Feel free to modify, extend, and improve it

---
