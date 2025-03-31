import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, dataframe):
        self.df = dataframe
        self.figures = []
    
    def add_histogram(self, column, bins=10, title=None):
        """Добавление гистограммы"""
        fig, ax = plt.subplots()
        self.df[column].hist(bins=bins, ax=ax)
        ax.set_title(title or f'Гистограмма для {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Частота')
        self.figures.append(fig)
        return fig
    
    def add_line_plot(self, x_column, y_column, title=None):
        """Добавление линейного графика"""
        fig, ax = plt.subplots()
        self.df.plot.line(x=x_column, y=y_column, ax=ax)
        ax.set_title(title or f'Линейный график {y_column} по {x_column}')
        self.figures.append(fig)
        return fig
    
    def add_scatter_plot(self, x_column, y_column, title=None):
        """Добавление диаграммы рассеяния"""
        fig, ax = plt.subplots()
        self.df.plot.scatter(x=x_column, y=y_column, ax=ax)
        ax.set_title(title or f'Диаграмма рассеяния {y_column} по {x_column}')
        self.figures.append(fig)
        return fig
    
    def show_all(self):
        """Показать все графики"""
        plt.show()
    
    def clear(self):
        """Очистить все сохраненные графики"""
        self.figures = []
        plt.close('all')