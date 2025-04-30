
# 🧠 Análisis de Tumores Cerebrales

## 🇦🇷 Español

### 📌 Acerca del proyecto

Este repositorio corresponde a la primera entrega del curso **Data Science II** de CoderHouse.  
El objetivo es trabajar con un conjunto de datos clínicos simulados para realizar un **análisis exploratorio de datos (EDA)**, identificar patrones relevantes y presentar los principales hallazgos a través de una presentación (`Tumores-Cerebrales.pdf`) disponible en la raíz del repositorio.

### 🧬 Dataset utilizado

El dataset fue obtenido de **Kaggle** y simula información médica sobre pacientes con tumores cerebrales.  
Incluye datos como edad, género, síntomas, ubicación del tumor, tratamientos recibidos y evolución del paciente.  
Es un conjunto de datos **sintético**, generado únicamente con fines educativos y de investigación.

### ⬇️ Cómo descargar el dataset

La descarga se realiza mediante la **API de Kaggle**.  
Pasos:

1. Crear una cuenta en [Kaggle](https://www.kaggle.com/).
2. Ir a la sección **Settings > API** y generar un nuevo token.
3. Guardar el archivo `kaggle.json` en la carpeta `environment/`.
4. Ejecutar el siguiente script desde la raíz del proyecto:

```bash
python scripts/download_data.py
```

> ⚠️ **Importante**: si vas a hacer un Fork del repositorio, no olvides guardar tu archivo `kaggle.json` dentro de `environment/` (no se sube por seguridad, ya está en el `.gitignore`).

### 📄 Recursos del proyecto

- 📊 [Notebook de limpieza de datos (Data Wrangling)](notebooks/01_data_wrangling.ipynb)
- 📈 [Notebook de análisis exploratorio (EDA)](notebooks/02_exploratory_data_analysis.ipynb)
- 🧾 [Presentación en PDF](Tumores-Cerebrales.pdf)

---

## 🇺🇸 English

# 🧠 Brain Tumor Analysis

### 📌 About the project

This repository is part of the first assignment for the **Data Science II** course at CoderHouse.  
Its goal is to work with a simulated clinical dataset to perform **exploratory data analysis (EDA)**, identify key patterns, and summarize the main findings in a visual presentation (`Tumores-Cerebrales.pdf`), located at the root of this repository.

### 🧬 Dataset used

The dataset was sourced from **Kaggle**, and it simulates medical information related to brain tumor patients.  
It includes demographic information, tumor characteristics, symptoms, treatments, and outcomes.  
It is a **synthetic dataset**, intended solely for educational and research purposes.

### ⬇️ How to download the dataset

The dataset is downloaded using the **Kaggle API**.  
Steps:

1. Create an account at [Kaggle](https://www.kaggle.com/).
2. Go to **Settings > API** and generate a new token.
3. Save the `kaggle.json` file inside the `environment/` folder.
4. Run the following script from the root of the project:

```bash
python scripts/download_data.py
```

> ⚠️ **Note**: If you're forking this repo, make sure to place your `kaggle.json` inside `environment/` (the file is ignored by Git for security reasons).

### 📄 Project Resources

- 📊 [Data Wrangling Notebook](notebooks/01_data_wrangling.ipynb)  
- 📈 [Exploratory Data Analysis (EDA) Notebook](notebooks/02_exploratory_data_analysis.ipynb)  
- 🧾 [Project Presentation (PDF)](Tumores-Cerebrales.pdf)
