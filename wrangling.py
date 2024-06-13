import pandas as pd
import glob
import os

# Set up General Election CSV

# To run this elsewhere, please make sure this path makes sense
generalsPath = r'data/2021SpecialGenerals/'

generalFiles = glob.glob(os.path.join(generalsPath, "*.xlsx"))

dfList = []

for file in generalFiles:
    df = pd.read_excel(file)
    dfList.append(df)

generalDf = pd.concat(dfList, axis=0, ignore_index=True)

generalDf.to_csv('output/2021_special_generals.csv')

# Set up Primary Election CSV

# To run this elsewhere, please make sure this path makes sense
primaryPath = r'data/2021SpecialPrimaries/'

primaryFiles = glob.glob(os.path.join(primaryPath, "*.xlsx"))

dfList = []

for file in primaryFiles:
    df = pd.read_excel(file)
    dfList.append(df)

primaryDf = pd.concat(dfList, axis=0, ignore_index=True)

primaryDf.to_csv('output/2021_special_primaries.csv')

# Find Duplicates
elections = {'2021_special_primaries.csv': primaryDf, '2021_special_generals.csv': generalDf}

for dataset, election in elections.items():
    duplicates = election[election.duplicated('VOTER ID')]
    if duplicates.empty:
        print('No Duplicates Found in {}!'.format(dataset))
    else:
        print('Duplicates Found in {}!'.format(dataset))
        print(duplicates)