from os.path import expanduser, join

import gower
import numpy
import pandas
from numpy import ndarray, savetxt

from clearedData import ClearedData
from rowDataFromFile import RowDataFromFile


class DistanceMatrix:
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __dfClearedCata: pandas.DataFrame = pandas.DataFrame({"Column1": ["a", "c"], "Column2": ["b", "d"]}, index=["Row1", "Row2"], dtype=str)
    __distanceMatrix: ndarray

    # Constructors
    def __init__(self, cleared_data: ClearedData) -> None:
        self.__dfClearedCata = cleared_data.get_cleared_data()
        self.__distanceMatrix = self.__gower_distance(self.__dfClearedCata)
        pass

    # Methods
    def __gower_distance(self, dataframe: pandas.DataFrame) -> ndarray:
        return gower.gower_matrix(dataframe)

    # Accessor( = getter) methods
    def get_distance_matrix(self) -> ndarray:
        return self.__distanceMatrix
        pass


if __name__ == '__main__':
    fileName = join(expanduser("~"), "Downloads", "601285.json")
    rowData: RowDataFromFile = RowDataFromFile(file_name=fileName)  # object must start from lower-case letter
    row_data_json: dict = rowData.get_json()
    clearedData: ClearedData = ClearedData(row_data_json=row_data_json)  # object must start from lower-case letter
    distanceMatrix: DistanceMatrix = DistanceMatrix(cleared_data=clearedData)  # object must start from lower-case letter

    arrayOut: ndarray = distanceMatrix.get_distance_matrix()
    savetxt(fname=join(expanduser("~"), "Downloads", "distanceMatrix.csv"),
            X=arrayOut,
            fmt='%1.2f',
            delimiter=",")

    pass  # Press Ctrl+8 to toggle the breakpoint.
