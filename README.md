# DSC180A-Methodology-5

Learn bias mitigation techniques using the Medical Expenditure data

# run.py

Runs scripts that retrieves dataset, extracts/creates features, trains various models with bias mitigation, and create visualizations based on the results.

## notebooks/

Contains holistic .ipynb that was used to replicate a bias mitigation project and explore our own bias mitigation techniques using an open-source healthcare dataset.

## references/

## src/

### data/

Contains data preprocessing script that includes renaming features, handling null values, and quantizing continuous features.

### features/

Contains feature creation script that includes converting features to one-hot encodings.

### models/

Contains modeling script that trains various of models (including logistic regression, random forrest) with and without bias mitigation techniques (including reweighing and prejudice remover).

### visualizations/

Creates correlation plots (including race vs insurance and age vs diseases) as well as model drift using the evaluation metrics from models/ between two datasets.

## test/

### out/

Output after running data preprocessing and feature creation.

### results/

#### metrics/

Metrics after training various models on the dataset.

#### visualizations/

Plots created after running visualization script.

### testdata/

Test dataset sampled from larger Medical Expenditure Data.
