import pandas as pd

# Membaca dataset
restaurant_data = pd.read_csv('restaurant_data.csv')

# 1. Cek tipe variabel
print(restaurant_data.dtypes)

# 2. Distribusi normal
print(restaurant_data.describe())

# 3. Cek outlier, noise, missing values, dan duplikasi data
print("Jumlah missing values:")
print(restaurant_data.isnull().sum())

print("Jumlah duplikasi data:")
print(restaurant_data.duplicated().sum())

# 4. Proporsi pelanggan pria dan wanita
sex_counts = restaurant_data['sex'].value_counts()
print("Proporsi pelanggan pria dan wanita:")
print(sex_counts)

# 5. Kecenderungan tips lebih besar untuk pria atau wanita
tips_by_sex = restaurant_data.groupby('sex')['tip'].mean()
print("Rata-rata tips:")
print(tips_by_sex)

# 6. Kecenderungan tips lebih besar di hari-hari tertentu
tips_by_day = restaurant_data.groupby('day')['tip'].mean()
print("Rata-rata tips per hari:")
print(tips_by_day)

# 7. Kecenderungan tips lebih besar dari pelanggan perokok atau bukan
tips_by_smoker = restaurant_data.groupby('smoker')['tip'].mean()
print("Rata-rata tips dari perokok dan bukan perokok:")
print(tips_by_smoker)

# 8. Pengaruh hari pada kecenderungan tips
tips_by_sex_day = restaurant_data.groupby(['sex', 'day'])['tip'].mean()
print("Rata-rata tips dari pelanggan pria/wanita per hari:")
print(tips_by_sex_day)

tips_by_smoker_day = restaurant_data.groupby(['smoker', 'day'])['tip'].mean()
print("Rata-rata tips dari pelanggan perokok/bukan perokok per hari:")
print(tips_by_smoker_day)

# 9. Pola lain yang dapat ditemukan
# Misal, hubungan antara ukuran kelompok (size) dan total bill atau tips
size_vs_total_bill = restaurant_data.groupby('size')['total_bill', 'tip'].mean()
print("Rata-rata total bill dan tips berdasarkan ukuran kelompok:")
print(size_vs_total_bill)

# 10. Saran untuk pemilik restoran
# Berdasarkan analisis, saran dapat berupa menyesuaikan harga makanan atau menawarkan promosi pada hari-hari tertentu
# serta menyesuaikan staf pelayanan berdasarkan kecenderungan pelanggan.

# 11. Skills/kompetensi yang diperlukan
# Pemahaman statistik deskriptif, penggunaan alat visualisasi data, dan kemampuan interpretasi untuk membuat rekomendasi bisnis.
