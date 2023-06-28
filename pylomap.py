# Heatmap Generation from MicroOrganism Data
# By William Pearson, Hannah Eccleston, and Tristan Manchester

from scipy.spatial.distance import euclidean
from skbio.stats.composition import clr
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

class Sample:
    """
    Sample Class.
    
    This class represents a biological sample, characterized by its name, taxa, abundances,
    and pathways.

    Attributes
    ----------
    sample_name : str
        The name of the sample.
    taxa : pandas.DataFrame
        The taxa present in the sample.
    abundances : list
        The abundances of each taxon in the sample.
    pathways : dict
        The metabolic pathways present in the sample.
    """

    def __init__(self, sample_name, taxa, abundances):
        self.sample_name = sample_name
        self.taxa = taxa
        self.abundances = abundances
        self.pathways = {}

class CreateSamples:
    """
    CreateSamples Class.

    This class is used to create a list of Sample objects from provided data.

    Attributes
    ----------
    all_sample_data : pandas.DataFrame
        The data containing all sample information.
    taxon_dict : pandas.DataFrame
        The dictionary mapping taxa to their IDs.
    parent : pandas.DataFrame
        The parent data.
    samples : list
        The list of Sample objects created.
    """

    def __init__(self, all_sample_data, taxon_dict, parent):
        self.all_sample_data = all_sample_data
        self.taxon_dict = taxon_dict
        self.parent = parent
        self.samples = []

    def create(self, sample_names=None):
        """
        Create Sample objects from data.

        If a list of sample names is provided, it creates Sample objects for those samples.
        If no list is provided, it creates Sample objects for all samples in the data.

        Parameters
        ----------
        sample_names : list, optional
            The names of the samples to create objects for.

        Returns
        -------
        list
            A list of Sample objects.
        """

        if sample_names is None:  # If no list of sample names is provided, use all sample names
            sample_names = self.all_sample_data.columns[1:]

        for sample in sample_names:
            if sample not in self.all_sample_data.columns:
                raise ValueError(f"No data found for sample: {sample}")

            # Select the data for this sample and remove rows with NaN abundances
            sample_data = self.all_sample_data[['Taxon', sample]]
            sample_data = sample_data[sample_data[sample].notna()]  

            taxa = sample_data['Taxon'].tolist()
            abundances = sample_data[sample].tolist()

            # Create a DataFrame for each sample with Taxon as one column and Taxon ID as the other column
            taxa_df = pd.DataFrame(taxa, columns=['Taxon'])
            taxa_df['Taxon ID'] = taxa_df['Taxon'].map(self.taxon_dict.set_index('Taxon')['Taxon ID'].to_dict())

            # Create a Sample object for this sample and append it to the list of samples
            sample_obj = Sample(sample, taxa_df, abundances)
            self.samples.append(sample_obj)

        return self.samples


class Microbe:
    """
    Microbe Class.
    
    This class represents a microbial taxon, characterized by its taxon_id and associated pathways.

    Attributes
    ----------
    taxon_id : str
        The unique identifier for the microbe.
    pathways : list
        The metabolic pathways associated with the microbe.
    """

    def __init__(self, taxon_id, pathways):
        self.taxon_id = taxon_id
        self.pathways = pathways  # List of pathways

class CreateMicrobes:
    """
    CreateMicrobes Class.

    This class is used to create a list of Microbe objects from provided data.

    Attributes
    ----------
    parent : pandas.DataFrame
        The parent data.
    microbes : list
        The list of Microbe objects created.
    """

    def __init__(self, parent):
        self.parent = parent
        self.microbes = []

    def create(self):
        """
        Create Microbe objects from data.

        Creates a Microbe object for each unique taxon ID in the data.

        Returns
        -------
        list
            A list of Microbe objects.
        """
        unique_taxon_ids = self.parent['Taxon ID'].unique()
        for taxon_id in tqdm(unique_taxon_ids, desc='Creating microbes', unit='microbe'):
            pathways = self.parent[self.parent['Taxon ID'] == taxon_id]['Pathway'].tolist()
            microbe_obj = Microbe(taxon_id, pathways)
            self.microbes.append(microbe_obj)
        return self.microbes

