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
        
        k = len(np.unique(y)) #get number of clusters
        all_point_distances = [] #will hold distance lists for each point
        scores=np.empty((1,X.shape[0]))
        
        for sample_idx,sample in enumerate(X):
            l = [[] for i in range(k)] #create a list of lists that holding dist. vals betw cur_point and other cluster points
            
            for label_idx in range(0,len(y)):
                dist = cdist(X[sample_idx], X[label_idx], self.metric) #distance between current point and all other points
                (l[y[label_idx]]).append(dist) #add dist to list in l corresponding to the current label
            
            all_point_distances.append(l) #append to keep track of distance lists for each point
            
            for i in range(0,len(l)):
                a = None #will hold avg dist from current point to other points in its cluster
                b = [] #will hold avg dist from current point to other clusters

                #if the current point and the current list of distances were calculated from points in the same cluster,
                #subtract one from the length of the current list
                if i==y[sample_idx]:
                    a = sum(l[i])/(len(l[i])-1) #average of distances between current point and points in its cluster
                    
                #otherwise calculate the average as normal
                else:
                    b.append = sum(l[i])/len(l[i]) #average of the distances from the current point to other cluster points
                
            scores[sample_idx] = (min(b)-a)/max(min(b)-a)
            

        return scores


