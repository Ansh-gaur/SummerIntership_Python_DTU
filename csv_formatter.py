<<<<<<< HEAD
import pandas as pd
import os
import sys

input_file = 'towerEoutput.csv'
output_file = 'output.csv'

if not os.path.isfile(input_file):
    print(f"Error: Input file '{input_file}' does not exist.")
    sys.exit(1)

def remove_blank_rows(input_file):
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error: Unable to read the input file '{input_file}'. {e}")
        sys.exit(1)

    try:
        df = df.map(lambda x: str(x).strip() if not pd.isnull(x) else None)
        df = df.map(lambda x: None if x == '' else x)
        df.iloc[:, 0] = df.iloc[:, 0].str.replace(' ', '')

        j = 0
        for i in range(len(df)):
            if pd.isnull(df.iloc[i, 0]):
                if df.loc[i, "Description"] is not None and df.loc[j, "Description"] is not None:
                    df.loc[j, "Description"] = df.loc[j, "Description"] + " | " + df.loc[i, "Description"]
                    df.loc[i, "Description"] = None
            else:
                j = i

        # df = df.dropna(subset=[df.columns[1]])
        df = df.dropna(how='all', axis=0)

        j = 0
        df.iloc[:, 0] = df.iloc[:, 0].astype(str)
        for i in range(len(df) - 1, 0, -1):
            if not df.iloc[i, 0][0].isnumeric() and df.iloc[i, 0] != "None":
                j = i - 1
                while j >= 0:
                    if df.iloc[j, 0][0].isnumeric():
                        df.iloc[i, 0] = df.iloc[j, 0] + " " + df.iloc[i, 0]
                        break
                    j -= 1
        df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: None if str(x) == "None" else x)
        return df
    except Exception as e:
        print(f"Error: An error occurred while processing the DataFrame. {e}")
        sys.exit(1)

try:
    df = remove_blank_rows(input_file)
    df.to_csv(output_file, index=False)
    print(f'Process completed! Saving as {output_file}')
except Exception as e:
    print(f"Error: Unable to save the output file '{output_file}'. {e}")
    sys.exit(1)
=======
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
>>>>>>> 576f884846184a6b2e495387d12ed0db21752ca9
