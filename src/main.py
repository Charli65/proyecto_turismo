import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_PATH = os.path.join("data", "turistas.csv")

def cargar_datos():
    try:
        df = pd.read_csv(DATA_PATH)
        print("✅ Datos cargados correctamente")
        return df
    except FileNotFoundError:
        print("⚠️ No se encontró dataset. Creando dataset simulado...")
        data = {
            "anio": [2021, 2021, 2022, 2022],
            "ciudad": ["Asunción", "Encarnación", "Ciudad del Este", "Asunción"],
            "tipo_turismo": ["Cultural", "Compras", "Receptivo", "Compras"],
            "visitantes": [15000, 32000, 18000, 25000],
            "gasto_promedio": [250, 300, 270, 350]
        }
        df = pd.DataFrame(data)
        os.makedirs("data", exist_ok=True)
        df.to_csv(DATA_PATH, index=False)
        print("✅ Dataset simulado guardado en data/turistas.csv")
        return df

def visualizar_datos(df):
    plt.figure(figsize=(8, 5))
    sns.barplot(x="tipo_turismo", y="visitantes", data=df, estimator=sum, ci=None)
    plt.title("Turistas por tipo de turismo en Paraguay")
    plt.savefig("outputs/visita_turismo.png")
    plt.show()

if __name__ == "__main__":
    df = cargar_datos()
    print(df.head())
    os.makedirs("outputs", exist_ok=True)
    visualizar_datos(df)
