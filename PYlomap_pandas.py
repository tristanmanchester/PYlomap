import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class SampleInformation:
    def __init__(self, workbook_name, worksheet_name, sample_name):
        self.workbook_name = workbook_name
        self.worksheet_name = worksheet_name
        self.sample_name = sample_name
        self.name_override = None
        self.microorganism_tree = []
        self.excel_sheet = None

    def determine_microorganisms(self):
        # create pandas dataframe with all sample's info
        self.excel_sheet = pd.read_excel(self.workbook_name, skiprows=2, sheet_name=self.worksheet_name,
                                         names=['domain', 'phylum', 'classification',
                                                'order', 'family', 'genus'], header=None,
                                         usecols=[0, 1, 2, 3, 4, 5]).join(
            pd.read_excel(self.workbook_name, skiprows=1, sheet_name=self.worksheet_name)[self.sample_name]).rename(
            {self.sample_name: 'relative_abundance'}, axis=1).replace('__', np.nan)


def make_heat_map(datasets, line_width_override=0, percent_to_ignore=0, max_value=None):
    dataset_list = []
    for dataset in datasets:
        microbe_list = (
            dataset.excel_sheet.ffill(axis='columns').drop(['domain', 'phylum', 'classification', 'order', 'family'],
                                                           axis=1).rename({'relative_abundance': dataset.sample_name,
                                                                           'genus': 'microbe'}, axis=1).set_index(
                'microbe'))  # create a list of microbes with the highest order name and their RA from the dataset
        dataset_list.append(microbe_list)  # add the microbe RA list to the list of datasets

    dataframe = dataset_list[0]  # create a dataframe with the first dataset in the list
    for i in range(1, len(datasets)):
        dataframe[datasets[i].sample_name] = dataset_list[i][
            datasets[i].sample_name]  # create new columns for the RAs from each dataset
    dataframe = dataframe.astype(float).loc[~(dataframe < percent_to_ignore / 100).all(
        axis=1)] * 100  # choose only the data greater than percent_to_ignore, and multiply by 100 for percentage
    dataframe.index.name = None

    # Plot Data
    heatmap_plot(dataframe, line_width_override, max_value)


def heatmap_plot(data, line_width_overide, max_value):
    sns.set(font_scale=1.)  # for increasing font size
    plt.figure(figsize=(10, 10), constrained_layout=True, facecolor=None,
               edgecolor=None)  # set figure size, constrain layout to fit size, back background transparent
    p = sns.heatmap(data, annot=True, linewidths=line_width_overide, cmap="YlGnBu", yticklabels=True,
                    vmax=max_value)  # vmax is the highest value displayed, all higher values take the same colour
    p.set_xlabel('Sample')  # set x axis label
    plt.show()
    # plt.savefig('heatmap.png', dpi=100, pad_inches=1, transparent=True)


dataSet1 = SampleInformation("/content/drive/MyDrive/pylomap/data.xlsx", "Sheet1", "sample1")
dataSet2 = SampleInformation("/content/drive/MyDrive/pylomap/data.xlsx", "Sheet1", "sample2")
dataSet3 = SampleInformation("/content/drive/MyDrive/pylomap/data.xlsx", "Sheet1", "sample3")
dataSet4 = SampleInformation("/content/drive/MyDrive/pylomap/data.xlsx", "Sheet1", "sample4")
dataSet1.determine_microorganisms()
dataSet2.determine_microorganisms()
dataSet3.determine_microorganisms()
dataSet4.determine_microorganisms()

make_heat_map([dataSet1, dataSet2, dataSet3, dataSet4], percent_to_ignore=1, max_value=15)
