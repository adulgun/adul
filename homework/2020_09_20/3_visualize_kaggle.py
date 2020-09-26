# 22p21i0098-อดุลวิทย์
# https://github.com/adulgun/adul

import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
fifa_filepath = "fifa.csv"
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)
print(fifa_data.head())
print(list(fifa_data.columns))

sns.lineplot(data=fifa_data)
plt.show()

sns.barplot(x=fifa_data.index, y=fifa_data['BRA'])
plt.show()

sns.heatmap(data=fifa_data, annot=True)
plt.xlabel("1993-08-08")
plt.show()

sns.scatterplot(x=fifa_data['ARG'], y=fifa_data['BRA'])
sns.regplot(x=fifa_data['ARG'], y=fifa_data['BRA'])
plt.show()

sns.kdeplot(data=fifa_data['ARG'], shade=True)
plt.show()

sns.jointplot(x=fifa_data['ARG'], y=fifa_data['BRA'], kind="kde")
plt.show()

sns.distplot(a=fifa_data['ARG'], label="ARG", kde=False)
sns.distplot(a=fifa_data['BRA'], label="BRA", kde=False)
sns.distplot(a=fifa_data['ESP'], label="ESP", kde=False)
plt.show()

sns.kdeplot(data=fifa_data['ARG'], label="ARG", shade=True)
sns.kdeplot(data=fifa_data['BRA'], label="BRA", shade=True)
sns.kdeplot(data=fifa_data['ESP'], label="ESP", shade=True)
plt.show()