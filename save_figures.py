import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

os.makedirs('outputs', exist_ok=True)

ep = ExecutePreprocessor(timeout=1200, kernel_name='python3')

notebooks = [
    'WORK STATION FOR DESCRIPTIVE ANALYSIS.ipynb',
    'WORK STATION FOR MACHINE LEARNING.ipynb', 
]

for nb_path in notebooks:
    print(f'Running {nb_path}...')
    with open(nb_path) as f:
        nb = nbformat.read(f, as_version=4)
    ep.preprocess(nb, {'metadata': {'path': '.'}})  
    with open(nb_path, 'w') as f:
        nbformat.write(nb, f)
    print(f'Done: {nb_path}')

print('All notebooks executed.')