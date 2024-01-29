from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, confusion_matrix
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold, cross_val_score
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# # Charger les données d'entraînement et de test à partir des fichiers CSV
# df = pd.read_csv("/home/docker/code/old_data/old_jm/dataset_player.csv")
# print("len(df):", len(df))

# df.fillna(0, inplace=True)

# print((df == '#DIV/0!').any().any())
# print(np.where(df == '#DIV/0!'))

# # df = df.dropna()
# # print("len(df without na):", len(df))

# list_players = df["player_id"].unique()
# print("list_players:", list_players)

# list_mae = []

# ### Stratified cross validation

# for player_id in list_players :

#     df_player = df[df["player_id"] == player_id]
#     # print("len(df_player):", len(df_player))

#     X = df_player.drop(["player_id", "RPE"], axis=1)
#     y = df_player["RPE"]
#     print(X)
#     print(y)

#     stratified_kfold = KFold(n_splits=5, shuffle=True, random_state=42)

#     random_forest = RandomForestRegressor(n_estimators=100, random_state=42)

#     scores = -cross_val_score(random_forest, X, y, cv=stratified_kfold, scoring='neg_mean_absolute_error')
#     print("scores:", scores)

#     list_mae.append(scores.mean())

# print(list_mae)
# print(np.mean(list_mae))

### Test sur tout

train = pd.read_csv("code_RF/dataset_rf_train")
test = pd.read_csv("code_RF/dataset_rf_test")

X_train = train.drop(["RPE", "n_date"], axis=1)
y_train = train["RPE"]
X_test = test.drop(["RPE", "n_date"], axis=1)
y_test = test["RPE"]

random_forest = RandomForestRegressor(n_estimators=100, random_state=42)

random_forest.fit(X_train, y_train)

y_pred = random_forest.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)

print("MAE full:", mae)


### Training by player

list_players = train["player_id"].unique()
# print("list_players:", list_players)

list_mae = []

for player_id in list_players :

    train_player = train[train["player_id"] == player_id]
    test_player = test[test["player_id"] == player_id]

    X_train = train_player.drop(["player_id", "RPE", "n_date"], axis=1)
    y_train = train_player["RPE"]
    X_test = test_player.drop(["player_id", "RPE", "n_date"], axis=1)
    y_test = test_player["RPE"]

    random_forest = RandomForestRegressor(n_estimators=100, random_state=42)

    random_forest.fit(X_train, y_train)

    y_pred = random_forest.predict(X_test)

    list_mae.append(mean_absolute_error(y_test, y_pred))

# print(list_mae)
print("MAE player by player:", np.mean(list_mae))