import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Arbuz:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Загружает данные из CSV """
        self.df = pd.read_csv(self.file_path)
        print("Данные загружены успешно!")

    def filter_cash(self, back_to_keep):
        """Фильтрует данные по списку штатов"""
        if self.df is None:
            print("Ошибка: данные не загружены!")
            return None
        self.df = self.df[self.df["CASH"].isin(back_to_keep)]
        print("Фильтрация завершена!")