
#For list of tuples providek, create a list of the third element in each tuple item.
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
t_check = []
for tup in lst_tups:
    t_check.append(tup[2])
print(t_check)


# 5. Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called 'seconds'.
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

seconds = []
for tup in tups:
    seconds.append(tup[1])
print(seconds)

# Swapping with Tuple

a = 1
b = 2
(a, b) = (b, a)