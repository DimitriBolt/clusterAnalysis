from os.path import expanduser, join

from pandas import DataFrame
from pandas import json_normalize

from rowDataFromFile import RowDataFromFile


class ClearedData:
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __row_data_json: dict = {}
    __cleared_data: DataFrame = None

    # Constructors
    def __init__(self, row_data_json: dict) -> None:
        self.__row_data_json = row_data_json
        row_data_frame = json_normalize(self.__row_data_json, 'data')

        answer_columns = [i for i in row_data_frame.columns if 'answer' in i]
        answer_columns = [i for i in answer_columns if 'raw' not in i]
        answer_columns = [i for i in answer_columns if '.t' not in i]

        self.__cleared_data = row_data_frame[answer_columns]

    # Methods
    # Accessor( = getter) methods
    def get_cleared_data(self) -> DataFrame:
        return self.__cleared_data


if __name__ == '__main__':
    fileName = join(expanduser("~"), "Downloads", "601285.json")
    rowData: RowDataFromFile = RowDataFromFile(file_name=fileName)  # object must start from lower-case letter
    row_data_json: dict = rowData.get_json()
    # it is not! numerical variables, there are categorized features
    # K-means,
    # https://en.wikipedia.org/wiki/Ward%27s_method,
    # https://en.wikipedia.org/wiki/Cluster_analysis#Centroid-based_clustering,
    # https://en.wikipedia.org/wiki/Hierarchical_clustering
    # do not work
    clearedData: ClearedData = ClearedData(row_data_json=row_data_json)  # object must start from lower-case letter

    dfOut: DataFrame = clearedData.get_cleared_data()
    dfOut.to_csv(path_or_buf=join(expanduser("~"), "Downloads", "dataFrame.csv"),
                 sep=",")
    pass  # Press Ctrl+8 to toggle the breakpoint.