class Pathways:
    """
    Pathways Class.
    
    This class represents the collection of unique metabolic pathways found in the data.

    Attributes
    ----------
    parent : pandas.DataFrame
        The parent data.
    pathways : dict
        A dictionary where keys are pathway names and values are lists of taxon IDs associated with the pathway.
    """

    def __init__(self, parent):
        self.parent = parent
        self.pathways = {}

    def create(self):
        """
        Create pathways dictionary from data.

        Creates a dictionary where each unique pathway in the data is a key and the associated values are the taxon IDs.

        Returns
        -------
        dict
            A dictionary of pathways and their associated taxon IDs.
        """
        unique_pathways = self.parent['Pathway'].unique()
        for pathway in tqdm(unique_pathways, desc="Creating pathways"):
            taxon_ids = self.parent[self.parent['Pathway'] == pathway]['Taxon ID'].tolist()
            self.pathways[pathway] = taxon_ids
        return self.pathways


class ReadDataFiles:
    """
    A class used to read and preprocess different data files required for the project.

    ...

    Attributes
    ----------
    all_sample_data_path : str
        Path to the All Sample Data Excel file.
    taxon_dict_path : str
        Path to the Taxon Dictionary Excel file.
    function_dict_path : str
        Path to the Function Dictionary Excel file.
    parent_path : str
        Path to the Parent CSV file.

    Methods
    -------
    read_excel_file(file_path, usecols=None, skiprows=None, column_names=None):
        Reads an Excel file with specified columns, skipped rows, and column names.
    read_all_sample_data():
        Reads and preprocesses the Sample Data file.
    read_taxon_dict():
        Reads the Taxon Dictionary file.
    read_function_dict():
        Reads the Function Dictionary file.
    read_parent():
        Reads the Parent file.
    """

    def __init__(self, all_sample_data_path, taxon_dict_path, function_dict_path, parent_path):
        """Initializes the ReadDataFiles with specified paths to the data files."""
        self.all_sample_data_path = all_sample_data_path
        self.taxon_dict_path = taxon_dict_path
        self.function_dict_path = function_dict_path
        self.parent_path = parent_path

    def read_excel_file(self, file_path, usecols=None, skiprows=None, column_names=None):
        """
        Reads an Excel file with specified columns, skipped rows, and column names.

        Parameters:
        file_path (str): Path to the Excel file.
        usecols (list, optional): List of column indices to read. Default is None.
        skiprows (int, optional): Number of rows to skip at the start. Default is None.
        column_names (list, optional): List of column names. Default is None.

        Returns:
        df (DataFrame): Pandas DataFrame containing the data read from the Excel file.
        """
        df = pd.read_excel(file_path, usecols=usecols, skiprows=skiprows)
        if column_names:
            df.columns = column_names
        return df

    def read_all_sample_data(self, taxon_level=None):
        """
        Reads and preprocesses the Sample Data file.

        Returns:
        all_sample_data (DataFrame): Pandas DataFrame containing the preprocessed Sample Data.
        """
        # Read the file, skipping the first row
        all_sample_data = self.read_excel_file(self.all_sample_data_path, skiprows=1)

        # Set column names for the first six columns
        all_sample_data.columns.values[:6] = ['Domain', 'Phylum', 'Class', 'Order', 'Family', 'Genus']

        # Delete any columns that are completely empty (have no sample data)
        all_sample_data = all_sample_data.dropna(axis=1, how='all')

        # Combine the first six columns into a single 'Taxon' column,
        # ignore values that are "__", and separate each taxon with "; "
        cols_to_drop = ['Domain', 'Phylum', 'Class', 'Order', 'Family', 'Genus']
        all_sample_data['Taxon'] = all_sample_data[cols_to_drop].apply(
            lambda row: '; '.join(filter(lambda x: x != "__", row)), axis=1)
        all_sample_data = all_sample_data.drop(columns=cols_to_drop)

        # Reorder columns to move 'Taxon' to the first position
        cols = list(all_sample_data.columns)
        cols = [cols[-1]] + cols[:-1]
        all_sample_data = all_sample_data[cols]

        return all_sample_data

    def read_taxon_dict(self):
        """
        Reads the Taxon Dictionary file.

        Returns:
        taxon_dict (DataFrame): Pandas DataFrame containing the Taxon Dictionary data.
        """
        # Read the file, skipping the first two rows, and set column names
        taxon_dict = self.read_excel_file(self.taxon_dict_path, usecols=[0, 1], skiprows=2)
        taxon_dict.columns = ['Taxon ID', 'Taxon']
        return taxon_dict

    def read_function_dict(self):
        """
        Reads the Function Dictionary file.

        Returns:
        function_dict (DataFrame): Pandas DataFrame containing the Function Dictionary data.
        """
        # Read the file, skipping the first row, and set column names
        function_dict = self.read_excel_file(self.function_dict_path, usecols=[0, 1], skiprows=1)
        function_dict.columns = ['Pathway', 'Pathway description']
        return function_dict

    def read_parent(self):
        """
        Reads the Parent file.

        Returns:
        parent (DataFrame): Pandas DataFrame containing the Parent data.
        """
        # Read the file and set column names
        parent = pd.read_csv(self.parent_path, usecols=[1, 2])
        parent.columns = ['Pathway', 'Taxon ID']
        return parent



