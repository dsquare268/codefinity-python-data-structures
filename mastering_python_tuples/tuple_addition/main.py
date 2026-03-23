animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

#Change tuple to list
updated_animal_movies = list(animal_movies)

#Add more movies to the list
updated_animal_movies.append("Dumbo")
updated_animal_movies.append("Zootopia")

#Change list back to tuple
animal_movies = tuple(updated_animal_movies)

print("Updated animal movies:", animal_movies)