# FatigueNet model implementation

This code_FN folder contains 4 files and 1 folder :

- preprocess_JM_data.ipynb
    - Merging and normalization datasets 
    - Split by player_id
    - Remove inconsistent date data

- preprocess_catapult_data.ipynb
    - Adding session id to raw catapult data
    - Process catapult data
        1. Concatenating all data per player
        2. Cleaning Hear rate feature
        3. Split concatenated dataset by player
        4. Split each player dataset by session
        5. Get max session length for each player
        6. Pad and normalize session

- fatigue_net_model.ipynb
    - implementing the FatigueNet model
    - training and testing

- data folder
    - training data
    - test data

STEPS:
> put code_FN in the same file as data (the given ones)
> run preprocess_JM_data.ipynb to pre-process Player-Weather data (JM data)
> run preprocess_catapult_data.ipynb to pre-process catapult data
> run fatigue_net_model.ipynb to train our deep learning model and test it

As we split catapult data by session, and not by AM/PM each day, we couldn't use the evaluate_predictions.py script. Also, as some date were not in both catapult and JM data, these data have been remove.