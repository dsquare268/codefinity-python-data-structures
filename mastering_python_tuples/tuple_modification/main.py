movie_genres = ("Action", "Comedy", "Drama", "Horror", "Sci-Fi")

# Convert tuple to list
temp_list = list(movie_genres)
# show contents of list
print("Prior genre:", temp_list)

# change contents of list
temp_list[2] = "Thriller"  
temp_list[3] = "Adventure"  

# change the list back to tuple
movie_genres = tuple(temp_list)

# clear the list
temp_list.clear()

# Testing
print("Updated genres:", movie_genres)
print("What's left in temp_list:", temp_list)