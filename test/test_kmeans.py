#Importing Dependencies
import pytest
import numpy as np
from cluster import (KMeans, Silhouette, make_clusters)

def test_kmeans():
    #test things like k=0, samples<k, large dimensionality (m), low dimensionality (m=1), very high k
    #check to make sure that a few points that should be clustered together are in fact assigned the same labels
    
    #make some clusters to test
    t_clusters, t_labels = make_clusters(scale=0.3)
    
    
    #-----------------------------------------------------------
    #check to make sure that k=0 raises an AttributeError
    try:
        kmeans = KMeans(k=0)
        assert False
    except AttributeError:
        assert True
        
        
    #------------------------------------------------------------
    #check to make sure that fitting doesn't occur if k<the number of observations
    try:
        kmeans2 = KMeans(k=1000)
        kmeans2.fit(t_clusters)
        assert False
    except AttributeError:
        assert True
    
    
    #------------------------------------------------------------
    #check that algorithm will run with a large k
    d_clusters, d_labels = make_clusters(n=1000, m=200, k=3)
    kmeans3 = KMeans(k=1000)
    kmeans3.fit(d_clusters)
    pred_labels = kmeans3.predict(d_clusters)
    #checking that it properly created 1000 unique clusters since there are 100 observations
    assert len(kmeans3.clusters)==1000
    assert len(np.unique(kmeans3.clusters))==1000
    
    
    #-------------------------------------------------------------
    #check that certain points are clustered together, even if labels change
    l_clusters, l_labels = make_clusters(scale=2)
    kmeans4 = KMeans(k=3)
    kmeans4.fit(l_clusters)
    pred_labels = kmeans4.predict(l_clusters)
    #observations at indices 399 and 450 should have the same label
    assert pred_labels[0][399] == pred_labels[0][450] #include the [0] to unlist how the data is stored
    #check labels of two other observations that should be clustered
    assert pred_labels[0][100] == pred_labels[0][150]
    
    
    #--------------------------------------------------------------
    #check that the algorithm can handle single-dimensional data
    #the provided plotting function will not be able to plot the results, but can still run some checks
    l_clusters, l_labels = make_clusters(scale=2, m=1)
    kmeans5 = KMeans(k=3)
    kmeans5.fit(l_clusters)
    pred_labels = kmeans6.predict(l_clusters)
    assert len(np.unique(kmeans5.clusters))==3
    assert len(kmeans5.clusters) == 3
    assert len(kmeans5.centroids[0]) #check that the centroids only have 1 dimension
    
    
    #---------------------------------------------------------------
    #check that the algorithm can handle high-dimensional data
    t_clusters, t_labels = make_clusters(scale=0.3, m=200)
    kmeans6 = KMeans(k=3)
    kmeans6.fit(t_clusters)
    pred_labels = kmeans6.predict(t_clusters)
    #assert that fitting and predictions happened correctly
    assert len(kmeans6.clusters)==5
    assert len(np.unique(kmeans6.clusters))==5
    assert pred_labels[0][300]==pred_labels[0][250]
    assert len(kmeans6.centroids[0]) #check that the centroids have 200 dimensions
    
    
    


def test_silhouette():
    #check to make sure silhouette scores fall between -1 and 1
    #check that silhouette scores incr. as k increases (maybe compare avg silhouette score for the data in different k cases)
    
    pass
