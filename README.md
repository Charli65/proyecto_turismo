# Proyecto de Planificación Turística en Paraguay

Este proyecto analiza y visualiza datos turísticos de Paraguay para tres categorías:

- turismo receptivo;
- turismo cultural;
- turismo de compras.

Incluye un análisis en Python, un cuaderno de Jupyter y un mapa interactivo generado con Folium.

## Requisitos

- Python 3
- `pip`

## Instalación

1. Clona el repositorio y entra en la carpeta del proyecto:

   ```bash
   git clone https://github.com/Charli65/proyecto_turismo.git
   cd proyecto_turismo
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   En Windows, activa el entorno con:

   ```powershell
   .venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Uso

### Ejecutar el análisis principal

Desde la raíz del repositorio:

```bash
python3 src/main.py
```

El script lee `data/turistas.csv`. Si el archivo no existe, crea un conjunto de datos de ejemplo. El gráfico resultante se guarda en `outputs/visita_turismo.png`.

### Explorar el cuaderno

```bash
jupyter notebook notebooks/analisis_inicial.ipynb
```

### Ver el mapa interactivo

Puedes abrir `index.html` directamente en el navegador. Si el navegador restringe algún recurso local, inicia un servidor sencillo:

```bash
python3 -m http.server 8000
```

Luego visita [http://localhost:8000](http://localhost:8000).

## Estructura

- `data/`: datos turísticos en formato CSV.
- `src/`: scripts de análisis y visualización.
- `notebooks/`: análisis exploratorio en Jupyter.
- `outputs/`: gráficos y resultados generados.
- `index.html`: mapa turístico interactivo.

## Tecnologías

Pandas, NumPy, Matplotlib, Seaborn, scikit-learn, Statsmodels, Prophet, GeoPandas, Folium y Jupyter.

## Fuentes del mapa

El mapa usa [Leaflet](https://leafletjs.com/) y mosaicos de [OpenStreetMap](https://www.openstreetmap.org/copyright).
