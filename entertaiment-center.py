#TODO prefect the code to follow googles style guide
import media
import fresh_tomatoes


'''
 This is an array of Movie objects its more effecient to store it in array rather
 than name individual instance varables for each movie.

'''
movie_list = [
media.Movie("The Punisher (1989)"," https://upload.wikimedia.org/wikipedia/en/c/c7/Punisher89poster.jpg","https://www.youtube.com/watch?v=umYvv7K4Z_I"),
media.Movie("Goodfellas", "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg", "https://www.youtube.com/watch?v=2ilzidi_J8Q"),
media.Movie("Hackers (1995)", "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg", "https://www.youtube.com/watch?v=Rn2cf_wJ4f4"),
media.Movie("Jaws", "https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg", "https://www.youtube.com/watch?v=U1fu_sA7XhE"),
media.Movie("The Godfather", "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg", "https://www.youtube.com/watch?v=sY1S34973zA"),
media.Movie("The Matrix", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", "https://www.youtube.com/watch?v=vKQi3bBA1y8")
]

# fresh toamatos takes the movie list and turns it into a web page.
fresh_tomatoes.open_movies_page(movie_list)
