import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([2, 4, 6, 8, 10])
print(s)


# Serie object creation initialized with a dictionary
height = {"Santiago": 180, "Pedro": 170, "Juan": 160, "Maria": 150, "Ana": 140}
result = pd.Series(height)

print(result)
print()

"""
Creación de un objeto series inicializándolo con algunos
de los elementos de un diccionario de python
"""
height = {"Santiago": 180, "Marcelo": 172, "Luis": 174, "Alejandra": 160}
s = pd.Series(height, index=["Marcelo", "Luis"])
print(s)


# Serie object creation inizialized with a scalar
s = pd.Series(34, ["test1", "test2", "test3"])
print(s)

# Custom index in Series
s = pd.Series([2, 4, 6, 8], index=["num1", "num2", "num3", "num4"])
print(s["num3"])


# Dataframe object creation
people = {
    "weight": pd.Series([65, 70, 75, 80], ["Santiago", "Pedro", "Juan", "Maria"]),
    "height": pd.Series({"Santiago": 180, "Pedro": 170, "Juan": 160, "Maria": 150}),
    "children": pd.Series([2, 3], ["Santiago", "Pedro"]),
}


# object serie with temperatures and matplotlib
temperatures = pd.Series([4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.2, 4.7, 4.1, 3.9])
s = pd.Series(temperatures, name="Temperatures")
print(s)
s.plot()
# plt.show()

df = pd.DataFrame(people)
print(df)

df = pd.DataFrame(
    people, columns=["weight", "height"], index=["Santiago", "Pedro", "Juan"]
)
print(df)

# methods combination
print()
df2 = (df["weight"] >= 60) & (df["weight"] < 80)
print(df2)

print(df.iloc[1:3])

# advanced consults in pandas
print()
df3 = df.query("height > 150 and  weight > 70")
print(df3)

# dataframe copy
df_copy = df.copy()
print(df_copy)

# add new column to dataframe
df_copy["birthday"] = [1990, 1991, 1992]
print(df_copy)
print()

# column calculated
df_copy["age"] = 2025 - df_copy["birthday"]
print(df_copy)
print()

# new column creating a new dataframe
df_modified = df_copy.assign(pets=[1, 3, 0])
print(df_modified)
