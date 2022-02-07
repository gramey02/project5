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
        
        #optimization procedure
        for in in self.max_iter:
            self.clusters = self._create_clusters(self.centroids) #create the clusters based on the current centroids
            old_centroids = self.centroids #store old centroids for comparison later
            self.centroids = self.get_centroids() #recalculate centroids after new clusters have been created
            
            #calculate error between old centroids and newest centroids
            if self.get_error() <= self.tol:
                break
                
            
            
            
            #check the difference between the previous clusters and these clusters (i.e. check for convergence)
        #for i in max_iters... -- finish when max_iters is reached, but also include 
        #a break if convergence point is reached before then
            #update the clusters
            #update the centroids
            #check if convergence has been reached

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

    def get_error(self) -> float:
        """
        returns the final mean-squared error of the fit model

        outputs:
            float
                the squared-mean error of the fit model
        """
        #for each "iteration" in the for loop of the fit method
        #calculate the distance from each point to its centroid (using whatever distance metric was provided)
        #square the distances
        #take the mean
        pass
        
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
            list containing indices of data samples sorted into which cluster they belong to
        """
        clusters = [[] for i in range(self.k)] #create a list of lists that represent empty clusters for now
        for idx,sample in enumerate(self.fit_mat):
            centroid_idx = self._closest_centroid(sample, centroids) #find the closest centroid for each sample
            clusters[centroid_idx].append(idx) #append current sample index to the cluster with the centroid it is closest to
        return clusters

    
    
    def _closest_centroid(self, sample, centroids, metric):
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
            distances.append(cdist(sample, centroids[i], metric))
            
        centroid_idx = np.argmin(distances) #get index of minimum distance--corresponds to 
        return centroid_idx