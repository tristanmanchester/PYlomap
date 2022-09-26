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

        # create pandas dataframe with all sample's info:
        # reads excel sheet from workbook name, skips first 2 rows
        # takes only the first 5 columns and names them domain, pylum etc
        # joins that to a new dataframe of just RA column, this time skips 1 row so sample name isn't removed from sheet
        # renames new column relative abundance and replaces __ values with numpy NaN

        self.excel_sheet = pd.read_excel(self.workbook_name, skiprows=2, sheet_name=self.worksheet_name,
                                         names=['domain', 'phylum', 'classification',
                                                'order', 'family', 'genus'], header=None,
                                         usecols=[0, 1, 2, 3, 4, 5]).join(
            pd.read_excel(self.workbook_name, skiprows=1, sheet_name=self.worksheet_name)[self.sample_name]).rename(
            {self.sample_name: 'relative_abundance'}, axis=1).replace('__', np.nan)


def create_datasets(data_excel_file=None, sample_list=None):
    dataset_list = []
    for sample in sample_list:
        dataset_list.append(SampleInformation(data_excel_file, 'Sheet1', sample))
    return dataset_list

# custom aitchison distance for distance metric https://www.frontiersin.org/articles/10.3389/fmicb.2017.02224/full
def aitchison(u, v):
  # sets 0% values to very small finite numbers because the aitchison caluclation has a log in there somewhere 
  u[u == 0] = 0.000000001
  v[v == 0] = 0.000000001
  dist =  euclidean(clr(u), clr(v))
  return dist

def make_heat_map(datasets, percent_to_ignore=0, max_value=None, pathways=None, name_override=None, pathway_search=None, 
                  save_fig=False, latex_table=False, taxon_dict=None, function_dict=None, parent=None, data_excel_file=None, group_by=None):

    # if user doesn't want to group by taxon:
    # creates a dataframe with lowest taxon available for each microbe and columns of relative abundances for each sample name
    # if they specify a taxon, groups all microbes with matching taxon names and sums their relative abundances

    if group_by is None:
      list = []
      for dataset in datasets:
        list.append(dataset.excel_sheet_sample_name[dataset.sample_name])
      dataframe = datasets[0].excel_sheet_sample_name.join(list[1:]).ffill(axis='columns').drop(['domain', 'phylum', 'classification', 'order', 'family'],
                                                            axis=1).rename(
                  {'genus': 'microbe'}, axis=1).set_index(
                  'microbe')
      dataframe = dataframe.astype(float).loc[~(dataframe < percent_to_ignore / 100).all(axis=1)] * 100
    else:
      list = []
      for dataset in datasets:
        list.append(dataset.excel_sheet_sample_name[dataset.sample_name])
      dataframe = datasets[0].excel_sheet_sample_name.join(list[1:]).groupby(group_by).sum()
      dataframe = dataframe.astype(float).loc[~(dataframe < percent_to_ignore / 100).all(axis=1)] * 100

    # creates a dataframe of joined microbe names as they appear in taxon dictionary

    joined_names = pd.DataFrame(pd.read_excel(data_excel_file, skiprows=2,
                                              names=['domain', 'phylum', 'classification',
                                                     'order', 'family', 'genus'], header=None,
                                              usecols=[0, 1, 2, 3, 4, 5]).replace('__', np.nan)[
                                    ['domain', 'phylum', 'classification',
                                     'order', 'family', 'genus']].agg(lambda x: '; '.join(x.dropna().astype(str)),
                                                                      axis=1))

    # loads taxon dictionary, function dictionary, and parent file into dataframes
    # parent file is as csv because it's a bit faster
    # initiates some lists to use and makes a list of nice pastel colours for the function labels on the heatmap

    taxon_dict = pd.read_excel(taxon_dict)
    parent = pd.read_csv(parent).set_index('sample')  # set index as sample for easy indexing
    list_of_unique_taxons_in_pathway = []
    list_of_microbes_with_pathway_confidence = []
    colour_lists = []
    colour_maps = []
    pathways_table = None
    colours_to_use = iter([plt.cm.Pastel1(i) for i in range(9)])
    function_dictionary = pd.read_excel(function_dict,
                                        skiprows=1)

    # if the user entered a pathway search term:
    # looks in the function dictionary description column for this substring
    # .pathway selects only pathway name column, .tolist turns column into a list of search results
    # if there's too many search results, it picks the top 9 (there's only 9 pastel colours lol)

    if pathway_search is not None:
        pathways = function_dictionary[['pathway', 'description']].loc[
            function_dictionary['description'].str.contains(pathway_search,
                                                            case=False)].pathway.tolist()
        if len(pathways) > 9:
            pathways = pathways[0:9]

    # takes pathways variable (either from search or from user entered list of pathways)
    # iterates through the list of pathway names
    # gets pathway with description from function dictionary and adds it to a list
    # looks in the parent file for these pathways, makes a list of unique taxons associated with each pathway

    if pathways is not None:
        pathways_description_list = []
        for pathway in pathways:
            pathway_with_description = function_dictionary[['pathway', 'description']].loc[
                function_dictionary['pathway'].str.contains(pathway)]
            pathways_description_list.append(
                pathway_with_description)

            list_of_unique_taxons_in_pathway.append(
                parent.loc[parent['function'].str.contains(
                    pathway)].taxon.unique().tolist())

    # concatenate list of pathway descriptions into dataframe for LaTex table generation

        pathways_table = pd.concat(pathways_description_list)

    # iterates through list of lists of unique taxons for each pathway
    # checks for these taxons in taxon dictionary to find specific microbes they're associated with
    # sorts by confidence and then drops duplicate microbes
    # result is list of microbes associated with each pathway

        for list_of_unique_taxons in list_of_unique_taxons_in_pathway:
            list_of_microbes_with_pathway_confidence.append(
                taxon_dict.loc[taxon_dict['Feature ID'].str.contains('|'.join(list_of_unique_taxons))].sort_values(
                    'Confidence', axis=0, ascending=False).drop_duplicates(
                    'Taxon').Taxon.to_list())

        for i in range(len(list_of_microbes_with_pathway_confidence)):  # makes a list of each colour
            colour_lists.append([next(colours_to_use)] * len(list_of_microbes_with_pathway_confidence[i]))

        for i in range(len(list_of_microbes_with_pathway_confidence)):  # maps colour lists to microbes
            colour_maps.append(
                joined_names[0].map(dict(zip(list_of_microbes_with_pathway_confidence[i], colour_lists[i]))).rename(
                    pathways[i]).fillna('white'))

        colour_maps = pd.concat(colour_maps, axis=1)  # joins list of colour maps into dataframe
    else:
        colour_maps = None

    if latex_table:  # checks if user wants a LaTex table of pathways and descriptions
        if 'pathways_table' in locals():  # checks if pathways are used and creates LaTex table of descriptions
            pathways_table.columns = pathways_table.columns.str.title()
            with pd.option_context("max_colwidth", 1000):
              print(pathways_table.to_latex(index=False))  # prints the LaTex code

    # Plot Data
    sample_names = []

    # create list of sample names for save figure
    # add list of sample names and list of pathways to save name
    # result is the filename contains all sample info and pathway info

    for i in datasets:
        sample_name = i.sample_name
        sample_names.append(sample_name)
    if pathways is not None:
      save_name = f'[{"; ".join(sample_names)}] - [{"; ".join(pathways)}]'
    else:
      save_name = f'[{"; ".join(sample_names)}]'

    # calls heatmap plot function, passes it dataframe (top level microbe names, sample name columns, relative abundances)
    # passes it max value for heatmap colour bar, any name overrides, whether or not to save fig, and the name to save it by

    heatmap_plot(dataframe, max_value, colour_maps, name_override, save_fig, save_name, group_by)

