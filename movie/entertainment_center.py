import media
import fresh_tomatoes


#movie instances
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

butterfly_effect = media.Movie("Butterfly Effect",
                        "An amazing story about the reflection of small changes in life can result in other transformations",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BODNiZmY2MWUtMjFhMy00ZmM2LTg2MjYtNWY1OTY5NGU2MjdjL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SY1000_CR0,0,689,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=DTlEYtHKrYY")

avengers = media.Movie("Avengers",
                        "The Avengers' First Movie",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM4OGJmNWMtOTM4Ni00NTE3LTg3MDItZmQxYjc4N2JhNmUxXkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_SY1000_SX675_AL_.jpg",
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

fight_club = media.Movie("Fight Club",
                        "A depressed man suffering from insomnia meets a strange soap salesman",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzFjMWNhYzQtYTIxNC00ZWQ1LThiOTItNWQyZmMxNDYyMjA5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=BdJKm16Co6M")

mad_max = media.Movie("Mad Max",
                        "Years after the collapse of civilization, the tyrannical Immortan Joe enslaves apocalypse survivors inside the desert fortress the Citadel.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYTY2MTlhMTItZGFiOS00ZGM5LTlhYjUtZWU4NmZmOWJmNzc0XkEyXkFqcGdeQXVyNDUzOTQ5MjY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=hEJnMQG9ev8")

cidade_deus = media.Movie("Cidade de Deus",
                        "In the poverty-stricken favelas of Rio de Janeiro in the 1970s, two young men choose different paths",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNTM4MjZjNWEtMmQxMi00YzY5LTg4ZTAtODJlMDVkZWZmNTVhXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SY1000_CR0,0,677,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=nBWtTrLxUjM")

movies = [toy_story, butterfly_effect, avengers, fight_club, mad_max, cidade_deus]

#opening the page with movies from the list
fresh_tomatoes.open_movies_page(movies)
