import pandas as pd
df = pd.read_csv("project_data.csv")
df = df[["customer_id","year_of_birth","educational_level","marital_status","annual_income"]]
df_1=df.educational_level.value_counts()
print(df_1)
df = df.sort_values(by="annual_income",ascending=False)
df = df.dropna()
df_2 =df.annual_income
print("HEAD_2\n",df_2.head(20))
print("TAIL_2\n",df_2.tail())
df_3 = df.loc[ (df["year_of_birth"]>1960) & (df["annual_income"]>50000) ]
print(df_3[["customer_id","year_of_birth","annual_income"]])
df_4 = pd.merge(df_2,df_3,on="annual_income")
print("TASK 4:",df_4)
#KetHon or DaLyHon: Married or Divorced ==> marital_status
df_5 = df[["customer_id","marital_status"]]
df_5 = df_5.loc[(df["marital_status"] == "Married") | (df["marital_status"] == "Divorced")]
print(df_5)
df_6 = df[["educational_level","annual_income"]]
print(df_6.groupby(by = "educational_level").mean("annual_income"))
#task_7
df_7 = df[["educational_level","annual_income","marital_status"]]
print(df_7.groupby(["educational_level","marital_status"]).mean("annual_income"))
#task_8
print(df)
# khach hang tap trung o phan khuc graduation(257)>phd(114)>master(81)>high_school(40)>basic(7)
# thu nhap cua khach hang nhin chung dao dong tu 2447-->157243
# co 206/486 khach hang sn 1960 co muc thu nhap 50,000$/y ==> khach hang co thu nhap tuong doi tot