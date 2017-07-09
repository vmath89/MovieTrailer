class Movie:
    """
    This class containes the attibutes which will be used to display the movies with the trailer.
    """

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
        """
        :param movie_title: The title of the movie.
        :param movie_storyline: The story of the movie.
        :param poster_image: The poster image url of the movie.
        :param trailer_youtube:The youtube trailer url of the movie.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
