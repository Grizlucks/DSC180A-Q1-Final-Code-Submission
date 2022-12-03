import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from IPython.display import Markdown, display
import seaborn as sns



def create_visualizations(inpath, outpath):
    # read df 19 from inpath
    df_19 = pd.read_csv(f"{outpath}/df_panel_19.csv")
    # read df 20 from inpath
    df_20 = pd.read_csv(f"{outpath}/df_panel_20.csv")
    
    
    high_ch = df_19[df_19['CHOLDX'] == 1]
    coronary = df_19[df_19['CHDDX'] == 1]

    race = df_19['RACE']
    
    non_categorical = ['AGE', 'K6SUM42', 'MCS42', 'PCS42', 'PERWT15F']

    #Non-Whites with Health Insurance
    df_19[race == 'Non-White']['INSCOV'].value_counts().rename({1: 'Private', 2: 'Public', 3: 'Uninsured'}) .plot(kind='barh', title='Non-White Individuals Health Insurance Status')
    plt.savefig('test/results/visualizations/non_white_health_ins.jpg')
    plt.close()

    #White with Health Insurance
    df_19[race != 'Non-White']['INSCOV'].value_counts().rename({1: 'Private', 2: 'Public', 3: 'Uninsured'}).plot(kind='barh', title='White Individuals Health Insurance Status')
    plt.savefig('test/results/visualizations/white_health_ins.jpg')
    plt.close()

    #High Cholesterol Pressure by Age
    high_ch.groupby(by="AGE").size().plot(kind='line', title='High Cholesterol Pressure by Age')
    plt.savefig('test/results/visualizations/cholesterol_by_age.jpg')
    plt.close()

    #Coronary Heart Disease by Age
    coronary.groupby(by="AGE").size().plot(kind='line', title='Coronary Heart Disease by Age')
    plt.savefig('test/results/visualizations/heart_disease_by_age.jpg')
    plt.close()
    
    # Correlation plot 1
    corr_plot_19 = pd.plotting.scatter_matrix(df_19[np.append(non_categorical, 'UTILIZATION') ])
    plt.savefig('test/results/visualizations/correlation_19.jpg')
    plt.close()

    # Correlation plot 2
    corr_plot_20 = pd.plotting.scatter_matrix(df_20[np.append(non_categorical, 'UTILIZATION') ])
    plt.savefig('test/results/visualizations/correlation_20.jpg')
    plt.close()
    
