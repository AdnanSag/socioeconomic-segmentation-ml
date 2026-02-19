import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import math
import plotly.express as px

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score
from kneed import KneeLocator

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: CSV file '{file_path}' not found.")
        return None

def analyzing(df):
    pd.set_option('display.max_columns', None)
    print("-" * 60)
    print(df.info())
    print("-" * 60)
    print(df.describe())
    
def plot_all_histograms(df, title_prefix=""):     
    if df is None: return
    num_cols = df.select_dtypes(include=[np.number]).columns
    if len(num_cols) == 0:
        return
    n_cols = 3
    n_rows = math.ceil(len(num_cols) / n_cols)
    plt.figure(figsize=(5 * n_cols, 4 * n_rows))
    for i, col in enumerate(num_cols, 1):
        plt.subplot(n_rows, n_cols, i)
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f"{title_prefix}{col}")
        plt.xlabel("")
        plt.ylabel("")
    plt.tight_layout()
    plt.show()
    
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.show()

def scaling(df):
    scaler = MinMaxScaler()
    df_scaled_matrix = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(df_scaled_matrix, columns=df.columns)
    return df_scaled

def PrincipalComponentAnalysis(df):
    pca = PCA()
    pca_df = pd.DataFrame(pca.fit_transform(df))
    plt.figure()
    plt.step(list(range(1, len(pca.explained_variance_ratio_) + 1)), np.cumsum(pca.explained_variance_ratio_))
    plt.plot(list(range(1, len(pca.explained_variance_ratio_) + 1)), np.cumsum(pca.explained_variance_ratio_))
    plt.ylabel("Variance Covered")
    plt.title("Variance Covered")
    plt.show()
    return pca_df

def kmeancluster(df):
    wcss = []
    k_range = range(1, 11)
    
    for k in k_range:
        kmeans = KMeans(n_clusters=k, init="k-means++", random_state=42)
        kmeans.fit(df)
        wcss.append(kmeans.inertia_)
    
    plt.figure()
    plt.plot(k_range, wcss, marker='o')
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("WCSS")
    plt.title("Elbow Method")
    plt.show()


    kl = KneeLocator(k_range, wcss, curve="convex", direction="decreasing")
    optimal_k = kl.elbow
    final_k = optimal_k if optimal_k else 3 
    
    model = KMeans(n_clusters=final_k, init="k-means++", random_state=42)
    labels = model.fit_predict(df)
    
    if len(set(labels)) > 1:
        print("K-Means Silhouette Score:", silhouette_score(df, labels))
    return labels

def dbscan_cluster(df):
    """
    DBSCAN için otomatik hiperparametre optimizasyonu yapar.
    En yüksek Silhouette Skoruna sahip modeli seçer.
    """
    eps_values = np.arange(0.1, 3.0, 0.1) 
    min_samples_values = range(2, 8)      
    
    best_score = -1
    best_params = {'eps': 0.25, 'min_samples': 3}
    best_labels = None
    
    print("DBSCAN için en iyi parametreler aranıyor...")
    
    for eps in eps_values:
        for min_samples in min_samples_values:
            model = DBSCAN(eps=eps, min_samples=min_samples)
            labels = model.fit_predict(df)
            
            unique_labels = set(labels)
            n_clusters = len(unique_labels) - (1 if -1 in labels else 0)
            
            if n_clusters >= 2:
                score = silhouette_score(df, labels)
                
                if score > best_score:
                    best_score = score
                    best_params = {'eps': eps, 'min_samples': min_samples}
                    best_labels = labels
                    
    if best_labels is None:
        model = DBSCAN(eps=0.25, min_samples=3)
        best_labels = model.fit_predict(df)
    else:
        print(f"En İyi DBSCAN Parametreleri: eps={best_params['eps']:.2f}, min_samples={best_params['min_samples']}")
        
    return best_labels

