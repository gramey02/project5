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
        self.metric = euclidian
        
        #initialize empty clusters and centroids
        self.clusters = [] #holds data point labels for the current clustering
        self.centroids = [] #hold mean feature vector for each centroid
        
    
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
        self.d = mat.shape[1] #number of dimensions in matrix (i.e. number of columns)
        
        #for shorter typing:
        n = self.n
        k = self.k
        d = self.d
        
        #set random seed
        np.random.seed(42) #set to 42 for now so results are reproducible

        #initialize centroids by randomly picking k data points as the starting centroids
        np.random.choice(n, k, replace=False) #generate random indices to pick from the input array
        for
        #1. assign data points to a random cluster to initialize the centroids (can also pick k random points as centroids)
        
        #2. optimization
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
        returns the final squared-mean error of the fit model

        outputs:
            float
                the squared-mean error of the fit model
        """
        #take difference between each point and the cluster center, for all of the points, then square that

    def get_centroids(self) -> np.ndarray:
        #you will call this within the fit method to get the centroids
        #assign the final centroids as an attribute of the class so that you can use it in the predict method
        """
        returns the centroid locations of the fit model

        outputs:
            np.ndarray
                a `k x m` 2D matrix representing the cluster centroids of the fit model
        """
        
    #create a function that gets the closest centroid (which is different from the get_centroids method above)
    #def _closest_centroid(self, data point, centroids)
    
    #create a (private) function that creates the clusters given centroids as an argument
    #def _create_clusters(self, centroids)
        #iterate over the actual data points to get the closest centroid to each data point,
        #then assign the data point to the cluster that corresponds to that centroid
    #return clusters
    
    #create a function that gets the Euclidian distance between two vectors
    
    #anything that the user doesn't explicitly need to call, make it a private method/function