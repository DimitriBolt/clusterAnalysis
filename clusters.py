from os.path import expanduser, join

import pandas
import argparse

from numpy import ndarray, savetxt
from sklearn.cluster import DBSCAN

from clearedData import ClearedData
from distanceMatrix import DistanceMatrix
from rowDataFromFile import RowDataFromFile
from rowDataFromURL import RowDataFromURL


class Clusters:
    # https://towardsdatascience.com/clustering-on-numerical-and-categorical-features-6e0ebcf1cbad
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __distanceMatrix: DistanceMatrix
    __clusterLabels: ndarray

    # Constructors
    def __init__(self, distance_matrix: DistanceMatrix) -> None:
        self.__distanceMatrix = distance_matrix
        # Configuring the parameters of the clustering algorithm
        dbscan_cluster = DBSCAN(eps=0.3,
                                min_samples=2,
                                metric="precomputed")
        # Fitting the clustering algorithm
        dbscan_cluster.fit(distance_matrix.get_distance_matrix())
        # Adding the results to a new column in the dataframe
        self.__clusterLabels = dbscan_cluster.labels_

    # Methods
    # Accessor( = getter) methods
    def get_cluster_labels(self) -> ndarray:
        return self.__clusterLabels


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cl parameters about data source')
    parser.add_argument('--path', '-p',
                        dest="path",
                        type=str,
                        help="path to JSON-result of the survey")
    args = parser.parse_args()
    if args.path is None:
        rowData: RowDataFromURL = RowDataFromURL(url="https://raw.githubusercontent.com/DimitriBolt/clusterAnalysis/master/data/601285.json")  # object must start from lower-case letter
    else:
        rowData: RowDataFromFile = RowDataFromFile(file_name=args.path)
    clearedData: ClearedData = ClearedData(row_data_json=rowData.get_json())  # object must start from lower-case letter
    distanceMatrix: DistanceMatrix = DistanceMatrix(cleared_data=clearedData)  # object must start from lower-case letter
    clusters: Clusters = Clusters(distance_matrix=distanceMatrix)  # object must start from lower-case letter

    clusterLabels: ndarray = clusters.get_cluster_labels()
    savetxt(fname=join(expanduser("~"), "Downloads", "clusterLabels.csv"),
            X=clusterLabels,
            fmt='%d',
            delimiter=",")
    pass  # Press Ctrl+8 to toggle the breakpoint.
