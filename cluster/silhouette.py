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
        scores=np.zeros((1,X.shape[0]))
        
        for sample_idx,sample in enumerate(X):
            #create a list of lists that holds dist. vals betw cur_point and other cluster points
            cur_point_dist = [[] for i in range(k)]
            
            for label_idx in range(0,y.shape[1]):
                #distance between current point and all other points
                dist = cdist(np.array([X[sample_idx]]), np.array([X[label_idx]]), self.metric)
                dist = dist[0][0] #unlist the current distance value
                (cur_point_dist[y[0][label_idx]]).append(dist) #add dist to list in l corresponding to the current label
            
            all_point_distances.append(cur_point_dist) #append to keep track of distance lists for each point
            #print(cur_point_dist)
            
            a = None #will hold avg dist from current point to other points in its cluster
            b = [] #will hold avg dist from current point to other clusters
            
            for i in range(0,len(cur_point_dist)):

                #if the current point and the current list of distances were calculated from points in the same cluster,
                #subtract one from the length of the current list
                if i == (y[0][sample_idx]):
                    #average of distances between current point and points in its cluster
                    #subtract 1 because the list also includes a zero for the distance between the current point and itself
                    a = sum(cur_point_dist[i])/(len(cur_point_dist[i])-1)
                    
                #otherwise calculate the average as normal
                else:
                    #average of the distances from the current point to other cluster points
                    b.append(sum(cur_point_dist[i])/len(cur_point_dist[i]))
                #print(a)
                #print(b)
                
            scores[0][sample_idx] = (min(b)-a)/max(min(b),a)
            

        return scores


