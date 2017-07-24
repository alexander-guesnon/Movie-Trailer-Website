#TODO edit fresh_tomatoes css and html to be more personal
#TODO prefect the code to follow googles style guide

#take in class movie and fresh_tomatoes
import media
import fresh_tomatoes

# shove all 6 of thos movies into a array
movie_list = [
media.Movie("The Punisher (1989)"," https://upload.wikimedia.org/wikipedia/en/c/c7/Punisher89poster.jpg","https://www.youtube.com/watch?v=umYvv7K4Z_I"),
media.Movie("Goodfellas", "https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg", "https://www.youtube.com/watch?v=2ilzidi_J8Q"),
media.Movie("Hackers (1995)", "https://upload.wikimedia.org/wikipedia/en/6/67/Hackersposter.jpg", "https://www.youtube.com/watch?v=Rn2cf_wJ4f4"),
media.Movie("Jaws", "https://upload.wikimedia.org/wikipedia/en/e/eb/JAWS_Movie_poster.jpg", "https://www.youtube.com/watch?v=U1fu_sA7XhE"),
media.Movie("The Godfather", "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg", "https://www.youtube.com/watch?v=sY1S34973zA"),
media.Movie("The Matrix", "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", "https://www.youtube.com/watch?v=vKQi3bBA1y8")
]

# make 6 of my favorit movies acording to the constructor

#Punisher

#goodfellas
'''

'''
#Hackers
'''

'''
#Jaws
'''

'''
#The Godfather
'''

'''
#The Matrix
'''

'''

#send that array to the fresh_tomatoes.py through open_movies_page()
# fresh toamatos takes the movie list and turns it into a web page.
fresh_tomatoes.open_movies_page(movie_list)