class HeatmapData:
  """
  This class represents the data structure for a heatmap visualization. It processes
  sample data for the heatmap and provides a custom Aitchison distance function.
  """
  def __init__(self, samples):
    """
    Initialize the HeatmapData class.

    Args:
    samples (list): A list of sample objects.
    """
    self.samples = samples
    self.aitchison = self.get_aitchison_distance_function()

  def process_heatmap_data(self, taxon_level=None):
      """
      Processes the sample data to be used for the heatmap visualization.

      Args:
      taxon_level (str): The taxonomic level to aggregate on. Can be one of 'domain', 'phylum', 'class', 'order', 'family', 'genus'. Default is None, in which case no aggregation is performed.

      Returns:
      heatmap_data (DataFrame): A pandas DataFrame containing taxa and abundance information for each sample.
      """
      heatmap_data = pd.DataFrame(data=[self.samples[0].taxa.Taxon.tolist()] + [sample.abundances for sample in self.samples]).T
      heatmap_data.columns = ['Taxa'] + [sample.sample_name for sample in self.samples]

      if taxon_level is not None:
          taxon_levels = ['domain', 'phylum', 'class', 'order', 'family', 'genus']

          if taxon_level not in taxon_levels:
              raise ValueError('taxon_level must be one of ' + ', '.join(taxon_levels))

          # Split the 'Taxa' column into separate taxonomic levels
          taxa_split = heatmap_data['Taxa'].str.split("; ", expand=True)

          taxa_split.columns = taxon_levels

          # Aggregate by the specified taxon_level
          heatmap_data = heatmap_data.drop('Taxa', axis=1)
          heatmap_data = pd.concat([heatmap_data, taxa_split[taxon_level]], axis=1)

          # Group by the taxon_level and sum the abundances
          heatmap_data = heatmap_data.groupby(taxon_level).sum().reset_index().rename(columns={taxon_level: 'Taxa'})
      return heatmap_data


  # Define a custom aitchison distance for distance metric https://www.frontiersin.org/articles/10.3389/fmicb.2017.02224/full
  @staticmethod
  def get_aitchison_distance_function():
    """
    Defines a custom Aitchison distance function. Aitchison distance is a measure 
    often used in compositional data analysis. It is computed by transforming the 
    data with a centered log-ratio transformation and then computing the Euclidean 
    distance. In this function, zero percentages are set to very small finite 
    numbers because the Aitchison calculation has a logarithm operation.

    Returns:
    aitchison (function): A function that calculates the Aitchison distance between two vectors.
    """
    def aitchison(u, v):
      u[u == 0] = 0.000000001  # Replace 0s with small finite numbers
      v[v == 0] = 0.000000001
      dist =  euclidean(clr(u), clr(v))
      return dist

    return aitchison


