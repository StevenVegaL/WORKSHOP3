#  **Predicción del Índice de Felicidad en Países de Todo el Mundo** 🤖😊

## 🌟 Overview
Este proyecto se centra en la predicción del índice de felicidad de diferentes países utilizando técnicas avanzadas de aprendizaje automático y procesamiento de datos en tiempo real. Aprovechando el poder del streaming de datos con Kafka y la precisión del modelo de Random Forest, hemos desarrollado un sistema robusto y eficiente para realizar predicciones precisas y almacenarlas en una base de datos PostgreSQL.

## 📋 Table of Contents
- [🌟 Overview](#-overview)
- [📊 Data Sources](#-data-sources)
- [💻 Technologies Used](#-technologies-used)
- [🔧 Features](#-features)
- [📁 Estructura del Repositorio](#-estructura-del-repositorio)
- [🚀 Ejecución](#-ejecución)

## 📊 Data Sources
Los datos utilizados en este proyecto provienen de cinco archivos CSV que contienen información detallada sobre el índice de felicidad en diferentes países desde el año 2015 hasta el 2019. Cada archivo incluye una variedad de indicadores que influyen en la felicidad, tales como:

- **Economía (PIB per cápita):** Indicador económico que mide la producción de bienes y servicios por habitante.
- **Apoyo Social:** Medida de la percepción de soporte social que las personas sienten que tienen.
- **Expectativa de Vida:** Estimación de la cantidad de años que se espera que viva una persona.
- **Libertad para Tomar Decisiones:** Grado en que las personas sienten libertad para tomar decisiones sobre sus vidas.
- **Generosidad:** Indicador de las donaciones y actos de caridad realizados por los ciudadanos.
- **Percepción de la Corrupción Gubernamental:** Medida de la percepción de la corrupción en el gobierno y las instituciones públicas.

### 📂 Archivos de Datos
- `2015.csv`: Datos del año 2015.
- `2016.csv`: Datos del año 2016.
- `2017.csv`: Datos del año 2017.
- `2018.csv`: Datos del año 2018.
- `2019.csv`: Datos del año 2019.
- `happy_df.csv`: Conjunto de datos combinado que incluye todos los años anteriores.

Cada archivo ha sido cuidadosamente procesado y transformado para garantizar la calidad y consistencia de los datos antes de ser utilizados para el entrenamiento del modelo y las predicciones.

## 💻 Technologies Used
- **Python:** Lenguaje de programación principal utilizado para la manipulación de datos, entrenamiento del modelo y predicciones.
- **Kafka:** Utilizado para el streaming de datos en tiempo real.
- **PostgreSQL:** Base de datos utilizada para almacenar las predicciones y los datos originales.
- **Scikit-learn:** Biblioteca de aprendizaje automático utilizada para entrenar el modelo de Random Forest.
- **Pandas:** Biblioteca utilizada para la manipulación y análisis de datos.
- **Seaborn & Matplotlib:** Bibliotecas utilizadas para la visualización de datos.

## 🔧 Features
- **Extracción y Transformación de Datos (ETL):** Procesamiento y limpieza de datos desde múltiples archivos CSV.
- **Entrenamiento del Modelo:** Entrenamiento de un modelo de Random Forest utilizando una división de datos del 70-30.
- **Streaming en Tiempo Real:** Implementación de Kafka para capturar y procesar datos en tiempo real.
- **Predicciones y Almacenamiento:** Predicciones realizadas por el modelo y almacenadas en PostgreSQL.
- **Visualización de Datos:** Gráficas y visualizaciones para analizar el rendimiento del modelo y los datos.


## 📁 Estructura del Repositorio
La estructura del repositorio está organizada de la siguiente manera:

```plaintext
📦 NombreDelProyecto
├── 📂 data                   # Archivos de datos
│   ├── 📄 2015.csv
│   ├── 📄 2016.csv
│   ├── 📄 2017.csv
│   ├── 📄 2018.csv
│   ├── 📄 2019.csv
│   └── 📄 happy_df.csv       # Conjunto de datos combinado
├── 📂 main                   # Código principal del proyecto
│   ├── 📄 .gitignore
│   ├── 📄 feature_selection.ipynb  # Selección de características
│   ├── 📄 metric.ipynb              # Cálculo de métricas
│   ├── 📄 model_prediction.ipynb    # Predicciones del modelo
│   └── 📄 transform_happy.py        # Script de transformación de datos
├── 📂 model                  # Modelos entrenados
│   └── 📄 my_happiness_model.pkl    # Modelo de Random Forest entrenado
└── 📂 notebook               # Notebooks Jupyter para análisis
    └── 📄 eda.ipynb                # Análisis exploratorio de datos
```

## 🚀 Ejecución

1. **Asegúrate de que Docker esté instalado en tu máquina.**

2. **Guardar el archivo `docker-compose.yml` en tu directorio de trabajo, en la raíz de este.**

3. **Iniciar los servicios usando Docker Compose**:
   ```sh
   docker-compose up -d
   ```
   Esto descargará las imágenes necesarias y levantará los contenedores de Zookeeper y Kafka Broker.

4. **Verificar los contenedores en funcionamiento**:
   ```sh
   docker-compose ps
   ```
   Asegúrate de que ambos contenedores, zookeeper y kafka, estén en estado `Up`. También puedes verificar esto en Docker Desktop.

5. **Crear un Topic en Kafka**:
   Si no has creado un topic aún, puedes hacerlo ejecutando el siguiente comando desde el contenedor de Kafka:
   ```sh
   docker exec -it kafka kafka-topics --create --topic happy_test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

6. **Verificar el topic creado**:
   ```sh
   docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
   ```

7. **Ejecuta el Productor y Consumidor**:
   - Inicia el productor en el archivo `feature_selection` en la función `def send_message`.
   - Simultáneamente, ejecuta el consumidor en el archivo `model_prediction` en la función `def consume_messages`.

8. **Verificación Final**:
   Después de ejecutar el productor y el consumidor:
   - Asegúrate de que el productor envía los mensajes y se detiene.
   - Verifica que el consumidor recibe todos los mensajes, imprime la salida deseada, y se cierra correctamente después de un período de inactividad.

### Comandos Rápidos

```sh
# Clona el repositorio
git https://github.com/StevenVegaL/WORKSHOP3/tree/main

# Navega al directorio del proyecto
cd ejemplo

# Inicia los servicios con Docker Compose
docker-compose up -d

# Verifica que los contenedores estén en funcionamiento
docker-compose ps

# Crea un topic en Kafka
docker exec -it kafka kafka-topics --create --topic happy_test --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Verifica el topic creado
docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092

# Ejecuta el productor y el consumidor
# Inicia el productor en la función send_message de feature_selection
# Inicia el consumidor en la función consume_messages de model_prediction
```

¡Y listo! Ahora puedes disfrutar explorando y prediciendo la felicidad en todo el mundo. 🌟😊
