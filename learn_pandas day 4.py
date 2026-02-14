#heandling missing data

# NAN -NOT A NUMBER
# NONE - FOR OBJECT DATATYPE


# ISNULL()
# True - nan is missing
# False - value is present

import pandas as pd 
data = {
    "order_id": [101, 102, None],
    "product": [None, "Laptop", "Headphone"],
    "price": [15000, 55000, None],
    "quantity": [2, 1, None]
}

okay=pd.DataFrame(data)
print(okay)
print(okay.isnull())


# for count missing values
print(okay.isnull().sum())

 #dropna()
# okay.dropna(axis=1,inplace=True)  axis=0 mean removing null values from row , 1 mean from colum


okay.dropna(inplace=True)
print(okay)


#fillna(value,inplace=True)
okay.fillna(0,inplace=True)
print(okay)
okay['price'].fillna(okay['price'].mean(), inplace=True)
print(okay)


#interpolate
#leniar 
#polynomial
#time
#okay.interpolate(method="linear",exis = 0 , inplace = True)

import pandas as pd

okay = {
    "time": [1, 2, 3, 4, 5],
    "value": [10, None, 30, None, 50]
}

okay1 = pd.DataFrame(okay)

print("before interpolate")
print(okay1)



print("after interpolate")
okay1["value"]=okay1["value"].interpolate(method="linear")
print(okay1)