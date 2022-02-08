import numpy as np
from scipy.spatial.distance import cdist

class KMeans:
    def __init__(
            self,
            k: int,
            metric: str = "euclidean",
            tol: float = 1e-6,
            max_iter: int = 100):
        """
        inputs:
            k: int
                the number of centroids to use in cluster fitting
            metric: str
                the name of the distance metric to use
            tol: float
                the minimum error tolerance from previous error during optimization to quit the model fit
            max_iter: int
                the maximum number of iterations before quitting model fit
        """
        #assign initial attributes
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
        self.metric = metric
        
        #initialize empty clusters and centroids
        self.clusters = [[] for i in range(self.k)] #holds data point labels for the current clustering
        self.centroids = [] #holds mean feature vector for each centroid
        
    
    def fit(self, mat: np.ndarray):
        #this is basically like creation of the clusters, or finding of the centroids, and then in the predict method
        #you will place the data points on top of the fitted clusters based on what the data points are most similar to
        """
        fits the kmeans algorithm onto a provided 2D matrix

        inputs: 
            mat: np.ndarray
                A 2D matrix where the rows are observations and columns are features
        """
        self.fit_mat = mat #matrix for fitting
        self.n = mat.shape[0] #number of samples in matrix (i.e. number of rows)
        self.m = mat.shape[1] #number of features in matrix (i.e. number of columns)
        
        #for shorter typing:
        n = self.n
        k = self.k
        m = self.m
        
        #set random seed
        np.random.seed(42) #set to 42 for now so results are reproducible

        #initialize centroids by randomly picking k data points as the starting centroids
        rand_idx = np.random.choice(n, k, replace=False) #generate random indices to pick from the input array
        self.centroids = [mat[idx] for idx in rand_idx] #assign the samples of those indices to be the initial centroids
        
        #initialize variables
        cur_mse = 0
        last_mse = 0
        
        
        #optimization procedure
        for i in range(0,self.max_iter):
            #if i=0, initialize centroids randomly
            if i==0:
                rand_idx = np.random.choice(n, k, replace=False) #generate random indices to pick from the input array
                self.centroids = [mat[idx] for idx in rand_idx] #assign the samples of those indices to be the initial centroids
            #otherwise, get the centroids from the mean of each cluster
            else:
                self.centroids = self.get_centroids() #get centroids
            
            #now generate clusters from the calculated centroids
            self.clusters = self._create_clusters(self.centroids)
            #calculate the mse
            cur_mse = self.get_error()
            
            if i==0:
                last_mse = cur_mse
            #check if convergence has been reached
            else:
                if abs(cur_mse - last_mse) <= self.tol:
                    break
                else:
                    last_mse = cur_mse
                


    def predict(self, mat: np.ndarray) -> np.ndarray:
        """
        predicts the cluster labels for a provided 2D matrix

        inputs: 
            mat: np.ndarray
                A 2D matrix where the rows are observations and columns are features

        outputs:
            np.ndarray
                a 1D array with the cluster label for each of the observations in `mat`
        """
        labels = np.emtpy((1,mat.shape[0])) #create an empty 1D array to fill
        self.mat = mat
        clusters = [[] for i in range(self.k)] #create a list of lists that represent empty clusters for now
        for sample_idx, sample in enumerate(mat):
            centroid_idx = self._closest_centroid(sample, self.centroids) #find the closest centroid for each sample
            labels[sample_idx].append(centroid_idx) #append cluster label to 1D array
        return labels
        

    def get_error(self) -> float:
        """
        returns the final mean-squared error of the fit model

        outputs:
            float
                the squared-mean error of the fit model
        """
        errors = []
        for i in range(0,len(self.clusters)): #i is the index of the centroid/cluster you want
            for j in range(0,len(self.clusters[i])): #j is the index of each data point in the current cluster i
                cur_cluster = self.clusters[i] #get the list of samples in the current cluster
                cur_idx = cur_cluster[j] #get the index of the current data point since only indices are stored in self.clusters
                sample = self.fit_mat[cur_idx] #get the feature vector of the current data point from the original matrix
                
                #calculate distance between sample and corresponding centroid
                dist = cdist(sample, self.centroids[i], self.metric)
                errors.append(dist) #append to a list of errors
                
        #square the distances
        squared_errors = [number ** 2 for number in errors]
        #take mean of squared errors to get MSE
        return np.mean(squared_errors)
        
        
    def get_centroids(self) -> np.ndarray:
        #you will call this within the fit method to get the centroids
        #assign the final centroids as an attribute of the class so that you can use it in the predict method
        """
        returns the centroid locations of the fit model

        outputs:
            np.ndarray
                a `k x m` 2D matrix representing the cluster centroids of the fit model
        """
        centroids = np.zeroes((self.k, self.n)) #initialize an array where each row will be the mean values of a cluster
        #for each cluster index and each cluster, get the actual sample values in each cluster and find their mean to get the
        #overall mean feature values for the centroid
        for cluster_idx, cluster in enumerate(clusters):
            mean = np.mean(self.fit_mat[cluster], axis=0)
            centroids[cluster_idx] = mean
        return centroids
    
    def _create_clusters(self, centroids):
        """
        assigns all samples in the input matrix to the closest centroids
        
        input:
            mean feature vectors defining the centroids
        output:
            list of lists containing indices of data samples sorted into which cluster they belong to
        """
        clusters = [[] for i in range(self.k)] #create a list of lists that represent empty clusters for now
        for idx,sample in enumerate(self.fit_mat):
            centroid_idx = self._closest_centroid(sample, centroids) #find the closest centroid for each sample
            clusters[centroid_idx].append(idx) #append current sample index to the cluster with the centroid it is closest to
        return clusters

    
    
    def _closest_centroid(self, sample, centroids):
        """
        gets the index of the centroid that is closest to the input data point
        
        inputs:
            sample
                input data point in m dimensions
            centroids
                list of mean feature vectors representing each centroid
            metric:string
                distance metric used to calculate distances between sample and centroids
        output:
            index of centroid closest to sample
        """
        #calculate the distance between the current sample (i.e. row of the input matrix) and each centroid, and take the min
        distances = []
        for i in range(0,len(centroids)):
            distances.append(cdist(sample, centroids[i], self.metric))
            
        centroid_idx = np.argmin(distances) #get index of minimum distance--corresponds to 
        return centroid_idx