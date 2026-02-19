<div align="right">
  <a href="README.md">🇹🇷 Türkçe</a> | <a href="README_EN.md">🇬🇧 English</a>
</div>

# 🌍 <img src="https://flagcdn.com/w40/gb.png" width="32" alt="EN" style="vertical-align: middle;"> Global Socio-Economic Country Segmentation & Aid Prioritization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikit-learn)
![Plotly](https://img.shields.io/badge/Plotly-Data%20Visualization-purple?logo=plotly)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview
This project is a comprehensive **Unsupervised Learning** study developed to analyze the socio-economic and health metrics of countries (e.g., child mortality, income level) to ensure the proper prioritization of international aid budgets. 

Dimensionality reduction was performed on the dataset using **Principal Component Analysis (PCA)**, and countries were divided into socio-economic segments using **K-Means, DBSCAN, and Hierarchical Clustering** algorithms.

## 🚀 Key Features
* **Dimensionality Reduction:** **PCA** was applied to reduce noise in the dataset and improve algorithm performance.
* **Multi-Algorithm Clustering:** K-Means, DBSCAN, and Agglomerative Clustering algorithms were executed and compared independently.
* **Automated Hyperparameter Tuning:** Optimal `eps` and `min_samples` values for the DBSCAN algorithm were automatically optimized based on the Silhouette Score.
* **Interactive Geospatial Analysis:** Clustering results were visualized on a world map using **Plotly Choropleth** maps.

## 🛠️ Tech Stack
* **Data Manipulation:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` (MinMaxScaler, PCA, KMeans, DBSCAN, AgglomerativeClustering), `kneed`
* **Data Visualization:** `seaborn`, `matplotlib`, `plotly.express`

## 🧠 Methodology
1. **Data Preprocessing:** Bringing data to the same scale using `MinMaxScaler`.
2. **PCA:** Selecting the principal components that explain the vast majority of the variance.
3. **Clustering:**
   * **K-Means:** Mathematically finding the optimal K value (Elbow Method) using the `KneeLocator` library.
   * **DBSCAN:** Density-based clustering and outlier detection.
   * **Hierarchical:** Hierarchical clustering using Ward linkage and Euclidean distance metrics.
4. **Business Logic Mapping:** Converting the clusters formed by algorithms into meaningful business labels such as "Budget Needed", "In Between", and "No Budget Needed" based on average income levels.

## 📊 Visualizations
> **Note:** The graphical outputs obtained when the code is run are exemplified below.

### 1. Cluster Distributions
![Boxplots](images/Figure_2.png) 
*Statistical distribution of child mortality (child_mort) and income level across clusters.*

### 2. Global Action Map
![World Map](images/kmean.png) 
*Financial aid priority map around the world based on K-Means results.*

## ⚙️ Installation & Usage

1.  Clone the repository:
    ```bash
    git clone https://github.com/AdnanSag/socioeconomic-segmentation-ml.git
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
---

## 📬 Contact

If you'd like to talk about my projects or collaborate, feel free to reach out:
* **LinkedIn:** https://www.linkedin.com/in/adnan-sag/ 
* **E-posta:** adnansag91@gmail.com

*Created by Adnan Sag*