class HeatmapPlot:
    """
    This class is used for creating a heatmap plot from the processed data.
    It provides methods to search for pathways, check user-specified pathways, and create the heatmap plot.
    """

    def __init__(self, heatmap_data_object, all_pathways, function_dict, taxon_level=None):
        """
        Initialize the HeatmapPlot class.

        Args:
        heatmap_data_object (HeatmapData object): An object of the HeatmapData class.
        all_pathways (dict): A dictionary of all pathways.
        function_dict (DataFrame): A pandas DataFrame containing the function dictionary.
        """
        self.heatmap_data_object = heatmap_data_object
        self.heatmap_data = self.heatmap_data_object.process_heatmap_data(taxon_level)
        self.aitchison = self.heatmap_data_object.aitchison
        self.all_pathways = all_pathways
        self.function_dict = function_dict
        self.taxon_level = taxon_level

    def search_pathways(self, search_string):
        """
        Search for pathways in the function dictionary that contain the search string.

        Args:
        search_string (str): The string to search for in the pathway descriptions.

        Returns:
        (list): A list of pathways that match the search string.
        """
        matching_pathways = self.function_dict[self.function_dict['Pathway description'].str.contains(search_string, case=False)]
        return matching_pathways['Pathway'].tolist()

    def check_user_pathways(self, user_pathways):
        """
        Checks if the user-specified pathways are a list, string, or None and processes them accordingly.

        Args:
        user_pathways (str/list/None): The user-specified pathways.

        Returns:
        (list): A list of user-specified pathways or None.

        Raises:
        TypeError: If user_pathways is not a string, list or None.
        """
        if isinstance(user_pathways, list):
            return user_pathways
        elif isinstance(user_pathways, str):
            return self.search_pathways(user_pathways)
        elif user_pathways is None:
          return None
        else:
            raise TypeError('user_pathways must be either a string or a list (or None)')

    def heatmap_plot(self, user_pathways, threshold, taxon_dict):
        """
        Creates a heatmap plot using seaborn, with user-specified pathways and a given threshold.

        Args:
        user_pathways (str/list/None): The user-specified pathways.
        threshold (float): The threshold for filtering data.
        taxon_dict (DataFrame): A pandas DataFrame containing the taxon dictionary.

        Raises:
        Exception: If there's an issue during the plotting process.
        """
        user_pathways = self.check_user_pathways(user_pathways)
        # Filter data by threshold and fill NaNs
        filtered_data = self.heatmap_data[(self.heatmap_data.drop('Taxa', axis=1) > threshold / 100).any(axis=1)].fillna(0)

        # Identify microbes that are associated with the user-specified pathways
        user_pathways_taxa = []
        if user_pathways is not None and self.taxon_level is None:
          for pathway in user_pathways:
              if pathway in self.all_pathways:
                  taxa_ids = self.all_pathways[pathway]
                  taxa_names = taxon_dict[taxon_dict['Taxon ID'].isin(taxa_ids)]['Taxon'].tolist()
                  user_pathways_taxa.append(taxa_names)

          # Define colors for each pathway
          colors = sns.color_palette("pastel", len(user_pathways))  # change palette if needed

          # Create a DataFrame for row_colors
          row_colors = pd.DataFrame(index=filtered_data['Taxa'])
          filtered_data.set_index('Taxa', inplace=True)

          # Map colors to taxa for each pathway
          for pathway, taxa, color in zip(user_pathways, user_pathways_taxa, colors):
              row_colors[pathway] = row_colors.index.to_series().map(dict([(taxon, color) for taxon in taxa]))
        else:
          row_colors = None
          filtered_data.set_index('Taxa', inplace=True)


        # Drop 'Taxa' column for heatmap
        # plot_data = filtered_data.drop('Taxa', axis=1)
        plot_data = filtered_data

        # For yticklabels, split each string in 'Taxa' on "; " and take the rightmost substring
        yticklabels = self.heatmap_data[(self.heatmap_data.drop('Taxa', axis=1) > threshold / 100).any(axis=1)].fillna(0).Taxa.str.split("; ").str[-1]

        # Create clustermap
        g = sns.clustermap(data=plot_data, cmap="Blues", metric=self.aitchison, method="complete",
                          row_cluster=False, cbar_kws={'orientation': 'horizontal'},
                          yticklabels=yticklabels, row_colors=row_colors)

        # Set colorbar position and title
        g.ax_cbar.set_position([g.ax_heatmap.get_position().x0 + 0.25 * g.ax_heatmap.get_position().width,
                                g.ax_heatmap.get_position().y0 - 0.09, g.ax_heatmap.get_position().width * 0.5, 0.02])
        g.ax_cbar.set_title('Percent abundance')

        # Display the plot
        plt.show()


class LatexTable:
    """
    This class is used to create a LaTeX formatted table from the function dictionary.
    """

    def __init__(self, function_dict, user_pathways, heatmap_plot_instance):
        """
        Initialize the LatexTable class.

        Args:
        function_dict (DataFrame): A pandas DataFrame containing the function dictionary.
        user_pathways (str/list): A list of user-specified pathways or a string to search.
        heatmap_plot_instance (HeatmapPlot): An instance of the HeatmapPlot class for searching pathways by string.
        """
        self.function_dict = function_dict
        self.heatmap_plot_instance = heatmap_plot_instance
        self.user_pathways = self.heatmap_plot_instance.check_user_pathways(user_pathways)

    def create_table(self):
        """
        Generate a LaTeX table with the pathways specified by the user.
        
        The table includes all rows from the function dictionary that match the user-specified pathways.
        The table is returned as a string in LaTeX table format.

        Returns:
        (str): A string representing the LaTeX table.
        """
        if self.user_pathways is not None:
          # Filter the function_dict to only include the user-specified pathways
          function_dict_filtered = self.function_dict[self.function_dict['Pathway'].isin(self.user_pathways)]

          # Generate the LaTeX table and return it
          latex_table = function_dict_filtered.to_latex(index=False)
          return latex_table