def heatmap_plot(data, max_value, colour_maps, name_override, save_fig=False, save_name=None, group_by=None):
    if name_override is not None:  # override sample names if list of new names argument passed
        data = data.set_axis(name_override, axis=1, inplace=False)
    sns.set(font_scale=1)  # for increasing font size

    # creates cluster map which is a heatmap with a dendrogram showing sample similarity based on microbe abundances
    # row_colours creates columns showing which of the chosen pathways are associated with each microbe
    # pathways are not shown if they specified a lower taxon (not really useful)
    if group_by is None:
      g = sns.clustermap(data=data.reset_index(drop=True), annot=data.reset_index(drop=True), linewidths=0, cmap="Blues", vmax=max_value,
                        row_cluster=False, metric=aitchison, method="complete", row_colors=colour_maps,
                        yticklabels=data.index.values, cbar_kws={'orientation': 'horizontal'})
    else:
      g = sns.clustermap(data=data.reset_index(drop=True), annot=data.reset_index(drop=True), linewidths=0, cmap="Blues", vmax=max_value,
                        row_cluster=True, metric=aitchison, method="complete",
                        yticklabels=data.index.values, cbar_kws={'orientation': 'horizontal'})

    # puts the colour bar at the bottom and gives it a title

    g.ax_cbar.set_position([g.ax_heatmap.get_position().x0 + 0.25 * g.ax_heatmap.get_position().width,
                            g.ax_heatmap.get_position().y0 - 0.09, g.ax_heatmap.get_position().width * 0.5, 0.02])
    g.ax_cbar.set_title('Percent abundance')

    # if the user wants, saves a high resolution png file

    if save_fig:
        plt.savefig(save_name, dpi=300, bbox_inches='tight')

# Data
data_excel_file = 'data.xlsx'  # excel file containing sample relative abundances 
sample_list = ['sample1', 'sample2', 'sample3', 'sample4', 'sample5', 'sample6']  # which samples you wish to use from the data

# Dictionaries 
taxon_dict = 'Taxon Dictionary.xlsx'  # taxon dictionary in excel format
function_dict = 'Function Dictionary.xlsx'  # function dictionary in excel format
parent = 'FL Parent.csv'  # parent file in csv format 

# Pathways
pathways = ['PWY-5430', 'PWY-5431', 'PWY-7431', 'PWY-1361']  # define a list of custom pathway names ['pathway-1', 'pathway-2']
pathway_search = None  # search for a string in pathway descriptions, first 9 matching pathways are plotted 

# Heatmap and LaTex options
percent_to_ignore = 2  # lower bound for percentages displayed on heat map
max_value = None  # max value represented on heat map: all higher values have the same colour
name_override = None  # override sample names on heat map ['sample 1', 'sample 2']
save_fig = False  # saves heat map as png
latex_table = False  # output LaTex table with pathways and descriptions

dataset_list = create_datasets(data_excel_file, sample_list)
make_heat_map(dataset_list, percent_to_ignore, max_value, pathways, name_override, pathway_search, 
              save_fig, latex_table, taxon_dict, function_dict, parent, data_excel_file)
