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
        
        for sample_idx,sample in enumerate(X):
            point_distance = []
            l = [[] for i in range(k)] #create a list of lists that holding dist. vals betw cur_point and other cluster points
            
            for label_idx in range(0,len(y)):
                dist = cdist(X[sample_idx], X[label_idx], self.metric) #distance between current point and all other points
                (l[y[label_idx]]).append(dist) #add dist to list in l corresponding to the current label
                point_distance.append(ij_dist)
            
            all_point_distances.append(point_distance)
            
        
        
        
        
        
        
        
        
        
        
        
        #you have the input data and the labels for the input data
        #silhouette score for data point i is the distance from the point to the closest cluster, minus the distance from the point to the other points in the same cluster
        k = len(np.unique(y)) #get number of clusters
        all_distances = [] #this will hold arrays of the distances for each point
        
        #calculate distances between each point and all other points
        for i in range(0,X.shape(0)):
            point_label = y[i] #get the label at the same index as the current point
            distances = np.zeros((1,len(y))) #create an array that will hold all of the distances
            for j in range(0,len(y)): #get the distance between this point and all other points
                cur_label = y[j] #get the label of the iteration
                distances[j] = cdist(X[i], X[j], self.metric)
            all_distances[i].append(distances)
        
        #calculate cohesion by taking the mean distance between each point and all the points in the same cluster
        cohesion = np.zeros((1,len(y)) #list to contain mean intra-cluster distances for each point
        for i in range(0,len(y)):
            point_label = y[i]
            distances = all_distances[i]
            total = 0
            count = 0
            mean = 0
            for j in range(0,len(y)):
                current_label = y[j]
                count += 1
                if current_label == point_label: #if the point label equals the current label, then we're in the right cluster!
                total = total + distances[j] #add distances together
            mean = total/(count=1)
            cohesion[i] = mean

        for i in range()
        

        #for each point
            #get the label of that point
            #get the distance between that point and the other points in the same label
            #get the distance between that point and all other points not in the same label
            #take average within non-same clusters to get separation score
            #take min of separation scores
        return scores


