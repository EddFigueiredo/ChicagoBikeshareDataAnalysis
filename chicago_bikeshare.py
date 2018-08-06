#!/bin/python
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]
for row in range(20):
    print(data_list[row])

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")
for row in range(20):
    print(data_list[row][-2])

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    column_list = []
    for column in data:
        column_list.append(column[index])
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0
genders = column_to_list(data_list, -2)
for gender in genders:
    if gender == 'Male':
        male += 1
    elif gender == 'Female':
        female += 1


# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list: list):
    """
      Args:
          data_list: The first parameter. Must be a list
      Returns:
          A list (Male, Female) with integers corresponding to the count of males on index 0 and count of females on index 1
    """
    male = 0
    female = 0
    for data in column_to_list(data_list, -2):
        if data == 'Male':
            male += 1
        elif data == 'Female':
            female += 1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list: list):
    """
      Args:
          data_list: The first parameter. Must be a list
      Returns:
          A string (Male, Female, Equal) corresponding to the most popular gender on the list
    """
    answer = ""
    genders = count_gender(data_list)
    if genders[0] > genders[1]:
        answer = "Male"
    elif genders[0] < genders[1]:
        answer = "Female"
    elif genders[0] == genders[1]:
        answer = "Equal"
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

def count_user_type(datalist: list):
    """
      Args:
          datalist: The first parameter. Must be a list
      Returns:
          A dictionary with keys corresponding to unique items on datalist and value corresponding to total count.
    """
    types = column_to_list(datalist, -3)
    unique_types = set(types)
    count = {}
    for type in unique_types:
        count.update({type: 0})
    for type in types:
        count[type] += 1
    return count

def plot_chart(dataset: list, labels: dict):
    """
      Args:
          dataset: The first parameter. Must be a list
          labels: The second parameter. Must be a dictionary
      Returns:
          Nothing, plot the chart with values contained in the dataset, showing labels on labels
    """
    user_types = dataset
    types = [type for type in user_types]
    quantity = [user_types[type] for type in user_types]
    y_pos = list(range(len(types)))
    plt.bar(y_pos, quantity)
    plt.ylabel(labels['label-y'])
    plt.xlabel(labels['label-x'])
    plt.xticks(y_pos, types)
    plt.title(labels['label-title'])
    plt.show(block=True)

user_types = count_user_type(data_list)
labels = {'label-y': 'Quantity','label-x': 'Types', 'label-title': 'Quantity by Types'}

plot_chart(user_types, labels)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Some of the rows are empty."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)

def mininum(duration_list: list):
    """
      Args:
          duration_list: The first parameter. Must be a list
      Returns:
          An integer representing the minimum value in duration_list
    """
    min_value = 99999999
    last_min = 0
    for idx in range(1,len(duration_list)):
        last = int(duration_list[idx-1])
        current = int(duration_list[idx])
        if current < last:
            last_min = current
        else:
            last_min = last
        if last_min < min_value:
            min_value = last_min
    return min_value

def maximum(duration_list: list):
    """
      Args:
          duration_list: The first parameter. Must be a list
      Returns:
          An integer representing the maximum value in duration_list
    """
    max_value = 0
    last_max = 0
    for idx in range(1,len(duration_list)):
        last = int(duration_list[idx-1])
        current = int(duration_list[idx])
        if current > last:
            last_max = current
        else:
            last_max = last
        if last_max > max_value:
            max_value = last_max
    return max_value

def mean_value(duration_list: list):
    """
      Args:
          duration_list: The first parameter. Must be a list
      Returns:
          A float representing the mean value of duration_list
    """
    total = 0
    for duration in duration_list:
        total += int(duration)
    return float(total/len(duration_list))

def is_even(durations: list, total: int):
    """
      Args:
          durations: The first parameter. Must be a list
          total: The second parameter. Must be a integer representing the total length of durations
      Returns:
          An integer representing the mean value on both middle index
    """
    return durations[round(total//2)] + durations[round(total//2+1)] / 2

def is_odd(durations: list, total: int):
    """
      Args:
          durations: The first parameter. Must be a list
          total: The second parameter. Must be a integer representing the total length of durations
      Returns:
          An integer representing the value on the middle index of list durations
    """
    durations.sort()
    return durations[round(total//2)]

def median_value(duration_list: list):
    """
      Args:
          duration_list: The first parameter. Must be list
      Returns:
          Integer median value found on duration_list
    """
    total = len(duration_list)
    durations = [int(duration) for duration in duration_list]
    median = 'even' if total % 2 == 0 else 'odd'
    odd_or_even = {'odd': is_odd, 'even': is_even}
    return odd_or_even[median](durations, total)

def variation(duration_list: list):
    """
      Args:
          duration_list: The first parameter. Must be a list
      Returns:
          Dictionary with keys (min, max, mean, median) corresponding to:
          integer minimum value, integer maximum value, float mean value and integer median value,
    """
    return {'min': mininum(duration_list), 'max': maximum(duration_list), 'mean': mean_value(duration_list), 'median': median_value(duration_list)}

trip_variation = variation(trip_duration_list)
min_trip = trip_variation['min']
max_trip = trip_variation['max']
mean_trip = trip_variation['mean']
median_trip = trip_variation['median']


print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, 3))

print("\nTASK 10: Printing start stations:")
print(len(user_types))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
      Example function with annotations.
      Args:
          param1: The first parameter.
          param2: The second parameter.
      Returns:
          List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    return list(set(column_list)), [1 for item in range(len(column_list))]

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------