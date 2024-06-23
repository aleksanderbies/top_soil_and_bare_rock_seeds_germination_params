import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import seaborn as sns

def draw_series_plots(df):
    random_rows = df.sample(9)

    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 10))

    for index, (row_index, row) in enumerate(random_rows.iterrows()):
        col_index = index % 3
        ax = axes[index // 3, col_index]
        ax.plot(row)

        ax.set_xlabel('Time')
        ax.set_ylabel('Number of germinated seeds')

        ax.set_xticks([])

    plt.tight_layout()
    plt.show()
    
def draw_time_series(df, col_names, labels, title, y_label, colors=['green', 'orange']):
    plt.figure(figsize=(10,6))
    plt.plot(df[col_names[0]], marker='o', label=labels[0], color=colors[0])
    plt.plot(df[col_names[1]], marker='o', label=labels[1], color=colors[1])

    plt.gca().set_xticks([])
    
    plt.xlabel('Time')
    plt.ylabel(y_label)
    plt.title(title)

    plt.legend()

    plt.show()
    
def draw_time_series_difference_plot(df, col_names, title, _color='green'):    
    plt.figure(figsize=(10,6))
    plt.plot(df[col_names[0]] - df[col_names[1]], marker='o', color=_color)
    
    plt.gca().set_xticks([])

    plt.xlabel('Time')
    plt.ylabel('Difference')

    plt.show()

def draw_histogram(df, col_names, labels, _bins, colors=['green', 'orange']):
    plt.figure(figsize=(10,6))
    plt.hist(df[col_names[0]], bins=_bins, alpha=0.5, label=labels[0], color=colors[0])
    plt.hist(df[col_names[1]], bins=_bins, alpha=0.5, label=labels[1], color=colors[1])

    plt.legend()
    
    plt.xlabel('Germinated Seeds')
    plt.ylabel('Frequency')
    
    plt.show()
    
def draw_histogram_of_differences(df, col_names, labels, _bins, _color='green'):
    plt.figure(figsize=(10,6))
    plt.hist(df[col_names[0]] - df[col_names[1]], bins=_bins, color=_color, alpha=0.7, edgecolor='black')

    plt.xlabel('Difference')
    plt.ylabel('Frequency')
    
    plt.show()
    

def draw_kde_plot(_ts_1, _ts_2, labels, colors=['green', 'orange']):
    plt.figure(figsize=(10,6))
    
    ax_1 = sns.kdeplot(data=_ts_1, common_norm=False, fill=True, color=colors[0], palette='pastel', label=labels[0])
    ax_2 = sns.kdeplot(data=_ts_2, common_norm=False, fill=True, color=colors[1], palette='pastel', label=labels[1])
    
    ax_1.set_xticks([])
    ax_2.set_xticks([])
    
    ax_1.set_yticks([])
    ax_2.set_yticks([])
    
    plt.xlabel('Time')
    plt.ylabel('Number of germinated seeds')       
    plt.legend()
    plt.show()
    
def draw_cumulative_plots(df, col_names, labels, y_label, colors=['green', 'orange']):
    plt.figure(figsize=(10,6))

    plt.plot(df[col_names[0]].cumsum(), label=labels[0], marker='o', color=colors[0])
    plt.plot(df[col_names[1]].cumsum(), label=labels[1], marker='o', color=colors[1])

    plt.gca().set_xticks([])
    
    plt.xlabel('Time')
    plt.ylabel(y_label)
    plt.legend()

    plt.show()