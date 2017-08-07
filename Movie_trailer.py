import media
import fresh_tomatoes
alaipayuthey=media.Movie("Allaipayuthey","A computer expert (Madhavan) and a crusading doctor (Shalini) marry in secret, then deal with death and trauma",
                         "https://cinemachaat.files.wordpress.com/2010/07/alaipayutheyposter.jpg",
                         "https://www.youtube.com/watch?v=ez_XsttP9Es")



vikram_vedha=media.Movie("Vikram Vedha","The film is a dramatic, action thriller. The movie is the powerful clash between performers Madhavan and Vijay Sethupathy",
                         "http://static.sify.com/cms/image/rhvoLeibbbdef.jpg",
                         "https://www.youtube.com/watch?v=1sVr-uWZPjE")


minnale = media.Movie("Minnale","A man falls in love with a woman and cons his way into her heart through lies.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BZjAwOGY4ZWQtYTIwNi00MTFkLWE2ODQtZDcwZTQwNTQwOTNhXkEyXkFqcGdeQXVyMjAzMjcxNTE@._V1_UY1200_CR107,0,630,1200_AL_.jpg",
                      "https://www.youtube.com/watch?v=idcHIv088xQ")

ghajini = media.Movie("Ghajini","A man, who loses his memory every 15 minutes, has photographs, notes and tattoos to remind him to kill the man who brutally murdered his sweetheart.",
                      "https://2.bp.blogspot.com/-cPAj_Qlgous/U0WJi9bzNPI/AAAAAAAAF3U/-e5IJm6AL0w/s1600/Surya+Asin+Ghajini+Movie+HD+Images+Posters+Wallpapers+Pics+Photos+Firstlook+Stilla+(49).jpg",
                      "https://www.youtube.com/watch?v=tlvrGfHbPsw")

ayan = media.Movie("Ayan","A computer engineer (Suriya) leads a double life as a smuggler.",
                   "http://www.5starmusiq.com/movieimages/Tamil/A/Ayan_B.jpg",
                   "https://www.youtube.com/watch?v=VHsK5zfGmOE")

singam = media.Movie("Singam","The series follows the adventures of an honest police officer from Nallur, Durai Singam.",
                     "https://2.bp.blogspot.com/-9wQEkq_xzek/WImJXdSpmfI/AAAAAAAAFgU/cgvW56w3Pw4GV3pmjrJbVY07jo8onxuzQCLcB/s320/hqdefault.jpg",
                     "https://www.youtube.com/watch?v=96CgGu1JYbY")

enthiran = media.Movie("Enthiran","After countless weeks of seclusion in his laboratory, the brilliant Dr. Vaseegaran (Rajnikanth) emerges with his latest invention: Chitti (also Rajnikanth), an android created in his own image.",
                       "http://media2.intoday.in/indiatoday/images/stories/robo_647_061716115359.jpg",
                       "https://www.youtube.com/watch?v=Ghh1Y7lsWwk")

padayappa = media.Movie("Padayappa","The death of Padaiyappa's father destroys his family. But his luck changes, and he is able to lead a prosperous life, until his nemesis plots to ruin his happiness once more.",
                        "https://movieclickz.com/wp-content/uploads/2015/08/Movie-of-the-Day-Padayappa.jpg",
                        "https://www.youtube.com/watch?v=CnRXxRmPMQg")

sivaji = media.Movie("Sivaji","Sivaji returns from the U.S. to invest his money for good causes, but seeing his rising popularity, the politicians cheat him out of his property. Sivaji takes this as a challenge.",
                     "http://moviegalleri.net/wp-content/gallery/sivaji-3d-movie-release-posters/sivaji_the_boss_3d_release_posters_rajini_shriya_2592507.jpg",
                     "https://www.youtube.com/watch?v=Y7znvurIqRA")


movies=[alaipayuthey,vikram_vedha,minnale,ghajini,ayan,singam,enthiran,padayappa,sivaji]
fresh_tomatoes.open_movies_page(movies)