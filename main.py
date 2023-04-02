import pandas as pd
import numpy as np
desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

dict1 = {
    "Name": ["Hunain", "Aman", "Wasiq", "Kashi"],
    "Marks":[89, 97, 75, 87],
    "City" :["Hyderabad", "Matli", "Matyari", "Kotri"]
}
df = pd.DataFrame(dict1)
# print(df)
# df.to_csv("Marksheet.csv",index=False)
print(df.head(2))    # It provide the head(Starting Part) of the sheet with given parameter
print(df.tail(2))    # It provide the Tail(Ending Part) of the sheet with given parameter
print(df.describe()) # (It gives the statistical analysis(Calculate count,means,std,min,max,25%,50%,75%)

# If you want to read a excel sheet in this
data = pd.read_csv("name.csv")  This will make the external made sheet read in python
# if you want to change the value in that sheet
# name[column name][index which want to change] = value

#                                   Example Of Series
ser =pd.Series(np.random.rand(34))
print(ser)

                                    # Example of DataFrame
newdf = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
print(newdf)
print(newdf.dtypes)
print(newdf.columns)
print(newdf.index)

# If you want to convert this data frame into numpy array:
print(newdf.to_numpy())

# Transpose : Rows converted into columns and columns into rows
print(newdf.T)

# For sorting
# Here axis 0 = Rows & axis 1 = Columns,, ascending false = descending order & ascending True = Ascending order
print(newdf.head().sort_index(axis=0, ascending=True))

# Here newdf2 is the view of newdf as we will change anything in newdf2 it will also change that thing in newdf
newdf2 = newdf
newdf2[0][0] = 123
print(newdf.head())

# if we want to copy a dataframe into anyother variable then:
newdf2 = newdf.copy()
newdf2[0][0] = 32
print(newdf.head())


#                                 To get the data of netflix

data = pd.read_csv("netflix.csv")
print(data)
print(data["title"].value_counts())   # value count for particular thing
print(data.columns)
a = data.loc[(data.rating == "PG-13")]
print(a)
a = data.loc[(data.rating == "PG-13") & (data["release year"] == 2013)]
print(a)
print(data.isnull().sum())
print(data.notnull().sum())
b = data.loc[(data.rating == "TV-14") & (data["user rating score"] >= 90)]
print(b)
c = data.loc[(data.rating == "TV-14"),["title","release year","rating"]]
print(c)
#                 Function of iloc

d = data.iloc[[2,5]] # want particular rows
Here the list after comma is used what to show of the particular given categorie
print(d)
e = data.iloc[[2,5],0:3] # want particular rows with particular columns
print(e)

#                           Assignment for pokemon
#  Find the Lowest and Highest HP in the pokemon dataset
data = pd.read_csv("Pokemon.csv")
print(data)
print(data.columns)
a = data["HP"].min()
b = data["HP"].max()
c = data["Speed"].min()
print("Minimum HP is :", a)
print("Maximum HP is :", b)
print(c)

#                               Value Counts
print(data["Type 1"].value_counts())

# To sort the values in an particular column.....
# (Ascending order)
print(data.sort_values("Speed"))
# (Descending order)
print(data.sort_values(Speed,ascending=False))
print(data.sort_values([Speed,generation],ascending=[False,true]))


# Speed highlow......HP highlow


# Feature Engineering
# add column

Attack_high_low > "Attack High" , "Attack Low"

attack_mean = data["Attack"].mean()
#
def set_attack(val):
    if val < attack_mean:
        return "Attack High"
    elif val == attack_mean:
        return "Attack Neutral"
    else:
        return "Attack Low"

data["Attack_high_low"] = data["Attack"].apply(set_attack)
print(data)

# Group by
data1 = data.groupby("type 1").groups
print(data1)

data = pd.read_csv("netflix_titles.csv")
print(data)
