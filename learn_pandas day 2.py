# describe method
import pandas as pd 
data = {
    "order_id": [101, 102, 103],
    "product": ["Phone", "Laptop", "Headphone"],
    "price": [15000, 55000, 2000],
    "quantity": [2, 1, 3]
}

df = pd.DataFrame(data)
print(df)
print(df.describe())



# two questions we should ask ourself
# how big is our data 
# what are the names of our cloums
import pandas as pd 
data = {
    "order_id": [101, 102, 103],
    "product": ["Phone", "Laptop", "Headphone"],
    "price": [15000, 55000, 2000],
    "quantity": [2, 1, 3]
}

df = pd.DataFrame(data)
print(f"shape: {df.shape}")
print(f"colums :{df.columns}")


#1 select specific colum
#2 filter rows
#3 comine multiple condtions

#1 square braket 
#2 bolean condtions 

#2 filtering rows
#1 a series
#2 data frame multiple colum of data 

# syntax 
# for single colum 
# df = pd["colum_name"]
# for multiple colums
# df = pd["colum_name","colum_name2"]


#2 filtering rows 
# we use bolean indexing 

#based on a single condtion 
# filtering= df[df['salary']>5000]
#for multiple 
# filtering= df[df['salary']>5000 & (df['salary']<100000)]



#real example
import pandas as pd 
data = {
    "order_id": [101, 102, 103],
    "product": ["Phone", "Laptop", "Headphone"],
    "price": [15000, 55000, 2000],
    "quantity": [2, 1, 3]
}

df = pd.DataFrame(data)
single=df['price']
print(single)

single2=df[['price','order_id']]
print(single2)


high_salary=df[df['price']>15000]
print(high_salary)

high_salary2=df[(df['price']>15000) & (df['price'] <100000)]
print(high_salary2)

high_salary3=df[(df['price']>15000) | (df['price'] <10000)]  #| this or 
print(high_salary3)