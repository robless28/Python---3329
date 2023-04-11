# Direct console interaction 
# text file input (flat file, txt)
# Table date (rows and columns, .xls or .csv)
# using pandas
import pandas

data = pandas.read_csv('bestsellers.csv', sep=';')

# show me some data on the imported table
print(data.info())

# preview the data in the table 
print(data.head(2))

# find the max price of a book in this table 
# only want Price column
print(data['Price'].max())                                     # What is the maximum price of a book on the list?

# print the average price of all books in the column 
# print(data['Price'].mean())                                 # What is the average price of a book on this list?

# data.plot('Price')
# plt.show()  

# Value counts 
# Shows all values in the column 
    # and the number of times each va,ue appears 
print(data.Author.value_counts())

# Filter only rows from a certain year 
print(data.Year == 2010) 
yearEx = data[data.Year == 2010]                       
print(yearEx.head())

print(data.Author.head(n=5))                                  # Shows the first 5 authors 

print(data['User Rating'].min())                              # What is the lowest user rating for a book on this list?

print(data['Year'].min())                                     # How many years of data does this dataset cover?
print(data['Year'].max()) 
# print(data['Year'].period_range())                                                                

print(data.Author.unique())                                   # How many unique authors are on this list?