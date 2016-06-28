import fresh_tomatoes
import media

toystory = media.Movie("Toy Story","A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.","https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Toy_Story_logo.svg/2000px-Toy_Story_logo.svg.png","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toystory.storyline)

walle = media.Movie("Wall E", "In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.","https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg","https://www.youtube.com/watch?v=alIq_wG9FNk")

#walle.play_trailer()

zootopia = media.Movie("Zootopia", "In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.", "https://upload.wikimedia.org/wikipedia/commons/f/f3/Zootopia_logo.svg", "https://www.youtube.com/watch?v=bY73vFGhSVk")


kungfupanda = media.Movie("Kung Fu Panda", "In the Valley of Peace, Po the Panda finds himself chosen as the Dragon Warrior despite the fact that he is obese and a complete novice at martial arts.", "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg", "https://www.youtube.com/watch?v=PXi3Mv6KMzY")


cars = media.Movie("Cars", "A hot-shot race-car named Lightning McQueen gets waylaid in Radiator Springs, where he finds the true meaning of friendship and family.", "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg", "https://www.youtube.com/watch?v=WGByijP0Leo")


minions = media.Movie("Minions", "Minions Stuart, Kevin and Bob are recruited by Scarlet Overkill, a super-villain who, alongside her inventor husband Herb, hatches a plot to take over the world.", "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg", "https://www.youtube.com/watch?v=eisKxhjBnZ0")


movielist = [toystory, walle, zootopia, kungfupanda, cars, minions]

#fresh_tomatoes.open_movies_page(movielist)

print(media.Movie.__name__)
print(media.Movie.__module__)
