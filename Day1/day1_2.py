import pandas as pd

df = pd.read_csv('input.txt', sep='\s+', header=None, names=['Column1', 'Column2'])

arr1 = df['Column1'].tolist()
arr2 = df['Column2'].tolist()

res = sum(elem * arr2.count(elem) for elem in arr1)

print(res)