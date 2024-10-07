# Import Libraries
import os
import pandas as pd
import numpy as np

DATASETURL = 'https://gitlab.com/aelluminate/databank/databank/-/raw/main/2024-10/breast-cancer-cells/cell-samples.csv'

#Load the data
cells = pd.read_csv(DATASETURL)

# Separation of classes
benign = cells[cells['Class'] == 2]
malignant = cells[cells['Class'] == 4]

# Type Conversion
cells['BareNuc'] = pd.to_numeric(cells['BareNuc'], errors='coerce')

# Drop Rows
cells = cells.dropna(subset=['BareNuc'])

# Convert to integer
cells['BareNuc'] = cells['BareNuc'].astype('int')

print(cells.info())

# Save the preprocessed data
directory = 'datasets'

if not os.path.exists(directory):
    os.makedirs(directory)

filepath = os.path.join(directory, 'preprocessed.csv')

cells.to_csv(filepath, index=False)

if os.path.exists(filepath):
    print('Did not save.')