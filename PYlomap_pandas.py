# Heatmap Generation from MicroOrganism Data
# By William Pearson, Hannah Eccleston, and Tristan Manchester

# Import Packages
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
        # create pandas dataframe with all sample's info
        self.excel_sheet = pd.read_excel(self.workbook_name, skiprows=2, sheet_name=self.worksheet_name,
                                         names=['domain', 'phylum', 'classification',
                                                'order', 'family', 'genus'], header=None,
                                         usecols=[0, 1, 2, 3, 4, 5]).join(
            pd.read_excel(self.workbook_name, skiprows=1, sheet_name=self.worksheet_name)[self.sample_name]).rename(
            {self.sample_name: 'relative_abundance'}, axis=1).replace('__', np.nan)


def make_heat_map(datasets, percent_to_ignore=0, max_value=None, pathways=[], line_width_override=0,
                  name_override=None):
    dataset_list = []
    for dataset in datasets:
        microbe_list = (
            dataset.excel_sheet.ffill(axis='columns').drop(['domain', 'phylum', 'classification', 'order', 'family'],
                                                           axis=1).rename(
                {'relative_abundance': dataset.sample_name, 'genus': 'microbe'}, axis=1).set_index(
                'microbe'))
        # ^create a list of microbes with the highest order name and their RA from the dataset
        dataset_list.append(microbe_list)  # add the microbe RA list to the list of datasets

    dataframe = dataset_list[0]  # create a dataframe with the first dataset in the list
    for i in range(1, len(datasets)):
        dataframe[datasets[i].sample_name] = dataset_list[i][
            datasets[i].sample_name]  # create new columns for the RAs from each dataset
    dataframe = dataframe.astype(float).loc[~(dataframe < percent_to_ignore / 100).all(
        axis=1)] * 100  # choose only the data greater than percent_to_ignore, and multiply by 100 for percentage
    dataframe.index.name = None
    # create a dataframe of joined microbe names
    joined_names = pd.DataFrame(pd.read_excel('data.xlsx', skiprows=2,
                                              names=['domain', 'phylum', 'classification',
                                                     'order', 'family', 'genus'], header=None,
                                              usecols=[0, 1, 2, 3, 4, 5]).replace('__', np.nan)[
                                    ['domain', 'phylum', 'classification',
                                     'order', 'family', 'genus']].agg(lambda x: '; '.join(x.dropna().astype(str)),
                                                                      axis=1))
    
    taxon_dict = pd.read_excel('Taxon Dictionary.xlsx') # load taxon dictionary
    parent = pd.read_csv('Parent.csv').set_index('sample') # load parent dictionary
    list_of_unique_taxons_in_pathway = [] 
    list_of_microbes_with_pathway_confidence = []
    colour_lists = []
    colour_maps = []
    colours_to_use = iter([plt.cm.Pastel1(i) for i in range(9)]) # colours to use for pathways on heatmap
    for pathway in pathways: # iterate through pathway argument list
        list_of_unique_taxons_in_pathway.append(
            parent.loc[parent['function'].str.contains(pathway)].taxon.unique().tolist()) # makes list of lists unique taxons for each pathway

    for list_of_unique_taxons in list_of_unique_taxons_in_pathway: # iterates through list of lists of unique taxons for each pathway
        list_of_microbes_with_pathway_confidence.append(
            taxon_dict.loc[taxon_dict['Feature ID'].str.contains('|'.join(list_of_unique_taxons))].sort_values(
                'Confidence', axis=0, ascending=False).drop_duplicates('Taxon').Taxon.to_list()) # finds microbes associated with each taxon and removes duplicates

    for i in range(len(list_of_microbes_with_pathway_confidence)): # makes a list of each colour
        colour_lists.append([next(colours_to_use)] * len(list_of_microbes_with_pathway_confidence[i])) 

    for i in range(len(list_of_microbes_with_pathway_confidence)): # maps colour lists to microbes
        colour_maps.append(
            joined_names[0].map(dict(zip(list_of_microbes_with_pathway_confidence[i], colour_lists[i]))).rename(
                pathways[i]).fillna('white'))

    colour_maps = pd.concat(colour_maps, axis=1) # joins list of colour maps into dataframe

    # Plot Data
    heatmap_plot(dataframe, line_width_override, max_value, colour_maps, name_override)


def heatmap_plot(data, line_width_overide, max_value, colour_maps, name_override):
    if name_override is not None: # override sample names if list of new names argument passed
        data = data.set_axis(name_override, axis=1, inplace=False)
    sns.set(font_scale=1)  # for increasing font size
    plt.figure(figsize=(15, 10), constrained_layout=True, facecolor=None,
               edgecolor=None)  # set figure size, constrain layout to fit size, back background transparent

    sns.clustermap(data.reset_index(drop=True), annot=True, linewidths=line_width_overide, cmap="Blues", vmax=max_value,
                   row_cluster=False, metric="euclidean", method="ward", row_colors=colour_maps,
                   yticklabels=data.index.values)

    plt.show()


data_set_1 = SampleInformation("data.xlsx", "Sheet1", "A")
data_set_2 = SampleInformation("data.xlsx", "Sheet1", "B")
data_set_3 = SampleInformation("data.xlsx", "Sheet1", "C")
data_set_5 = SampleInformation("data.xlsx", "Sheet1", "E")
data_set_6 = SampleInformation("data.xlsx", "Sheet1", "F")

name_override = ['1', '2', '3', '4', '5', '6']
pathways = ['PWY-5431', 'PWY-5430', 'SO4ASSIM-PWY', 'PWY-7446']

make_heat_map([data_set_1, data_set_2, data_set_3, data_set_4, data_set_5, data_set_6], percent_to_ignore=3, max_value=None,
              pathways=pathways, name_override=name_override)
