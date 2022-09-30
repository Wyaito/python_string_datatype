# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
my_first_name = 'Wyatt'
#   - my_last_name
#       -set this equal to your last name
my_last_name = 'Lynch'
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
my_year_of_birth = 2002
#   - current_year
#       -set this equal to 2020
current_year = 2022

# TODO String Indexingggg
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - second two letter of your last name (use the -index)
# print(my_first_name)
# print(my_last_name)
# print(my_first_name[0])
# print(my_last_name[-4])
# print(my_first_name[0:2])
# print(my_last_name[-2])
#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times
# print(my_first_name,my_last_name)
# print((my_first_name +"\n") * 6)





# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - Birth Year Statement = first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year
# birthYearStatement = my_first_name + " " +my_last_name + ' was born in ' + str(my_year_of_birth)
birthYearStatement = "{} {} was born in {}"
print(birthYearStatement.format(my_first_name, my_last_name, my_year_of_birth))
birthdayCelebration = "{} {} was born in {} {} enjoyed celebrating {}"
print(birthdayCelebration.format(my_first_name, my_last_name, my_year_of_birth, my_first_name, current_year))

# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year
escapeExample = "{}\'s birth year is {}"
print(escapeExample.format(my_first_name, my_year_of_birth))
#print("Wyatt's computer")
escapeLastName = '\t{}'
print(escapeLastName.format(my_last_name))
# TODO Escape characters

# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case
print(my_first_name.casefold(),my_last_name.casefold())
print(len(my_last_name))
print(my_first_name.upper(),my_last_name.upper())