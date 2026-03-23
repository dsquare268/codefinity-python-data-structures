movie_genres = ("Action", "Comedy", "Drama", "Horror", "Sci-Fi")

# Write your code here
temp_list = list(movie_genres)

print("Prior genre:", temp_list)

temp_list[2] = "Thriller"  
temp_list[3] = "Adventure"  


movie_genres = tuple(temp_list)

temp_list.clear()

# Testing
print("Updated genres:", movie_genres)
print("What's left in temp_list:", temp_list)