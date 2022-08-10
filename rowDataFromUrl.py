import argparse

import pandas
import json
import requests


class RowDataFromUrl:
    # хранит в себе данные из JSON в формате DataFrame
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __url: str = "/home/dimitri/Загрузки/601285.json"
    __data: dict = None

    # Constructors
    def __init__(self, url: str = "https://raw.githubusercontent.com/DimitriBolt/clusterAnalysis/master/data/601285.json") -> None:
        self.__url = url
        response = requests.get(self.__url)
        # returns JSON object as a dictionary
        s = response.text
        self.__data = json.loads(s=s)

    # Methods
    # Accessor( = getter) methods
    def get_json(self) -> pandas.DataFrame:
        print(f"JSON fetched from URL {self.__url}")
        return self.__data


if __name__ == '__main__':
    URL: str = "https://raw.githubusercontent.com/DimitriBolt/clusterAnalysis/master/data/601285.json"
    rowData: RowDataFromUrl = RowDataFromUrl(url=URL)  # object must start from lower-case letter

    dictOut: dict = rowData.get_json()

    pass  # Press Ctrl+8 to toggle the breakpoint.
