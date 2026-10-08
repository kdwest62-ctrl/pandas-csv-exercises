import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
tasks = ['1. Print CSV',
         '2. Print first 5 rows',
         '3. Print CSV shape, columns, and data types',
         '4. Exit']
for item in tasks:
    print(item)
while True:
    task = input('Select task: ')
    if task == '1':
        choice = input('(f) full or (t) truncated: ')
        if choice == 'f':
            print(df.to_string())
            print('-' * 8)
        elif choice == 't':
            print(df)
            print('-' * 8)
		else:
			print('Invalid input')
    elif task == '2':
        print(df.head().to_string())
        print('-' * 8)
    elif task == '3':
        print(f'Shape: {df.shape}')
        print()
        print(f'Columns: {df.columns.to_list()}')
        print()
        print(f'Types:\n{df.dtypes}')
        print('-' * 8)
    elif task == '4':
        print('Program closed')
        break
    else:
        print('Invalid input')
