import pandas
import pandas as pd
import gower
from sklearn.cluster import DBSCAN


import numpy as np
from numpy import ndarray
from sklearn.linear_model import LinearRegression


class RegressionExercise:
    #  Initializer выполняется перед! основной программой.
    #  Private Instance or static Class attribute. Переменные должны начинаться с двух подчеркиваний.
    __dfInstanceMatrix: pandas.DataFrame = pandas.DataFrame({"Column1": ["a", "c"], "Column2": ["b", "d"]},
                                                            index=["Row1", "Row2"], dtype=str)

    # Constructors
    def __init__(self, df_outer_matrix: pandas.DataFrame) -> None:
        self.__dfInstanceMatrix = df_outer_matrix

    # Methods
    def ordinary_method(self, x: ndarray, y: ndarray, x_new: ndarray) -> pandas.DataFrame:
        model = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=-1)
        model.fit(x, y)
        r_sq = model.score(x, y)
        print(f"coefficient of determination: {r_sq}")
        print(f"intercept:: {model.intercept_}")
        print(f"slope: {model.coef_}")

        y_pred = model.predict(x)
        print(f"predicted response:\n {y_pred}", sep='\n')

        y_pred = model.intercept_ + model.coef_ * x
        print(f"predicted response:\n {y_pred}", sep='\n')

        print(f"x_new:\n {x_new}", sep='\n')
        y_new: ndarray = model.predict(x_new)
        print(f"y_new:\n {y_new}", sep='\n')

        return 2 * self.__dfInstanceMatrix

    # Accessor( = getter) methods
    def get__df_instance_matrix(self) -> pandas.DataFrame:
        return self.__dfInstanceMatrix


if __name__ == '__main__':
    Column1: dict = {"Row1": 1, "Row2": 3}
    dfIn: pandas.DataFrame = pandas.DataFrame({"Column1": Column1, "Column2": {"Row1": 2, "Row2": 4}})  # Dict of Dicts
    dfElement: int = dfIn["Column2"]["Row1"]
    regressionExercise: RegressionExercise = RegressionExercise(
        df_outer_matrix=dfIn)  # object must start from lower-case letter
    x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
    y = np.array([5, 20, 14, 32, 22, 38])
    x_new: ndarray = np.arange(5).reshape((-1, 1))
    dfOut: pandas.DataFrame = regressionExercise.ordinary_method(x=x, y=y, x_new=x_new)

    dfOut: pandas.DataFrame = regressionExercise.get__df_instance_matrix()

    # Creating a dictionary with the data
    dictionary = {"age": [22, 25, 30, 38, 42, 47, 55, 62, 61, 90],
                  "gender": ["M", "M", "F", "F", "F", "M", "M", "M", "M", "M"],
                  "civil_status": ["SINGLE", "SINGLE", "SINGLE", "MARRIED", "MARRIED", "SINGLE", "MARRIED", "DIVORCED", "MARRIED", "DIVORCED"],
                  "salary": [18000, 23000, 27000, 32000, 34000, 20000, 40000, 42000, 25000, 70000],
                  "has_children": [False, False, False, True, True, False, False, False, False, True],
                  "purchaser_type": ["LOW_PURCHASER", "LOW_PURCHASER", "LOW_PURCHASER", "HEAVY_PURCHASER", "HEAVY_PURCHASER", "LOW_PURCHASER", "MEDIUM_PURCHASER", "MEDIUM_PURCHASER", "MEDIUM_PURCHASER", "LOW_PURCHASER"]}

    # Creating a Pandas DataFrame from the dictionary
    dataframe = pd.DataFrame.from_dict(dictionary)
    dataframe.index = ["Customer 1", "Customer 2", "Customer 3", "Customer 4", "Customer 5", "Customer 6", "Customer 7", "Customer 8", "Customer 9", "Customer 10"]
    distance_matrix = gower.gower_matrix(dataframe)

    # Configuring the parameters of the clustering algorithm
    dbscan_cluster = DBSCAN(eps=0.3,
                            min_samples=2,
                            metric="precomputed")
    # Fitting the clustering algorithm
    dbscan_cluster.fit(distance_matrix)
    # Adding the results to a new column in the dataframe
    dataframe["cluster"] = dbscan_cluster.labels_


    pass  # Press Ctrl+8 to toggle the breakpoint.
