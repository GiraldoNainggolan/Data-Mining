# 1. Jawaban Nomor 1

import pandas as pd

# Membuat DataFrame
data = {
    "total_bill": [20.5, 30.25, 40.75],
    "tip": [5.0, 7.5, 8.25],
    "sex": ["Male", "Female", "Male"],
    "smoker": ["Yes", "No", "No"],
    "day": ["Sun", "Sat", "Sun"],
    "time": ["Dinner", "Dinner", "Lunch"],
    "size": [2, 3, 2],
}

df = pd.DataFrame(data)

# Memperbaiki tipe data variabel
df["sex"] = df["sex"].astype("category")
df["smoker"] = df["smoker"].astype("category")
df["day"] = df["day"].astype("category")
df["time"] = df["time"].astype("category")
df["size"] = df["size"].astype("uint8")

# Menampilkan tipe data setelah perbaikan
print("Tipe variabel setelah perbaikan:")
print(df.dtypes)

# Jawaban Nomor 2
plt.figure(figsize=(10, 8))
sns.boxplot(data=df[["total_bill", "tip"]])
plt.title("Box Plot untuk Melihat Outlier")
plt.xlabel("Variabel")
plt.ylabel("Value")
plt.show()

# Cek missing values
print("Missing values:")
print(df.isnull().sum())

# Cek duplikasi data
print("Duplikasi data:")
print(df.duplicated().sum())

import pandas as pd

# Membuat DataFrame
data = {
    "total_bill": [20.5, 30.25, 40.75],
    "tip": [5.0, 7.5, 8.25],
    "sex": ["Male", "Female", "Male"],
    "smoker": ["Yes", "No", "No"],
    "day": ["Sun", "Sat", "Sun"],
    "time": ["Dinner", "Dinner", "Lunch"],
    "size": [2, 3, 2],
}

df = pd.DataFrame(data)

# Memperbaiki tipe data variabel
df["sex"] = df["sex"].astype("category")
df["smoker"] = df["smoker"].astype("category")
df["day"] = df["day"].astype("category")
df["time"] = df["time"].astype("category")
df["size"] = df["size"].astype("uint8")

# Menampilkan tipe data setelah perbaikan
print("Tipe variabel setelah perbaikan:")
print(df.dtypes)

# 3. Jawaban nomor 2
plt.figure(figsize=(10, 8))
sns.boxplot(data=df[["total_bill", "tip"]])
plt.title("Box Plot untuk Melihat Outlier")
plt.xlabel("Variabel")
plt.ylabel("Value")
plt.show()

# Cek missing values
print("Missing values:")
print(df.isnull().sum())

# Cek duplikasi data
print("Duplikasi data:")
print(df.duplicated().sum())

# 5. Jawaban Nomor 5
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="sex")
plt.title("Perbandingan Proporsi Pelanggan Pria dan Wanita")
plt.xlabel("Sex (0=Male, 1=Female)")
plt.ylabel("Count")
plt.show()

# 6. Jawaban nomor 6
print("Rata-rata tips berdasarkan hari:")
print(df.groupby("day")["tip"].mean())


# 7. Jawaban nomor 7
print("Rata-rata tips berdasarkan status perokok:")
print(df.groupby("smoker")["tip"].mean())

# 8. Jawaban nomor 8
print("Rata-rata tips berdasarkan jenis kelamin dan hari:")
print(df.groupby(["sex", "day"])["tip"].mean())

# 9. Jawaban nomor 9
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x="total_bill", y="tip")
plt.title("Hubungan antara Total Bill dan Tip")
plt.xlabel("Total Bill (US dollars)")
plt.ylabel("Tip (US dollars)")
plt.show()

# 10. Jawaban nomor 10
# Membuat DataFrame contoh
data = {
    'total_bill': [20.5, 30.25, 40.75, 25.50, 35.00],
    'tip': [5.0, 7.5, 8.25, 4.0, 5.5],
    'day': ['Sun', 'Sat', 'Sun', 'Sat', 'Sun']
}

df = pd.DataFrame(data)

# Menghitung rata-rata tips per hari
avg_tips_per_day = df.groupby('day')['tip'].mean()

# Menampilkan rata-rata tips per hari
print("Rata-rata tips per hari:")
print(avg_tips_per_day)

# Menemukan hari dengan rata-rata tips terendah
min_avg_tip_day = avg_tips_per_day.idxmin()

print("\nHari dengan rata-rata tips terendah:", min_avg_tip_day)

# Menyusun rekomendasi
print("\nRekomendasi: Peningkatan pelayanan disarankan pada hari", min_avg_tip_day)

# 11. Jawaban nomor 11
# Membuat DataFrame contoh
data = {
    'total_bill': [20.5, 30.25, 40.75, 25.50, 35.00],
    'tip': [5.0, 7.5, 8.25, 4.0, 5.5],
    'day': ['Sun', 'Sat', 'Sun', 'Sat', 'Sun']
}

df = pd.DataFrame(data)

# Analisis deskriptif
descriptive_stats = df.describe()
print("Statistik Deskriptif:")
print(descriptive_stats)

# Visualisasi data: Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='tip', data=df)
plt.title('Boxplot of Tips by Day')
plt.xlabel('Day')
plt.ylabel('Tip')
plt.show()

# Komunikasi hasil analisis
min_tip_day = df.groupby('day')['tip'].mean().idxmin()
print("\nBerdasarkan analisis, rata-rata tips terendah adalah pada hari", min_tip_day)
print("Sebaiknya dilakukan peningkatan pelayanan pada hari tersebut.")