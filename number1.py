import pandas as pd
df = pd.read_csv('8.csv')
df = df['a'].tolist()
n = 0
for i in df:
    if (i%2 == 0):
        n+=1
print(n)
print(df)
# n = 1
# for i in range(90,251):
#     if (i % 2 == 0):
#         print(i)
#         print(n)
#         n += 1
# print(n)

