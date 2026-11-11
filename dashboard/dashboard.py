import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set judul halaman
st.set_page_config(page_title="E-commerce Analysis Dashboard", layout="wide")
st.title("Analisis Data E-commerce")

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    customers = pd.read_csv("data/customers_dataset.csv")
    geolocation = pd.read_csv("data/geolocation_dataset.csv")
    products = pd.read_csv("data/products_dataset.csv")
    return customers, geolocation, products

# Memuat data
customers, geolocation, products = load_data()

# Sidebar untuk kontrol
st.sidebar.header("Pengaturan Analisis")
analysis_type = st.sidebar.selectbox(
    "Pilih Jenis Analisis",
    ["Distribusi Pelanggan", "Karakteristik Produk"]
)

# --- Fitur Interaktif Tambahan ---
if analysis_type == "Distribusi Pelanggan":
    # Filter interaktif berdasarkan kota
    unique_cities = sorted(customers['customer_city'].unique())
    selected_cities = st.sidebar.multiselect(
        "Pilih Kota (kosongkan untuk semua)",
        options=unique_cities,
        default=unique_cities
    )
    # Filter data pelanggan berdasarkan kota yang dipilih
    filtered_customers = customers[customers['customer_city'].isin(selected_cities)]
else:
    filtered_customers = customers.copy()

if analysis_type == "Karakteristik Produk":
    # Menentukan rentang berat produk
    min_weight = int(products['product_weight_g'].min())
    max_weight = int(products['product_weight_g'].max())
    weight_range = st.sidebar.slider(
        "Pilih Rentang Berat Produk (gram)",
        min_value=min_weight,
        max_value=max_weight,
        value=(min_weight, max_weight)
    )
    # Filter data produk berdasarkan berat
    filtered_products = products[(products['product_weight_g'] >= weight_range[0]) &
                                   (products['product_weight_g'] <= weight_range[1])]
else:
    filtered_products = products.copy()

# Tab untuk analisis
tab1, tab2 = st.tabs(["📊 Visualisasi & EDA", "📈 Data Mentah"])

with tab1:
    if analysis_type == "Distribusi Pelanggan":
        st.header("Analisis Distribusi Pelanggan")
        
        # Tampilkan statistik dasar dari data pelanggan terfilter
        st.subheader("Statistik Dasar Pelanggan")
        st.write(filtered_customers.describe(include='all'))
        
        # Agregasi data: Jumlah Pelanggan per Kota
        st.subheader("Jumlah Pelanggan per Kota")
        city_counts = filtered_customers['customer_city'].value_counts().reset_index()
        city_counts.columns = ['Kota', 'Jumlah Pelanggan']
        st.dataframe(city_counts)
        
        # Visualisasi Top 10 Kota
        plt.figure(figsize=(10, 6))
        top_cities = filtered_customers['customer_city'].value_counts().head(10)
        sns.barplot(x=top_cities.values, y=top_cities.index, palette="viridis")
        plt.title('Top 10 Kota dengan Jumlah Pelanggan Terbanyak')
        plt.xlabel('Jumlah Pelanggan')
        plt.ylabel('Kota')
        st.pyplot(plt)
        
        # Peta Geolokasi (menggunakan sampel data geolocation)
        st.subheader("Distribusi Geografis Pelanggan")
        # Asumsikan geolocation merupakan data lokasi pelanggan
        st.map(geolocation.sample(1000).rename(columns={
            'geolocation_lat': 'latitude', 
            'geolocation_lng': 'longitude'
        }))
        
    elif analysis_type == "Karakteristik Produk":
        st.header("Analisis Karakteristik Produk")
        
        # Tampilkan statistik dasar dari data produk terfilter
        st.subheader("Statistik Dasar Produk")
        st.write(filtered_products.describe())
        
        # Visualisasi Distribusi Berat Produk
        plt.figure(figsize=(10, 6))
        sns.histplot(filtered_products['product_weight_g'].dropna(), bins=30, kde=True)
        plt.title('Distribusi Berat Produk (gram)')
        plt.xlabel('Berat (gram)')
        plt.ylabel('Frekuensi')
        st.pyplot(plt)

        # Visualisasi Distribusi Dimensi Produk
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        sns.histplot(filtered_products['product_length_cm'].dropna(), bins=30, ax=axes[0, 0], kde=True)
        sns.histplot(filtered_products['product_height_cm'].dropna(), bins=30, ax=axes[0, 1], kde=True)
        sns.histplot(filtered_products['product_width_cm'].dropna(), bins=30, ax=axes[1, 0], kde=True)
        
        axes[0, 0].set_title('Panjang Produk (cm)')
        axes[0, 1].set_title('Tinggi Produk (cm)')
        axes[1, 0].set_title('Lebar Produk (cm)')
        # Sisakan subplot ke-4 untuk informasi tambahan, misalnya korelasi antar dimensi
        corr = filtered_products[['product_length_cm', 'product_height_cm', 'product_width_cm']].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=axes[1, 1])
        axes[1, 1].set_title('Korelasi Dimensi Produk')
        plt.tight_layout()
        st.pyplot(fig)

with tab2:
    if analysis_type == "Distribusi Pelanggan":
        st.subheader("Data Pelanggan")
        st.dataframe(filtered_customers.head(10))
        
        st.subheader("Data Geolokasi")
        st.dataframe(geolocation.head(10))
    
    elif analysis_type == "Karakteristik Produk":
        st.subheader("Data Produk")
        st.dataframe(filtered_products.head(10))

# Menambahkan penjelasan di sidebar
st.sidebar.markdown("---")
st.sidebar.info(
    "Dashboard ini menampilkan analisis data e-commerce Brazil mencakup:\n"
    "- Distribusi geografis dan statistik pelanggan\n"
    "- Karakteristik produk dan analisis korelasinya\n"
    "- Data mentah dan agregasi untuk mendukung insight bisnis\n\n"
    "Fitur interaktif memungkinkan pengguna untuk memfilter data berdasarkan kota (untuk pelanggan) atau berat produk."
)
