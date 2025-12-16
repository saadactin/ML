# numbers = [1, 3, 7, 2, 9, 4]

# for num in numbers:
#     if num > 5:
#         print(f"Found: {num}")
#         break



# shape
# ans2 = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]

# ])
# print(ans2.shape) 
#  shape =  (rows,columns)
# print(ans2.size) // total number of elements 
# print(ans2.ndim) // number of dimensions 
# print(ans2.dtype) // data type of the elements 
# print(ans2.astype(float)) // convert the array to any data type 

# // fast math operations  without using loops

# print(np.sum(ans2))
# print(np.mean(ans2))
# print(ans2 * 2)
# print(ans2 + 2)


# Aggregation functioms 

# sum , mean , max ,min 

# print(np.std(ans2))
# print(np.var(ans2))

import pandas as pd

df = pd.read_csv('students.csv', encoding='latin1')
# also UTF-8
# df = pd.read_excel('students.xlsx')
# print(df.head())

# we can also read from cloud 

# tocsv() method to convert the dataframe to the csv 
# df.to_csv('students.csv', index=False)\
# so that the index is not included in the csv file

# # explore the data for the first time

# 1 understand the data 
# 2 understand the data types
# 3 understand the data structure
# 4 plan the next steps 

# # how to check the starting rows with head() and tail()

# the first 5 rows by default and if the number is provided then it will show the first n rows

# print(df.info()) 
# //gives the information about the data 
# //shape , data types , missing values 
# //null values , unique values , memory usage 

# print(df.describe()) 
#gives the statistics of the data 
#min , max , mean , std , 25% , 50% , 75% , count 
#missing values , unique values , memory usage

# ask questions  
# 1 how big is the data set
# 2 what are the names of cols 
# print(df.shape)

# # how to access the columns
# xx= df["name"]
# print(xx)

# filtering the rows 
# high_marks = df[(df["science"] > 90 ) & ( df["math"] > 90)]
# print(high_marks)

# Adding cols 
