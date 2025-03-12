import pandas as pd
import os

# Definir o caminho da pasta onde os arquivos CSV estão armazenados
data_path = "/Users/cindydelvalle/Projects/data_portfolio/ecommerce_data/"

# Listar arquivos disponíveis na pasta
arquivos = os.listdir(data_path)
print("📂 Arquivos disponíveis:", arquivos)

# Carregar o dataset de pedidos (olist_orders_dataset.csv)
df_orders = pd.read_csv(os.path.join(data_path, "olist_orders_dataset.csv"))

# Converter colunas de data para datetime
date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    df_orders[col] = pd.to_datetime(df_orders[col])

# Verificar valores nulos
missing_values = df_orders.isnull().sum()

# Criar nova coluna com o tempo de entrega (dias)
df_orders["delivery_time_days"] = (df_orders["order_delivered_customer_date"] - df_orders["order_purchase_timestamp"]).dt.days

# Exibir resumo dos dados transformados
print("\n📌 Dados Transformados:")
print(df_orders.head())
print("\n📊 Valores Nulos por coluna:")
print(missing_values)