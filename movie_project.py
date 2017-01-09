#importing the class we created from media
import media
import fresh_tomatoes

#input the movies using the media class

#add: who framed roger rabbit
roger_rabbit = media.Movie("Roger Rabbit", "A story about a Rabbit who is framed "
                           "and the detective that helps him",
                           "https://upload.wikimedia.org/wikipedia/en/3/32/Movie_poster_who_framed_roger_rabbit.jpg",
                           "https://www.youtube.com/watch?v=OFCIaMyMORg")

#indiana jones movoe
indiana_jones = media.Movie("Indiana Jones","A brave archeologist saves the "
                            "world and goes on adventures",
                            "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
                            "https://www.youtube.com/watch?v=4uABsht2bgY")

#the first back to the future movie
back_to_the_future = media.Movie("Back to the future","Time travel with Doc brown and "
                                 "Marty McFly",
                                 "https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
                                 "https://www.youtube.com/watch?v=qvsgGtivCgs")

#the 2nd batman movie
the_dark_knight = media.Movie("The dark Knight","Batman and the Joker battle blending "
                              "the lines of good and evil",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "ttps://www.youtube.com/watch?v=EXeTwQWrcwY")

#the Movie 'Sing'
sing = media.Movie("Sing","Animals have a singing competition to save the theatre",
                   "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=Y7uGHY-t80I")

#the minions movie
the_minions = media.Movie("The Minions","The story of how the minions got to where "
                          "we later meet them",
                          "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                          "https://www.youtube.com/watch?v=dVDk7PXNXB8")

#putting all movie vars in the list
movies=[roger_rabbit, indiana_jones,back_to_the_future, the_dark_knight, sing, the_minions]

#using the given file from udacity to create web site
fresh_tomatoes.open_movies_page(movies)

