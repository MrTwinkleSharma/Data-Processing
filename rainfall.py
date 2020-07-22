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
