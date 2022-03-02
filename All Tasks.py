# Ex 11.5 Dictionaries:

# Task 1:

dict1 = {}
enter_yes, print_yes = 'y', 'y'
prod_name, prod_price = "", 0
while enter_yes == 'y':
    prod_name = input("Enter a product name: ")
    prod_price = eval(input("Enter a product price: "))
    dict1[prod_name] = prod_price
    enter_yes = input("Add another product? (y/n): ")
    if enter_yes == 'n':
        break
while print_yes == 'y':
    search_prod = input("Enter a product name to search: ")
    search_price = dict1.get(search_prod, "not found")
    if search_price == "not found":
        print("Sorry, item not in list.")
    else:
        print("Price for product is:", dict1[search_prod])
    print_yes = input("Search for another product? (y/n): ")
    if print_yes == 'n':
        break

# Task 2:

dict1 = {}
enter_yes, print_yes = 'y', 'y'
prod_name, prod_price = "", 0
while enter_yes == 'y':
    prod_name = input("Enter a product name: ")
    prod_price = eval(input("Enter a product price: "))
    dict1[prod_name] = prod_price
    enter_yes = input("Add another product? (y/n): ")
    if enter_yes == 'n':
        break
while print_yes == 'y':
    search_price = input("Enter a price in dollars: ")
    dict1_values = dict1.values()
    dict1_val_list = list(dict1)
    print(dict1_val_list)
    for i in range(len(dict1_val_list)):
        if dict1_val_list[i] >= search_price:
            del dict1_val_list[i]
    print("Values lower then price entered are:", dict1_val_list)
    print_yes = input("Enter another price? (y/n): ")
    if print_yes == 'n':
        break

# Task 3:

days = {'January': 31, 'February': 28, 'March': 31, 'April': 30,
        'May': 31, 'June': 30, 'July': 31, 'August': 31,
        'September': 30, 'October': 31, 'November': 30, 'December': 31}

# Task 3 Part (a):
month_name = input("Enter name of a month: ")
print("Number of days in this month is:", days[month_name])

# Task 3 Part (b):
day_keys = list(days)
day_keys.sort()
print(day_keys)

# Task 3 Part (c):
for i in days:
    if days[i] == 31:
        print(i)

# Task 3 Part (d):
print("February")
for i in days:
    if days[i] == 30:
        print(i)
for i in days:
    if days[i] == 31:
        print(i)

# Task 3 Part (e):
month_name = input("Enter name of a month: ")
if month_name in days:
    print("Number of days in this month is:", days[month_name])  # Task 14

d = [{'name': 'Ali', 'phone': '0301-1532414', 'email': 'ali246@mail.net'},
     {'name': 'Muhammed', 'phone': '0320-1645318', 'email': 'muhammed86@mail.net'},
     {'name': 'Rustam', 'phone': '0364-3174341', 'email': ''},
     {'name': 'Ahmed', 'phone': '0326-2353718', 'email': 'ahmed232@mail.net'}]
for i in d:
    if i["email"] == '':
        print(i["name"])

# Task 5:

team_data = {"Fire-Eagles": [6, 5], "Deer-Fangs": [7, 4], "Death-Sabres": [8, 3]}

while True:
    team_name = input("Enter a team name: ")
    team_wins = eval(input("Enter team wins: "))
    team_losses = eval(input("Enter team losses: "))
    team_scores = [team_wins, team_losses]
    team_data[team_name] = team_scores
    Is_entry = input("Enter another team and their scores? [y/n]: ")
    if Is_entry == "n":
        break
print(team_data)

# Task 5 part (a):

team_data = {"Fire-Eagles": [6, 5], "Deer-Fangs": [7, 4], "Death-Sabres": [8, 3]}

team_name = input("Enter a team name: ")
team_scores = team_data[team_name]
team_total = team_scores[0] + team_scores[1]
win_percentage = (team_scores[0] / team_total) * 100
print(win_percentage)

# Task 5 part (b):

total_wins = []
team_values = team_data.values()
team_list = list(team_values)
for i in range(len(team_list)):
    total_wins.append(team_list[i][0])
print(total_wins)

# Task 7:

grid_1 = [36, 41, 24, 39, 38, 4, 2, 10, 19, 33, 30, 30, 47, 26, 27, 28, 20, 40, 38, 18, 2, 34, 4, 14, 8]
grid_dict = {}

for i in range(len(grid_1)):
    if i in grid_1:
        dict1[i] = grid_1.count(i)

print(grid_dict)

# Task 14

d = [{'name': 'Ali', 'phone': '555-1414', 'email': 'ali246@mail.net'},
     {'name': 'Muhammed', 'phone': '555-1618', 'email': 'muhammed86@mail.net'},
     {'name': 'Rustam', 'phone': '555-3141', 'email': ''},
     {'name': 'Ahmed', 'phone': '555-2718', 'email': 'ahmed232@mail.net'}]
for i in d:
    if i["email"] == '':
        print(i["name"])
