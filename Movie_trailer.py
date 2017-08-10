import media
import fresh_tomatoes

# Alaipayuthey is an instance of the class Movie.
# Values of movie_title, movie_storyline, poster_image, trailer_youtube are provided below.
alaipayuthey = media.Movie(
    "Allaipayuthey",
    "Love, makes life beautiful",
    "https://cinemachaat.files.wordpress.com/2010/07/alaipayutheyposter.jpg",
    "https://www.youtube.com/watch?v=ez_XsttP9Es")

# Vikram_vedha is an instance of the class Movie.
vikram_vedha = media.Movie(
    "Vikram Vedha",
    "The movie is the powerful clash between the heros",
    "http://static.sify.com/cms/image/rhvoLeibbbdef.jpg",
    "https://www.youtube.com/watch?v=1sVr-uWZPjE")

# Minnale is an instance of the class Movie.
minnale = media.Movie(
    "Minnale",
    "A man falls in love truely.",
    "https://i.ytimg.com/vi/vjvfRhHeFYI/hqdefault.jpg",
    "https://www.youtube.com/watch?v=idcHIv088xQ")

# Ghajini is an instance of the class Movie.
ghajini = media.Movie(
    "Ghajini",
    "A man, who loses his memory every 15 minutes.",
    "http://www.koodal.com/cinema/cine_reviews/2005/ghajini-192.jpg",
    "https://www.youtube.com/watch?v=tlvrGfHbPsw")

# Ayan is an instance of the class Movie.
ayan = media.Movie(
    "Ayan",
    "A computer engineer leads a double life as a smuggler.",
    "http://www.5starmusiq.com/movieimages/Tamil/A/Ayan_B.jpg",
    "https://www.youtube.com/watch?v=6hoMoknGJn0")

# Singam is an instance of the class Movie.
singam = media.Movie(
    "Singam",
    "An honest police officer, Durai Singam.",
    "http://media2.intoday.in/indiatoday/images/stories/singam-story_647_021117100744.jpg",
    "https://www.youtube.com/watch?v=96CgGu1JYbY")

# Enthiran is an instance of the class Movie.
enthiran = media.Movie(
    "Enthiran",
    "Dr.Vaseegaran invents: Chitti, an android robot.",
    "http://media2.intoday.in/indiatoday/images/stories/robo_647_061716115359.jpg",
    "https://www.youtube.com/watch?v=mLvDObZZpqU")
 
# Padayappa is an instance of the class Movie.
padayappa = media.Movie(
    "Padayappa",
    "hardwork changes the life.",
    "https://movieclickz.com/wp-content/uploads/2015/08/Movie-of-the-Day-Padayappa.jpg",
    "https://www.youtube.com/watch?v=CnRXxRmPMQg")

# Sivaji is an instance of the class Movie.
sivaji = media.Movie(
    "Sivaji",
    "Sivaji invest his money for good causes, but politicians cheat him.",
    "http://static.sify.com/cms/image/pclwqAebjgfjc.jpg",
    "https://www.youtube.com/watch?v=Y7znvurIqRA")

# movies is a list of all the instances of the class Movie
movies = [alaipayuthey, vikram_vedha, minnale, ghajini,
          ayan, singam, enthiran, padayappa, sivaji]
# movies list is passed as a parameter value in to open_movies_page
# fresh_tomatoes is a module which contains the function open_movies_page
fresh_tomatoes.open_movies_page(movies)


