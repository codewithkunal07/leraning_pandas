#adding columns 
import pandas as pd 
data = {
    "order_id": [101, 102, 103],
    "product": ["Phone", "Laptop", "Headphone"],
    "price": [15000, 55000, 2000],
    "quantity": [2, 1, 3]
}

okay=pd.DataFrame(data)
print(okay)

okay['bonus']=okay['price']*0.1
print(okay)



#using insert method 
#df.insert(location,columname,data)

okay1=okay.insert(0,"id",[1,2,3])
print(okay) 


#updating 
#for updating specific row 

#.loc[]
#df.loc['row_index,'colum_nsme'] =  new value

okay.loc[0,'salary'] = 10000
print(okay)

#for updating all rows 
# increasing salary by 5% all data 
okay['price']= okay['price']*1.05
print(okay)


#droping the dat a
#d.okay(colum=['salary'],inplace = true)
print('modifyed data')
okay.drop(columns=['id'],inplace = True)
print(okay)

# for deleting multiple colums

okay.drop(columns=['quantity','salary'],inplace = True)
print(okay)