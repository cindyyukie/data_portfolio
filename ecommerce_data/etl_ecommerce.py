import os
import pandas as pd

# Definir caminho dos arquivos
DATA_PATH = "ecommerce_data"

# 1️⃣ Extração - Carregar os datasets
def load_data(file_name):
    file_path = os.path.join(DATA_PATH, file_name)
    return pd.read_csv(file_path)

# 2️⃣ Transformação - Ajustes nos dados
def transform_data(df):
    date_columns = [
        "order_purchase_timestamp", "order_approved_at", 
        "order_delivered_carrier_date", "order_delivered_customer_date", 
        "order_estimated_delivery_date"
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    # Criar nova coluna: tempo de entrega em dias
    df["delivery_time_days"] = (df["order_delivered_customer_date"] - df["order_purchase_timestamp"]).dt.days

    return df

# 3️⃣ Carga - Salvar os dados transformados
def save_data(df, output_file):
    output_path = os.path.join(DATA_PATH, output_file)
    df.to_csv(output_path, index=False)
    print(f"✅ Dados transformados salvos em: {output_path}")

# 🚀 Executar o pipeline ETL
if __name__ == "__main__":
    print("🔄 Iniciando pipeline ETL...")
    
    df_orders = load_data("olist_orders_dataset.csv")
    df_orders = transform_data(df_orders)
    
    print("\n📌 Primeiras linhas dos dados transformados:")
    print(df_orders.head())

    print("\n📌 Valores nulos por coluna:")
    print(df_orders.isnull().sum())

    save_data(df_orders, "orders_transformed.csv")