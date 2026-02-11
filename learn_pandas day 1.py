# pandas
# read data from a csv file into  a data frame 
import pandas as pd

df = pd.read_csv(
    r"C:\Users\Dell\Downloads\sales_data_sample.csv",
    encoding="latin1"
)

print(df.head())


# read data from a json file into  a data frame 
import pandas as pd

df = pd.read_json(
    r"C:\Users\Dell\Downloads\sample_Data.json"
)

print(df.head())


import pandas as pd

data = {
    "order_id": [101, 102, 103],
    "product": ["Phone", "Laptop", "Headphone"],
    "price": [15000, 55000, 2000],
    "quantity": [2, 1, 3]
}

df = pd.DataFrame(data)
print(df)


# df.to_csv("sales_data.csv", index=False) # for removing index  use index=fales
# #we use it for saving files in csv.

# df.to_excel("sales_data.xlsx", index=False)
# for saving in excel file 

# df.to_json("sales_data.json", index=False)
# for saving in json  file 


# head(10) - print starting 10 rows
# tail(10) - print end 10 rows
# head(n) - by default 5
# tail(n) - by default 5

import pandas as pd
df = pd.read_csv(
    r"C:\Users\Dell\Downloads\sales_data_sample.csv",
    encoding="latin1"
)

print(df.head())


import pandas as pd
df = pd.read_csv(
    r"C:\Users\Dell\Downloads\sales_data_sample.csv",
    encoding="latin1"
)

print(df.tail())


#understanding the data
import pandas as pd

df = pd.read_csv(
    r"C:\Users\Dell\Downloads\sales_data_sample.csv",
    encoding="latin1"
)

print(df.info())

# ex_2
import pandas as pd

data = {
    "order_id": [101, 102, 103],
    "product": ["Phone", "Laptop", "Headphone"],
    "price": [15000, 55000, 2000],
    "quantity": [2, 1, 3]
}

df = pd.DataFrame(data)
print(df.info)



