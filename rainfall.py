import pandas as pd #importing pandas library for later use as short abbreviation pd

#now i am going to create a canned data to visualize the dataframe
#create a key value pair for dictionary to be passed in Dataframe method

data = { 
'City Name':pd.Series(['Badaun', 'Bareilly' , 'Gorakhpur' ,'Lucknow' ,'Kanpur']),
'Actual': pd.Series(['1.8mm', '25.2mm', '25.6mm', '12.9mm', '10mm']),
'Normal': pd.Series(['5.5mm', '7.1mm', '10.5mm', '4.7mm', '3.2mm']),
}

#format of value of a key is pd.series(alist)
print("Our DataFrame is :\n")
df1 = pd.DataFrame(data)

#similiary can create using CSV and JSON
df2 = pd.read_csv (r'./rain.csv')
df3 = pd.read_json (r'./rain.json')

print(df1,'\n',df2, '\n',df3)
#Data Frame is Two dimensinal array like spread sheet

#this function cleans all the null to 0 without affecting the original dataframe
#syntax newdataframe = olddataframe.fillna(0), Enter what you want to fill 
Cleaned_data = df3.fillna(0)
print(Cleaned_data)
#dropna() is used to drop the number which does not have a value
Cleaned_with_remove_data = df3.dropna(0)
print(Cleaned_with_remove_data)

# Counting the number of rows that missing number
count = 0
for row in df3.iterrows():
  if any(row.isnull()):
    count = count+1
    
#dataframe.iterrows() and series.isnull() are in pandas library, 1st is to iterate the rows and later is for checking is there any of the tuple is false 
# any is inbuilt function in python to check if there is a false in An iterable object (list, tuple, dictionary) then return false

print(count) # will going to print 1 for this condition 

    
