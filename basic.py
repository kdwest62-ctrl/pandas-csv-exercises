import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
tasks = ['1. Show first 5 rows',
         '2. Exit']
for item in tasks:
    print(item)
while True:
    task = input('Select task: ')
    if task == '1':
        print(df.head().to_string())
    elif task == '2':
        print('Program closed')
        break
    else:
        print('Invalid input')
