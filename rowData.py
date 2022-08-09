import pandas
import json


class RowData:
    # хранит в себе данные из JSON в формате DataFrame
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __fileName: str = "/home/dimitri/Загрузки/601285.json"
    __data: dict = None

    # Constructors
    def __init__(self, file_name: str = "/home/dimitri/Загрузки/601285.json") -> None:
        self.__fileName = file_name
        # Opening JSON file
        f = open(self.__fileName)
        # returns JSON object as
        # a dictionary
        self.__data = json.load(f)
        # Closing file
        f.close()

    # Methods
    # Accessor( = getter) methods
    def get_json(self) -> pandas.DataFrame:
        return self.__data


if __name__ == '__main__':
    fileName: str = "/home/dimitri/Загрузки/601285.json"
    rowData: RowData = RowData(file_name=fileName)  # object must start from lower-case letter
    dfOut: pandas.DataFrame = rowData.get_json()
    pass  # Press Ctrl+8 to toggle the breakpoint.
