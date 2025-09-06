movie_list = ["Interstellar", "Inception", "The Prestige", "Insomnia", "Batman Begins"]
ratings_list = [1, 10, 10, 8, 6]

# We want to merge movie_list and ratings_list into a list of tuples
# We can use `zip` function to merge two lists
print(list(zip(movie_list, ratings_list)))
