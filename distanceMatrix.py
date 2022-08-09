import gower
import pandas

from clearedData import ClearedData
from rowData import RowData


class DistanceMatrix:
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __dfClearedCata: pandas.DataFrame = pandas.DataFrame({"Column1": ["a", "c"], "Column2": ["b", "d"]}, index=["Row1", "Row2"], dtype=str)
    __DistanceMatrix: pandas.DataFrame = pandas.DataFrame({"Column1": ["a", "c"], "Column2": ["b", "d"]}, index=["Row1", "Row2"], dtype=str)

    # Constructors
    def __init__(self, df_cleared_data: pandas.DataFrame) -> None:
        self.__dfClearedCata = df_cleared_data
        self.__DistanceMatrix = self.__gower_distance(self.__dfClearedCata)

    # Methods
    def __gower_distance(self, dataframe: pandas.DataFrame) -> pandas.DataFrame:
        return gower.gower_matrix(dataframe)

    # Accessor( = getter) methods
    def get_distance_matrix(self) -> pandas.DataFrame:
        return self.__DistanceMatrix


if __name__ == '__main__':
    fileName: str = "/home/dimitri/Загрузки/601285.json"
    rowData: RowData = RowData(file_name=fileName)  # object must start from lower-case letter
    row_data_json: dict = rowData.get_json()
    clearedData: ClearedData = ClearedData(row_data_json=row_data_json)  # object must start from lower-case letter
    dfClearedData: pandas.DataFrame = clearedData.get_cleared_data()
    distanceMatrix: DistanceMatrix = DistanceMatrix(df_cleared_data=dfClearedData)  # object must start from lower-case letter
    dfOut: pandas.DataFrame = distanceMatrix.get_distance_matrix()
    pass  # Press Ctrl+8 to toggle the breakpoint.
