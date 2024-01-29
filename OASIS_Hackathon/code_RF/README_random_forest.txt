> Random Forest Regression for Player RPE Prediction
This code implements a Random Forest Regression model to predict Rating of Perceived Exertion (RPE) for players using training and testing datasets. The code performs the following tasks:

> Data Loading and Preprocessing:
Load training and testing datasets from CSV files.
Handle missing values by filling NaN with zeros.
Optional: Drop rows with NaN values.
Identify and handle '#DIV/0!' entries.
Extract unique player IDs from the dataset.

> Stratified Cross-Validation:
Iterate through each player in the dataset.
Perform stratified k-fold cross-validation (k=5) using Random Forest Regression.
Calculate and store the mean absolute error (MAE) for each player.

> Testing on Full Dataset:
Load separate training and testing datasets.
Train a Random Forest Regression model on the training data.
Make predictions on the testing data.
Calculate and print the MAE for the entire dataset.

> Training by Player:
Iterate through each player in the training dataset.
Train a Random Forest Regression model specific to each player.
Make predictions on the corresponding testing data.
Calculate and store the MAE for each player.

> Results:
Print the overall mean MAE for predictions made player by player.

Note: The code assumes that the CSV files are in the specified paths, and you may need to adjust these paths based on your directory structure.