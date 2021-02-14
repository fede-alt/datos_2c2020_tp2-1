# datos_2c2020_tp2
Repositorio del segundo trabajo práctico grupal de la materia Organización de Datos. Grupo: Axones Informáticos

## rawdata/
Carpeta donde estan los datos descargados de la competencia (no deberían modificarse)

## examples/
Carpetas con modelos de ejemplo, aportar si tienen algunos a mano

## log/ 
En el tp se evalúa la tabulación de resultados, cuando quieren loguear modelos y sus resultados importan el modulo ``Logger.py`` y llaman a la función `"log_model"` con la firma:

        ```
        log_model(model, hyperparameters, features, score, verbose=True)
        
        model: Nombre del modelo
        hyperparameters: diccionario con la estructura {nombre: valor}
        features: lista con las columnas que se usaron
        score: resultado
    
        ```

## models/
Los modelos de machine learning para el tp

## Data Preprocessing.ipynb
Notebook donde se preprocesa los datos. Feature engineering.

## datasets/
Carpeta donde se deberían exportar los sets de datos de ``Data Preprocessing.ipynb`` y desde donde se importan para los modelos

## IDEAS/TODO:

Feature hashing:
   * Agregar columna que cuente cuantas entradas hay para cada Opportunity_ID
   * Agregar columna que cuente el rango en días entre las fechas estimadas de inicio y fin
   * Tema territorios: Podríamos buscar alguna librería que mapee regiones a coordenadas
                       y usamos esos valores en 2d en vez de Binary Encoding
   * asd
