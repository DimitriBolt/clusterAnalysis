import pandas

from rowDataFromFile import RowDataFromFile


class ClearedData:
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __row_data_json: dict = {}
    __cleared_data: pandas.DataFrame = None

    # Constructors
    def __init__(self, row_data_json: dict) -> None:
        self.__row_data_json = row_data_json
        row_data_frame = pandas.json_normalize(self.__row_data_json, 'data')
        answer_columns = [i for i in row_data_frame.columns if 'answer' in i]
        self.__cleared_data = row_data_frame[answer_columns]

    # Methods
    # Accessor( = getter) methods
    def get_cleared_data(self) -> pandas.DataFrame:
        return self.__cleared_data


if __name__ == '__main__':
    fileName: str = "/home/dimitri/Загрузки/601285.json"
    rowData: RowDataFromFile = RowDataFromFile(file_name=fileName)  # object must start from lower-case letter
    row_data_json: dict = rowData.get_json()
    clearedData: ClearedData = ClearedData(row_data_json=row_data_json)  # object must start from lower-case letter

    dfOut: pandas.DataFrame = clearedData.get_cleared_data()
    pass  # Press Ctrl+8 to toggle the breakpoint.
