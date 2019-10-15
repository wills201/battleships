import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name':['john','mary',5,[1,2,3],('bill',),'lisa','jose'],
    'age':[23,78,22,19,45,33, "helo"],
    'gender':['M','F','M','M',"M",5,'B'],
    'num_children':["hi",0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})
print(df)

def clean_data(df):
    for elem in df:

        all_types = {}

        for element in df[elem]:
            if type(element) in all_types:
                all_types[type(element)] += 1
            else:
                all_types[type(element)] = 1


        max_val = max(all_types.values())

        for element in all_types:
            if all_types[element] == max_val:
                max_key = element

        for index in range(len(df[elem])):
            if not(isinstance(df[elem][index], max_key)) and len(all_types) > 1:
                df[elem][index] = None
    return df

df = clean_data(df)

print(df)