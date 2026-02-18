# 🌍 Global Socio-Economic Country Segmentation & Aid Prioritization

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikit-learn)
![Plotly](https://img.shields.io/badge/Plotly-Data%20Visualization-purple?logo=plotly)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview
Bu proje, ülkelerin sosyo-ekonomik ve sağlık metriklerini (çocuk ölümleri, gelir düzeyi vb.) analiz ederek, uluslararası yardım bütçelerinin doğru önceliklendirilmesini sağlamak amacıyla geliştirilmiş kapsamlı bir **Denetimsiz Öğrenme (Unsupervised Learning)** çalışmasıdır. 

Veri seti üzerinde **Temel Bileşen Analizi (PCA)** ile boyut indirgeme yapılmış ve ülkeler **K-Means, DBSCAN ve Hiyerarşik Kümeleme** algoritmaları kullanılarak sosyo-ekonomik segmentlere ayrılmıştır.

## 🚀 Key Features
* **Dimensionality Reduction:** Veri setindeki gürültüyü azaltmak ve algoritma performansını artırmak için **PCA** uygulanmıştır.
* **Multi-Algorithm Clustering:** K-Means, DBSCAN ve Agglomerative Clustering algoritmaları bağımsız olarak çalıştırılıp karşılaştırılmıştır.
* **Automated Hyperparameter Tuning:** DBSCAN algoritması için en uygun `eps` ve `min_samples` değerleri Silhouette Skoru baz alınarak otomatik olarak optimize edilmiştir.
* **Interactive Geospatial Analysis:** Kümeleme sonuçları, **Plotly Choropleth** haritaları ile dünya haritası üzerinde görselleştirilmiştir.

## 🛠️ Tech Stack
* **Data Manipulation:** `pandas`, `numpy`
* **Machine Learning:** `scikit-learn` (MinMaxScaler, PCA, KMeans, DBSCAN, AgglomerativeClustering), `kneed`
* **Data Visualization:** `seaborn`, `matplotlib`, `plotly.express`

## 🧠 Methodology
1. **Data Preprocessing:** `MinMaxScaler` kullanılarak verilerin aynı ölçeğe getirilmesi.
2. **PCA:** Varyansın büyük çoğunluğunu açıklayan temel bileşenlerin seçilmesi.
3. **Clustering:**
   * **K-Means:** `KneeLocator` kütüphanesi ile optimum K değerinin (Elbow Method) matematiksel olarak bulunması.
   * **DBSCAN:** Yoğunluk tabanlı kümeleme ve aykırı değer (outlier) tespiti.
   * **Hierarchical:** Ward linkage ve Euclidean uzaklık metrikleri ile hiyerarşik kümeleme.
4. **Business Logic Mapping:** Algoritmaların oluşturduğu kümelerin, ortalama gelir (income) seviyelerine göre "Budget Needed", "In Between" ve "No Budget Needed" şeklinde anlamlı iş etiketlerine dönüştürülmesi.

## 📊 Visualizations
> **Not:** Kod çalıştırıldığında elde edilen grafik çıktıları aşağıda örneklenmiştir.

### 1. K-Means Elbow Method & Variance 
![Elbow Curve](https://via.placeholder.com/800x400.png?text=Insert+Elbow+Curve+Screenshot+Here) 
*KneeLocator ile optimum küme sayısının belirlenmesi.*

### 2. Cluster Distributions
![Boxplots](https://via.placeholder.com/800x400.png?text=Insert+Boxplot+Screenshot+Here) 
*Çocuk ölümleri (child_mort) ve gelir seviyesinin (income) kümelere göre istatistiksel dağılımı.*

### 3. Global Action Map
![World Map](https://via.placeholder.com/800x400.png?text=Insert+Plotly+Map+Screenshot+Here) 
*K-Means sonuçlarına göre dünyadaki finansal yardım öncelik haritası.*

## ⚙️ Installation & Usage

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Repository'yi klonlayın:
```bash
git clone [https://github.com/](https://github.com/)[KULLANICI_ADIN]/country-clustering-analysis.git
cd country-clustering-analysis
