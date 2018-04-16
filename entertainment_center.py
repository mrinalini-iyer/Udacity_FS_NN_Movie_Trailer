"""This file runs to loads a website that stores a list of
   movie titles, along with respective box art imagery and
   movie trailer website.
"""
import media
import fresh_tomatoes

# 1. Instantiating toy story movie class with its information.
toy_story = media.Movie(
    "Toy Story",
    "A boy and his toys that come to life.",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# 2. Instantiating Avatar movie class with its information.
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet.",
    "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io")

# 3. Instantiating Fight Club movie class with its information.
fight_club = media.Movie(
    "Fight Club",
    "A man discontended with his whitecollar job.",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

# 4. Instantiating ratatouille movie class with its information.
ratatouille = media.Movie(
    "Ratatouille ",
    "Remy, a young and ambitious rat wants to become a cook.",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=1yKqLNnxGZw")

# 5. Instantiating midnight in paris movie class with its information.
midnight_paris = media.Movie(
    "Midnight in Paris",
    "Screenwriter forced to confront the shortcoming of his relationship.",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/\
Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=BYRWfS2s2v4")

# 6. Instantiating finding nemo movie class with its information.
finding_nemo = media.Movie(
    "Finding Nemo",
    "Epic journey of bringing Nemo home.",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
    "https://www.youtube.com/watch?v=sdesVtORgR4")


# List of all favorite movies to be displayed on the website.
movies = [toy_story, avatar, fight_club,
          ratatouille, midnight_paris, finding_nemo]

"""
    Using starter code - fresh_tomatoes module provided by Udacity to generate
    a website that displays our list of movies.
"""
fresh_tomatoes.open_movies_page(movies)
