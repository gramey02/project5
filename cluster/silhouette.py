import numpy as np
from scipy.spatial.distance import cdist

class Silhouette:
    def __init__(self, metric: str = "euclidean"):
        """
        inputs:
            metric: str
                the name of the distance metric to use
        """
        #assign initial attribute
        self.metric = metric

    def score(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        calculates the silhouette score for each of the observations

        inputs:
            X: np.ndarray
                A 2D matrix where the rows are observations and columns are features. 

            y: np.ndarray
                a 1D array representing the cluster labels for each of the observations in `X`

        outputs:
            np.ndarray
                a 1D array with the silhouette scores for each of the observations in `X`
        """
        #you have the input data and the labels for the input data
        #silhouette score for data point i is the distance from the point to the closest cluster, minus the distance from the point to the other points in the same cluster
        for i in range(0,X.shape(0)):
            cur_label = y[i]
        
        
        
        #for each point
            #get the label of that point
            #get the distance between that point and the other points in the same label
            #get the distance between that point and all other points not in the same label
            #take average within non-same clusters to get separation score
            #take min of separation scores
        return scores