def hierarchical_cluster(df, n_clusters=3):
    model = AgglomerativeClustering(n_clusters=n_clusters, metric='euclidean', linkage='ward')
    labels = model.fit_predict(df)
    
    if len(set(labels)) > 1:
        print("Hierarchical Silhouette Score:", silhouette_score(df, labels))
    return labels

def map_clusters_by_income(df, cluster_col):
    labels = df[cluster_col].copy()
    valid_clusters = df[labels != -1]
    
    n_clusters = valid_clusters[cluster_col].nunique()
    mapping = {-1: "Outlier/Noise (DBSCAN)"}
    
    if n_clusters > 0:
        # Kümeleri gelir (income) ortalamasına göre sırala
        cluster_income = valid_clusters.groupby(cluster_col)['income'].mean().sort_values()
        
        if n_clusters == 2:
            mapping[cluster_income.index[0]] = "Budget Needed (Lowest)"
            mapping[cluster_income.index[1]] = "No Budget Needed (Highest)"
            
        elif n_clusters == 3:
            mapping[cluster_income.index[0]] = "Budget Needed"
            mapping[cluster_income.index[1]] = "In Between"
            mapping[cluster_income.index[2]] = "No Budget Needed"
            
        else:
            for i, cluster_id in enumerate(cluster_income.index):
                if i == 0:
                    mapping[cluster_id] = "Budget Needed (Lowest)"
                elif i == n_clusters - 1:
                    mapping[cluster_id] = "No Budget Needed (Highest)"
                else:
                    mapping[cluster_id] = f"In Between Level {i} (low levels represents high need of budget)"
                    
    return labels.map(mapping)

def world_visualization(df, cluster_column, title):
    # Dinamik isimlendirmeler için genişletilmiş renk haritası
    color_map = {
        "Budget Needed": "Red",
        "In Between": "Yellow",
        "No Budget Needed": "Green",
        "Budget Needed (Lowest)": "DarkRed",
        "No Budget Needed (Highest)": "DarkGreen",
        "In Between (Level 1)": "Orange",
        "In Between (Level 2)": "Gold",
        "Outlier/Noise (DBSCAN)": "Black"
    }
    
    fig = px.choropleth(
        df,
        locationmode="country names",
        locations="country",
        title=title,
        color=cluster_column,
        color_discrete_map=color_map 
    )
    fig.update_geos(fitbounds="locations", visible=True)
    fig.show()

def main():
    df2 = load_data("29-country_data.csv")
    if df2 is None: return
    
    df = df2.drop("country", axis=1)
    df_scaled = scaling(df)

    pca_df = PrincipalComponentAnalysis(df_scaled)
    pca_df = pca_df.iloc[:, :3]

    df2['KMeans_Class'] = kmeancluster(pca_df)
    df2['KMeans_Mapped'] = map_clusters_by_income(df2, 'KMeans_Class')
    
    df2['DBSCAN_Class'] = dbscan_cluster(pca_df)
    df2['DBSCAN_Mapped'] = map_clusters_by_income(df2, 'DBSCAN_Class')
    
    df2['Hierarchical_Class'] = hierarchical_cluster(pca_df, n_clusters=3)
    df2['Hierarchical_Mapped'] = map_clusters_by_income(df2, 'Hierarchical_Class')

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    plt.subplot(1, 2, 1)
    sns.boxplot(data=df2, x="KMeans_Mapped", y="child_mort")
    plt.title("child_mort vs KMeans")
    plt.subplot(1, 2, 2)
    sns.boxplot(data=df2, x="KMeans_Mapped", y="income")
    plt.title("income vs KMeans")
    plt.tight_layout()
    plt.show()

    world_visualization(df2, "KMeans_Mapped", "K-Means: Needed Budget by Country")
    world_visualization(df2, "DBSCAN_Mapped", "DBSCAN: Needed Budget by Country")
    world_visualization(df2, "Hierarchical_Mapped", "Hierarchical: Needed Budget by Country")

if __name__ == "__main__":
    main()