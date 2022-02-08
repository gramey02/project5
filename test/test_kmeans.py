#Importing Dependencies
import pytest
import numpy as np
from cluster import (KMeans, Silhouette)

def test_edgeCase_clustering():
    #test things like k=0, samples<k, large dimensionality (m), low dimensionality (m=1), very high k
    
    pass


def test_clustering():
    #check to make sure that a few points that should be clustered together are in fact assigned the same labels
    pass


def test_silhouette_scoring():
    #check to make sure silhouette scores fall between -1 and 1
    #check that silhouette scores incr. as k increases (maybe compare avg silhouette score for the data in different k cases)
    pass
