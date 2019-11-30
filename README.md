# Data Visualization
Project to learn on Data Visualization

## Project 1:
Project to plot a pie chart using book dataset
Steps:
* Load the CSV file into a dataframe
* Select the "Place of Publication" column
* Count the values in the selected column to know how many times each unique value has appeared in the column
* Plot a pie chart for the value counts calculated in the previous step

## Project 2:
Project to create bar chart based on iris dataset
Steps:
* Load the CSV file into a dataframe
* Group by the dataframe based on the "species" and calculate the mean
* Plot a bar chart

## Project 3:
Project to plot two scatter charts using iris dataset
Steps:
* Load the CSV file into a dataframe
* Split the dataset into three dataframes based on the three species
* Plot a scatter chart using x='sepal_length', y='sepal_width', and separate colors for each of the three dataframes
* You need to link the three scatter charts to plot them in a single figure
* Repeat the last two steps with x='petal_length', y='petal_width'

## Project 4:
Project to plot it in  two separate figures and display both charts into one figure
Steps:
* Load the CSV file into a dataframe
* Split the dataset into three dataframes based on the three species
* Manually create the subplots with matplotlib while creating the subplots, set the number of rows to 1 and columns to 2
* Plot a scatter chart using x='sepal_length', y='sepal_width', and separate colors for each of the three dataframes
* You need to link the three scatter charts to plot them in a single figure
* Repeat the last two steps with x='petal_length', y='petal_width' in seperate chart
