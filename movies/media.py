import webbrowser
class Movie():
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.image_url = movie_poster
        self.trailer_url = movie_trailer

    def play_trailer(self):
        webbrowser.open_new_tab(self.trailer_url)
    
