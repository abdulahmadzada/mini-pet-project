import pandas as pd 
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score

df = pd.read_csv(r"C:\Users\WINNER\Desktop\New_python\real_estate_dataset.csv")
X = df.loc[:, "Square_Feet":"Distance_to_Center"]
y = df["Price"]
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42,train_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

r2_test = r2_score(y_test_pred, y_test)
r2_train = r2_score(y_train_pred, y_train)

cv_r2 = cross_val_score(model, X, y, cv=5, scoring="r2")

joblib.dump(model, "linear_model.pkl")

print(f"значение test: {r2}")
print(f"значение train: {r1}")
print(f"cross-validation: {cv_r2}")