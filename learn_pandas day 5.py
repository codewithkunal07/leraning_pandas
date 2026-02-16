#sorting data
# sorting data 1 colum sort_values()
#okay.sort_values(by="colum_name", true/false inplace = true)

import pandas as pd

okay = {
    "name": ["kunal", "hasim", "suri", "tushar"],
    "age": [12, 34, 23, 45],
    "salary": [2000, 34444, 233232, 2321]
}

df = pd.DataFrame(okay)
print(df)
df.sort_values(by="age", ascending=True, inplace=True)
print(df)


#for multiple colum sorting 
df.sort_values(by=["age","salary"], ascending=[True,True], inplace=True)


# Agrigates function
# df.["colum_name"].mean()
# df.["colum_name"].sum()
# df.["colum_name"].min()
# df.["colum_name"].meax()


import pandas as pd

okay = {
    "name": ["kunal", "hasim", "suri", "tushar"],
    "age": [12, 34, 23, 45],
    "salary": [2000, 34444, 233232, 2321]
}

df = pd.DataFrame(okay)
print(df)
sum_salary = df["salary"].sum()
print(sum_salary)


#groupby in pandas
groupby =df.groupby("age")["salary"].sum()
print(groupby)

# for multiple colum
groupby =df.groupby(["age","name"] )["salary"].sum()
print(groupby)


#merging and joining dataframe 
#pd.marge(df1,df2, on ="column_name",how=  "type of colum")


#example
import pandas as pd 

#customer dataframe 
df_customers = pd.DataFrame({
    "cust_id": [1,2,3],
    "name": ["kunal","hasim","suri"]
})

#order dataframe 
df_orders = pd.DataFrame({
    "cust_id": [1,2,3,4],
    "order_amount": [240,234,232,121]
})



merged1 = pd.merge(df_customers, df_orders, on="cust_id", how="inner")
print(merged1)

merged1 = pd.merge(df_customers, df_orders, on="cust_id", how="outer")
print(merged1)

merged1 = pd.merge(df_customers, df_orders, on="cust_id", how="left")
print(merged1)

merged1 = pd.merge(df_customers, df_orders, on="cust_id", how="right")
print(merged1)

#concatenation  in data frame 
# combine the data set in two format

# 1 vertically (row-wise)
# 2 horizontlly (colum-wise)

# pd.concate([df1,df2],exis =0 ,ignore_index=True)

#vertically
import pandas as pd 
df_region= pd.DataFrame({
    "CustomerId":[1,2],
    "Name":["kunal","hasim"]
})

print(df_region)

import pandas as pd 
df_region2= pd.DataFrame({
    "CustomerId":[3,4],
    "Name":["suri","gouash"]
})

df=pd.concat([df_region,df_region2],axis = 0 ,ignore_index=True)
print(df)

#for vertically
df=pd.concat([df_region,df_region2],axis = 1 ,ignore_index=True)
print(df)
