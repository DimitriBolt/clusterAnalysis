import gower
import pandas

from clearedData import ClearedData
from rowDataFromFile import RowDataFromFile


class DistanceMatrix:
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __dfClearedCata: pandas.DataFrame = pandas.DataFrame({"Column1": ["a", "c"], "Column2": ["b", "d"]}, index=["Row1", "Row2"], dtype=str)
    __DistanceMatrix: pandas.DataFrame = pandas.DataFrame({"Column1": ["a", "c"], "Column2": ["b", "d"]}, index=["Row1", "Row2"], dtype=str)

    # Constructors
    def __init__(self, cleared_data: ClearedData) -> None:
        self.__dfClearedCata = cleared_data.get_cleared_data()
        self.__DistanceMatrix = self.__gower_distance(self.__dfClearedCata)

    # Methods
    def __gower_distance(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        return gower.gower_matrix(dataframe)

    # Accessor( = getter) methods
    def get_distance_matrix(self) -> pandas.DataFrame:
        return self.__DistanceMatrix


if __name__ == '__main__':
    fileName: str = "/home/dimitri/Загрузки/601285.json"
    rowData: RowDataFromFile = RowDataFromFile(file_name=fileName)  # object must start from lower-case letter
    row_data_json: dict = rowData.get_json()
    clearedData: ClearedData = ClearedData(row_data_json=row_data_json)  # object must start from lower-case letter
    distanceMatrix: DistanceMatrix = DistanceMatrix(cleared_data=clearedData)  # object must start from lower-case letter

    dfOut: pandas.DataFrame = distanceMatrix.get_distance_matrix()
    pass  # Press Ctrl+8 to toggle the breakpoint.
