import matplotlib.pyplot as plt
import pandas as pd
from typing import Optional, List

class DataVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.figures: List[plt.Figure] = []

    def add_histogram(self, column: str, bins: int = 10, title: Optional[str] = None) -> plt.Figure:
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df[column].hist(bins=bins, ax=ax, edgecolor='black', alpha=0.7)
        ax.set_title(title or f'Гистограмма: {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Частота')
        ax.grid(True, linestyle='--', alpha=0.5)
        self.figures.append(fig)
        return fig

    def add_line_plot(self, x_column: str, y_column: str, title: Optional[str] = None) -> plt.Figure:
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df.plot(x=x_column, y=y_column, ax=ax, marker='o', linestyle='-', color='blue')
        ax.set_title(title or f'Линейный график: {y_column} от {x_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.xticks(rotation=45)
        self.figures.append(fig)
        return fig

    def add_scatter_plot(self, x_column: str, y_column: str, color_column: Optional[str] = None, 
                         title: Optional[str] = None) -> plt.Figure:
        fig, ax = plt.subplots(figsize=(10, 6))
        if color_column:
            scatter = ax.scatter(
                x=self.df[x_column], 
                y=self.df[y_column], 
                c=self.df[color_column], 
                cmap='viridis', 
                alpha=0.7
            )
            plt.colorbar(scatter, label=color_column)
        else:
            ax.scatter(
                x=self.df[x_column], 
                y=self.df[y_column], 
                color='green', 
                alpha=0.7
            )
        ax.set_title(title or f'Диаграмма рассеяния: {y_column} от {x_column}')
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.grid(True, linestyle='--', alpha=0.5)
        self.figures.append(fig)
        return fig

    def show_all_figures(self):
        for fig in self.figures:
            plt.figure(fig.number)
            plt.tight_layout()
            plt.show()
