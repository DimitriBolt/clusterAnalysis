import numpy
import pandas
from sklearn.cluster import DBSCAN

from clearedData import ClearedData
from distanceMatrix import DistanceMatrix
from rowData import RowData


class Clusters:
    # https://towardsdatascience.com/clustering-on-numerical-and-categorical-features-6e0ebcf1cbad
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __distanceMatrix: DistanceMatrix
    __labels: numpy.ndarray

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
        self.__labels = dbscan_cluster.labels_

    # Methods
    # Accessor( = getter) methods
    def get_labels(self) -> pandas.DataFrame:
        return self.__labels


if __name__ == '__main__':
    fileName: str = "/home/dimitri/Загрузки/601285.json"
    rowData: RowData = RowData(file_name=fileName)  # object must start from lower-case letter
    row_data_json: dict = rowData.get_json()
    clearedData: ClearedData = ClearedData(row_data_json=row_data_json)  # object must start from lower-case letter
    dfClearedData: pandas.DataFrame = clearedData.get_cleared_data()
    distanceMatrix: DistanceMatrix = DistanceMatrix(df_cleared_data=dfClearedData)  # object must start from lower-case letter
    clusters: Clusters = Clusters(distance_matrix=distanceMatrix)  # object must start from lower-case letter

    a: numpy.ndarray = clusters.get_labels()
    pass  # Press Ctrl+8 to toggle the breakpoint.
