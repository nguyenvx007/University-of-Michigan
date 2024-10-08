# Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”.

olympics = ('Beijing','London','Rio','Tokyo')
print(olympics)


# The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable country.

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

country = []
for tup in tuples_lst:
    country.append(tup[1])
print(country)

# With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.

olymp = ('Rio', 'Brazil', 2016)

city,country,year = olymp
print(city,country,year)

# Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order.

def info(name,gender,age,bday_month,hometown):
    return name,gender,age,bday_month,hometown
print(info('vinh','male','70','jan','denver'))

# Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country. You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}


# Option #1 Use subscripts

num_medals=[]
for team_medal in gold.items():
    num_medals.append(team_medal[1])
print(num_medals)

# Option #2 Use Assingment/unpacking into iterable variable

num_medals=[]
for team,medal in gold.items():
    num_medals.append(medal)
print(num_medals)
