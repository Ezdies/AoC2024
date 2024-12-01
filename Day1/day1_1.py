import pandas as pd

df = pd.read_csv('input.txt', sep='\s+', header=None, names=['Column1', 'Column2'])

arr1 = df['Column1'].tolist()
arr2 = df['Column2'].tolist()
res = sum(abs(elem1-elem2) for elem1, elem2 in zip(sorted(arr1), sorted(arr2)))
print(res)