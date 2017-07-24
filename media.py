import webbrowser

class Movie:
    #documention
    """
    This Object will store the title, box art, and movie trailer upon creation.

    If you uses the show_trailer function it will lanuch trailer in a web page.
    """
    #constructor
    def __init__(self,movie_title,movie_box_art, movie_trailer):
        self.title=movie_title
        self.box_art=movie_box_art
        self.trailer=movie_trailer

    #show_trailer
    def show_trailer(self):
        webbrowser.open_new(self.trailer)
#end of movie class
