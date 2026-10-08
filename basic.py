import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
print('Tasks')
tasks = ['1. Print CSV',
         '2. Data Loading and Inspection',
         '3. Basic DataFrame Information',
         '4. Count Customers by Country',
         '5. Find Unique Companies',
         '6. Filter by Subscription Date',
         '7. Exit']
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
    elif task == '2':
        print(df.head().to_string())
        print('-' * 8)
    elif task == '3':
        print('(s) shape, (c) columns, (t) data types')
        info = input('Select information: ')
        if info == 's':
            print(f'Shape: {df.shape}')
            print('-' * 8)
        elif info == 'c':
            columns = df.columns.to_list()
            for column in columns:
                print(column)
            print('-' * 8)
        elif info == 't':
            print(f'Types:\n{df.dtypes}')
            print('-' * 8)
        else:
            print('Invalid input')
    elif task == '4':
        pass
    elif task == '5':
        pass
    elif task == '6':
        pass
    elif task == '7':
        print('Program closed')
        break
    else:
        print('Invalid input')
