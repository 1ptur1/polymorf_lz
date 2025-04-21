
import pandas as pd
class Arbuz:
    def __init__(self):
        self.name = pd.read_csv('var10.csv')

    def divide(self):
        self.filtered_df_min = self.name[self.name['Сумма cash-back'] == 0]
        self.filtered_df_max = self.name[self.name['Сумма cash-back'] > 0]
        self.filtered_df_min.to_csv('cash_zero.csv', index=False)
        self.filtered_df_max.to_csv('cash_ne_zero.csv', index=False) 


    def __invert__(self):
        self.df_no_duplicates = self.name.drop_duplicates()
        self.a = len(self.name)
        self.b = len(self.df_no_duplicates)
        self.duplicates = self.a - self.b
        print("Кол-во дубликатов - ",self.duplicates )
        self.df_no_duplicates.to_csv('df_no_duplicates.csv', index=False) 


    def __del__(self):
        print("del")

def main():
    a = Arbuz()
    a.divide()
    ~a
if __name__ == "__main__":
    main()