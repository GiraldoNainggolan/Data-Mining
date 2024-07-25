import pandas as pd

# Membaca dataset
restaurant_data = pd.read_csv("restaurant_data.csv")

# Menampilkan informasi singkat tentang dataset
print("Informasi Dataset:")
print(restaurant_data.info())

# Menampilkan statistik deskriptif dari data numerik
print("\nStatistik Deskriptif:")
print(restaurant_data.describe())

# Menampilkan 5 baris pertama dari dataset
print("\n5 Baris Pertama dari Dataset:")
print(restaurant_data.head())

# Menghitung rata-rata total bill
rata_total_bill = restaurant_data['total_bill'].mean()
print("\nRata-rata Total Bill: ${:.2f}".format(rata_total_bill))

# Menghitung
