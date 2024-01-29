I- Importations
This section includes the necessary imports of Python libraries for data manipulation and analysis,
such as pandas, os, and datetime.

II- Import our CSV
This part of the notebook imports required CSV files from the specified directory,
including data related to anthropometrics, meteorological conditions, player information, catapult data,
and rpe data.

III- Work on Data_anthropo
In this section, the notebook converts the 'n_date' column to datetime objects and extracts only
the date component.

IV- Work on Meteo_data
A new function is created to differentiate between morning and afternoon
based on the time of day. The 'preprocess_meteo' function is then applied to process meteorological data.

V- Work on Catapult_data
Several functions are defined to preprocess catapult data, including concatenating CSV files,
calculating heart rate features, and formatting time columns. The resulting processed catapult data is
then grouped by date, AM/PM, and catapult ID.

VI- Merging
This section merges the processed datasets, including anthropometric, meteorological, and catapult data,
with the final training data. The resulting dataset is further processed, and columns are dropped or filled
as needed.

VII- Save Processed Data
The final processed data is saved to CSV files for further analysis and model training.
Two versions of the dataset are saved: one with basic features and another with additional features
that include the previous 5 RPE values.