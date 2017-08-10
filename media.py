import webbrowser


class Movie():
    """The Movie class has the attributes as follows:
        movie_title, movie_storyline,
        poster_image, trailer_youtube
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Constructor called and value of the variables are assigned to Instance variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """The webbrowser module includes functions to open URLs in a browser applications."""
        webbrowser.open(self.trailerurl)

