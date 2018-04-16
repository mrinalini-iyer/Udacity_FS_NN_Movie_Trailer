""" This file contains class definition for class Movie.
"""
import webbrowser


class Movie():
    """Summary of Movie class.

    Movie class encapsulates the following information about a movie:
    name, storyline, poster link, youtube URL.

    Attributes:
        title: A string containing movie name.
        storyline: A string explaining the movie story in a line.
        poster_image_url: A string containing URL of the movie poster online.
        trailer_youtube_url: A string containing youtube URL for the movie.
   """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ Inits Movie class with the arguments passed.
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens the movie youtube URL link in the web browser, using
            webbrowser python library function.

            Args: None

            Returns: None
        """
        webbrowser.open(self.trailer_youtube_url)

