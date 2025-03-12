import pandas as pd
import os

# Definir o caminho da pasta onde os arquivos CSV estão armazenados
data_path = "/Users/cindydelvalle/Projects/data_portfolio/ecommerce_data/"

# Listar arquivos disponíveis na pasta
arquivos = os.listdir(data_path)
print("📂 Arquivos disponíveis:", arquivos)

# Carregar o dataset de pedidos (olist_orders_dataset.csv)
df_orders = pd.read_csv(os.path.join(data_path, "olist_orders_dataset.csv"))

# Exibir as primeira linhas do dataset
print("\n📌 Primeiras linhas do dataset de pedidos:")
print(df_orders.head())

# Exibir informações sobre o dataset
print("\n📊 Informações sobre o dataset:")
print(df_orders.info())