# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl.
# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE.

# Today we will be looking at Kaggle's datasets and learning how to use data in our program

# First lets explore datasets! Go to Kaggle.com!
# Go to datasets and explore a dataset that find interesting. Think about questions you could answer that that data

# After spring break we will start data analysis on this data set: https://www.kaggle.com/gregorut/videogamesales
# Now we will learn how to analyze the data by practicing on a smaller dataset that I made:
# https://www.kaggle.com/msalaway/meeting-15-practice-dataset-chaparral-cs-club

# Lets find out who has a more shoes: girls or boys! (These are made up numbers)
# It may be more work to code it rather than by hand, but imagine this dataset with every person age 5-15

# First lets download the CSV file and load it into our program.
# We do this with a mod called pandas - go here: https://pandas.pydata.org/getting_started.html
# The cheat sheet at the bottom of the page is extremly useful - Simplified documentation

import pandas as pd         # This is importing the module
dataset = pd.read_csv(r'C:\Users\matth\Downloads\Meeting #15 Practice Dataset - Chaparral CS Club.csv')
# In the line above we covert the csv file in a manipulatable variable that we can handle in python
print(dataset)      # If you imported and have the correct location, the table should be printed in the terminal
dataset = dataset.sort_values("Gender")         # This re-organizes the data! Switch "Gender" with "Age"!
print(dataset)      # Watch the changes!

# So how do we traverse each row of the dataset?
# Like most algorithms, there are multiple ways to reach the same outcome. Here is what I prefer currently:

for i in range(len(dataset)):       # This creates a for-loop starting at 0 and ending at the length of the dataset.
# So the variable i would start at 0 and end at 25, increasing by one every time the loop executes.
    row = dataset.iloc[i]           # This takes a row of the dataset at the indicated index of i
    print(row)      # Watch as every row is individually printed to the terminal

# Now we will use the same method as above, but instead of printing each row, we want to count up
# how many shoes each gender has

# So think... how can we do this! There are multiple ways!!!
# One way is to look at each row and determine if it is a boy or girl, using the .contains() method
# Then, concurrently using if statments to execute a counter dependent on which gender

# Let's code it!
