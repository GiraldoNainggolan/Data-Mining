import pandas as pd

# Membaca dataset
restaurant_data = pd.read_csv("tips.csv")

# 1. Cek tipe variabel
print("1. Tipe variabel:")
print(restaurant_data.dtypes)
print()

# 2. Distribusi normal
print("2. Distribusi normal:")
print(restaurant_data.describe())
print()

# 3. Cek outlier, noise, missing values, dan duplikasi data
print("3. Penanganan data:")
print("Jumlah missing values:")
print(restaurant_data.isnull().sum())
print()

print("Jumlah duplikasi data:")
print(restaurant_data.duplicated().sum())
print()

# 4. Proporsi pelanggan pria dan wanita
print("4. Proporsi pelanggan pria dan wanita:")
sex_counts = restaurant_data["sex"].value_counts()
print(sex_counts)
print()

# 5. Kecenderungan tips lebih besar untuk pria atau wanita
print("5. Kecenderungan tips lebih besar untuk pria atau wanita:")
tips_by_sex = restaurant_data.groupby("sex")["tip"].mean()
print(tips_by_sex)
print()

# 6. Kecenderungan tips lebih besar di hari-hari tertentu
print("6. Kecenderungan tips lebih besar di hari-hari tertentu:")
tips_by_day = restaurant_data.groupby("day")["tip"].mean()
print(tips_by_day)
print()

# 7. Kecenderungan tips lebih besar dari pelanggan perokok atau bukan
print("7. Kecenderungan tips lebih besar dari pelanggan perokok atau bukan:")
tips_by_smoker = restaurant_data.groupby("smoker")["tip"].mean()
print(tips_by_smoker)
print()

# 8. Pengaruh hari pada kecenderungan tips
print("8. Pengaruh hari pada kecenderungan tips:")
tips_by_sex_day = restaurant_data.groupby(["sex", "day"])["tip"].mean()
print(tips_by_sex_day)
print()

tips_by_smoker_day = restaurant_data.groupby(["smoker", "day"])["tip"].mean()
print(tips_by_smoker_day)
print()

# 9. Pola lain yang dapat ditemukan
print("9. Pola lain yang dapat ditemukan:")
size_vs_total_bill = restaurant_data.groupby("size")["total_bill", "tip"].mean()
print(size_vs_total_bill)
print()

# 10. Saran untuk pemilik restoran
print("10. Saran untuk pemilik restoran:")
print(
    "Berdasarkan analisis, saran dapat berupa menyesuaikan harga makanan atau menawarkan promosi pada hari-hari tertentu serta menyesuaikan staf pelayanan berdasarkan kecenderungan pelanggan."
)
print()

# 11. Skills/kompetensi yang diperlukan
print("11. Skills/kompetensi yang diperlukan:")
print(
    "Pemahaman statistik deskriptif, penggunaan alat visualisasi data, dan kemampuan interpretasi untuk membuat rekomendasi bisnis."
)
