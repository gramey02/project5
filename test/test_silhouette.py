#Importing dependencies
import pytest
import numpy as np
from cluster import (KMeans, Silhouette, make_clusters)

def test_silhouette():
    
    t_clusters, t_labels = make_clusters(scale=0.3) #make dummy clusters
    kmeans = KMeans(k=3)
    kmeans.fit(t_clusters)
    pred_labels = kmeans.predict(t_clusters)
    test_s=Silhouette()
    scores = test_s.score(t_clusters,pred_labels)
    
    #silhouette scores should be in between 1 and -1
    for i in range(0,scores.shape[1]):
        assert scores[0][i] <= 1
        assert scores[0][i] >= -1