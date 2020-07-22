import pandas as pd #importing pandas library for later use as short abbreviation pd

#now i am going to create a canned data to visualize the dataframe
#create a key value pair for dictionary to be passed in Dataframe method

data = { 
'City Name':pd.series([Badaun, Bareilly ,Gorakhpur ,Lucknow ,Kanpur])
'Actual': pd.series(['1.8mm', '25.2mm', '25.6mm', '12.9mm', '10mm'])
'Normal': pd.series(['5.5mm', '7.1mm', '10.5mm', '4.7mm', '3.2mm'])
}

#format of value of a key is pd.series(alist)
print("Our DataFrame is :\n")
df = pd.Dataframe(data)
print(df)
