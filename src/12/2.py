import numpy as np
import pandas as pd

# 1
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])

print(ds1 == ds2)


# 2
exam_data = {
    "name": [
        *["Anastasia", "Dima", "Katherine", "James", "Emily"],
        *["Michael", "Matthew", "Laura", "Kevin", "Jonas"],
    ],
    "score": [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    "attempts": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    "qualify": ["yes", "no", "yes", "no", "no", "yes", "yes", "no", "no", "yes"],
}

labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(exam_data, index=labels)
print(df)


# 3
df_three_rows = df.loc["a":"c"]
print(df_three_rows)


assert (
    str(df_three_rows)
    == "        name  score  attempts qualify\na  Anastasia   12.5         1     yes\nb       Dima    9.0         3      no\nc  Katherine   16.5         2     yes"
)


# 4
color = [
    *["Red", "Blue", "Orange"],
    *["Red", "White", "White"],
    *["Blue", "Green", "Green", "Red"],
]
df["color"] = color
print(df)


assert (
    str(df)
    == "        name  score  attempts qualify   color\na  Anastasia   12.5         1     yes     Red\nb       Dima    9.0         3      no    Blue\nc  Katherine   16.5         2     yes  Orange\nd      James    NaN         3      no     Red\ne      Emily    9.0         2      no   White\nf    Michael   20.0         3     yes   White\ng    Matthew   14.5         1     yes    Blue\nh      Laura    NaN         1      no   Green\ni      Kevin    8.0         2      no   Green\nj      Jonas   19.0         1     yes     Red"
)


# 5
df_new_order = df[["color", "score", "attempts", "name", "qualify"]]
print(df_new_order)

assert (
    str(df_new_order)
    == "    color  score  attempts       name qualify\na     Red   12.5         1  Anastasia     yes\nb    Blue    9.0         3       Dima      no\nc  Orange   16.5         2  Katherine     yes\nd     Red    NaN         3      James      no\ne   White    9.0         2      Emily      no\nf   White   20.0         3    Michael     yes\ng    Blue   14.5         1    Matthew     yes\nh   Green    NaN         1      Laura      no\ni   Green    8.0         2      Kevin      no\nj     Red   19.0         1      Jonas     yes"
)
