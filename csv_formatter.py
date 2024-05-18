import pandas as pd

input_file = '(2)Est.-civil-Table_1.csv'
output_file = 'output.csv'

def remove_blank_rows(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.apply(lambda row: row.str.strip(), axis=1)
    df = df.dropna(how='all', axis=0)
    df.iloc[:, 0] = df.iloc[:, 0].str.replace(' ', '')

    j=0
    for i in range(len(df)):
        if pd.isnull(df.iloc[i, 0]):
            df.iloc[j, 1] += " | " + df.iloc[i, 1]
        else:
            j=i

    df = df.dropna(subset=[df.columns[0]])

    df.to_csv(output_file, index=False)

remove_blank_rows(input_file, output_file)
