import fresh_tomatoes
import media

# This file contains the various movies and their individual information.

toy_story = media.Movie('Toy Story',
                        'A movie about toys coming to life.',
                        'https://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')

ice_age = media.Movie('Ice Age',
                      'A movie about animals protecting a child',
                      'https://images-na.ssl-images-amazon.com/images/M/MV5BMTEwMzU0NTEyNTVeQTJeQWpwZ15BbWU2MDIwNzA3OQ@@._V1_.jpg',
                      'https://www.youtube.com/watch?v=cMfeWyVBidk')

avatar = media.Movie('Avatar',
                     'When a marine is on an alien planet',
                     'https://glennewalker.files.wordpress.com/2009/12/c8d13-avatar.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

midnight_in_paris = media.Movie('Midnight in Paris',
                                'A movie about a screenwriter,'
                                ' who travels back in time at midnight.',
                                'https://natashastander.files.wordpress.com/2014/07/mip.jpg',
                                'https://www.youtube.com/watch?v=FAfR8omt-CY')

school_of_rock = media.Movie('School of Rock',
                             'A movie about using rock music to learn',
                             'http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v8_aa.jpg',
                             'https://www.youtube.com/watch?v=-_UedgKyL1o')

ratatouille = media.Movie('Ratatouille',
                          'A Rat is a chef in Paris',
                          'http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg',
                          'https://www.youtube.com/watch?v=3YG4h5GbTqU')

movies = [toy_story, ice_age, avatar, midnight_in_paris, school_of_rock,
          ratatouille]

# Calling the function from fresh_tomatoes to create a html page
# and display the movies.

fresh_tomatoes.open_movies_page(movies)
