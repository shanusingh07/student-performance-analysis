import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("studentsdata.csv")

print(df)

avg = df[["Math","Science","English"]].mean()
print(avg)

avg.plot(kind="bar")

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()