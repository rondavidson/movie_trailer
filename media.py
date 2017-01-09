import webbrowser

class Movie():
    def __init__(self, movie_title,movie_storyline,movie_image,movie_trailer):
        '''take the movie title, storyline, poster url, and youtube trailer
        link to create a class that we can use in a trailer website'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        '''open the youtube trailer link on the default browser'''
        webbrowser.open(self.trailer_youtube_url)
