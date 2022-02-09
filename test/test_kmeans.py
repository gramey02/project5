#Importing Dependencies
import pytest
import numpy as np
from cluster import (KMeans, Silhouette, make_clusters)

def test_kmeans():
    #test things like k=0, samples<k, large dimensionality (m), low dimensionality (m=1), very high k
    #check to make sure that a few points that should be clustered together are in fact assigned the same labels
    #check to make sure that k=0 raises an AttributeError
    try:
        kmeans = KMeans(k=0)
        assert False
    except AttributeError:
        assert True
        
    
    #check that it will run with a very large k
    kmeans2 = KMeans(k=1000)
    kmeans2.fit()
    


def test_silhouette():
    #check to make sure silhouette scores fall between -1 and 1
    #check that silhouette scores incr. as k increases (maybe compare avg silhouette score for the data in different k cases)
    
    pass