def get_data(all_sample_data, taxon_dict, function_dict, parent):
    """
    Function to read in all data files required for processing.

    Args:
    all_sample_data (str): File path for all sample data.
    taxon_dict (str): File path for the taxon dictionary.
    function_dict (str): File path for the function dictionary.
    parent (str): File path for the parent file.

    Returns:
    tuple: A tuple containing the loaded all sample data, taxon dictionary, function dictionary, and parent data.
    """
    data = ReadDataFiles(all_sample_data, taxon_dict, function_dict, parent)
    all_sample_data = data.read_all_sample_data()
    taxon_dict = data.read_taxon_dict()
    parent = data.read_parent()
    function_dict = data.read_function_dict()
    return all_sample_data, taxon_dict, function_dict, parent

def create_samples_and_pathways(all_sample_data, taxon_dict, parent, sample_list):
    """
    Function to create samples and pathways.

    Args:
    all_sample_data (DataFrame): DataFrame containing all sample data.
    taxon_dict (DataFrame): DataFrame containing the taxon dictionary.
    parent (DataFrame): DataFrame containing the parent data.
    sample_list (list): A list of sample names to include.

    Returns:
    tuple: A tuple containing a list of created Sample objects and a dictionary of all pathways.
    """
    samples = CreateSamples(all_sample_data, taxon_dict, parent).create(sample_list)
    all_pathways = Pathways(parent).create()
    return samples, all_pathways

def plot_heatmap(samples, all_pathways, function_dict, taxon_dict, user_pathways, print_table, threshold, taxon_level=None):
    """
    Function to create and plot a heatmap, and optionally print a LaTeX table of the pathways.

    Args:
    samples (list): A list of Sample objects.
    all_pathways (dict): A dictionary of all pathways.
    function_dict (DataFrame): DataFrame containing the function dictionary.
    taxon_dict (DataFrame): DataFrame containing the taxon dictionary.
    user_pathways (str or list or None): Either a string containing a search term, a list of specific pathways, or None.
    print_table (bool): Whether to print a LaTeX table of the pathways.
    threshold (int): The threshold value for percent abundance.
    taxon_level (str or None): The level at which to group taxa. If None, no grouping is done. 
                               Can be 'domain', 'phylum', 'class', 'order', 'family', or 'genus'.

    Returns:
    None
    """
    heatmap_data_object = HeatmapData(samples)
    heatmap_plot = HeatmapPlot(heatmap_data_object, all_pathways, function_dict, taxon_level)
    heatmap_plot.heatmap_plot(user_pathways, threshold, taxon_dict)
    if print_table:
        print(LatexTable(function_dict, user_pathways, heatmap_plot).create_table())

def main():
    """
    The main function of the script which runs the entire data processing, plotting, and printing process.

    Args:
    None

    Returns:
    None
    """
    # Define the file paths for the data sources
    all_sample_data = '/content/drive/MyDrive/Pylomap/pylomap/F data.xlsx'
    taxon_dict = '/content/drive/MyDrive/Pylomap/pylomap/Taxon Dictionary.xlsx'
    function_dict = '/content/drive/MyDrive/Pylomap/pylomap/Function Dictionary.xlsx'
    parent = '/content/drive/MyDrive/Pylomap/pylomap/FL Parent.csv'

    # Specify which samples should be plotted. If None, all samples are plotted
    sample_list = None      

    # Specify pathways to plot as a list OR a string to search OR None
    user_pathways = ['1CMET2-PWY', 'PWY-5430', 'PWY-5431']      

    # Percentage above which is displayed on the clustermap
    threshold = 3     

    # Specify whether a LaTeX table of the pathways should be printed
    print_latex_table = False

    # Specify the taxon level for grouping. If None, no grouping is done. Can be 'domain', 'phylum', 'class', 'order', 'family', or 'genus'
    taxon_level = None

    # Get data from all required files
    all_sample_data, taxon_dict, function_dict, parent = get_data(all_sample_data, taxon_dict, function_dict, parent)

    # Create samples and pathways
    samples, all_pathways = create_samples_and_pathways(all_sample_data, taxon_dict, parent, sample_list)

    # Plot the heatmap and optionally print the LaTeX table
    plot_heatmap(samples, all_pathways, function_dict, taxon_dict, user_pathways, print_latex_table, threshold, taxon_level)


if __name__ == "__main__":
    main()
