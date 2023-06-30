<div aria-autocomplete="none" class="editor-input" contenteditable="false" spellcheck="true" data-lexical-editor="true" style="user-select: text; white-space: pre-wrap; word-break: break-word;">
	<h1 class="editor-heading-h1 ltr" dir="ltr">
		<span data-lexical-text="true">Sample Class</span>
	</h1>
	<p class="editor-paragraph ltr" dir="ltr">
		<span data-lexical-text="true">This class represents a biological sample, characterised by its name, taxa, abundances, and pathways.</span>
	</p>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Attributes</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">sample_name (str): The name of the sample.</span>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">taxa (pandas.DataFrame): The taxa present in the sample.</span>
		</li>
		<li value="3" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">abundances (list): The abundances of each taxon in the sample.</span>
		</li>
		<li value="4" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">pathways (dict): The metabolic pathways present in the sample.</span>
		</li>
	</ul>
	<h1 class="editor-heading-h1 ltr" dir="ltr">
		<span data-lexical-text="true">CreateSamples Class</span>
	</h1>
	<p class="editor-paragraph ltr" dir="ltr">
		<span data-lexical-text="true">This class is used to create a list of Sample objects from provided data.</span>
	</p>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Attributes</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">all_sample_data (pandas.DataFrame): The data containing all sample information.</span>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">taxon_dict (pandas.DataFrame): The dictionary mapping taxa to their IDs.</span>
		</li>
		<li value="3" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">parent (pandas.DataFrame): The parent data.</span>
		</li>
		<li value="4" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">samples (list): The list of Sample objects created.</span>
		</li>
	</ul>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Methods</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">create(sample_names=None)</span>
		</li>
		<li value="2" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Create Sample objects from data.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Parameters:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">sample_names (list, optional): The names of the samples to create objects for.</span>
						</li>
					</ul>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="4" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">list: A list of Sample objects.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
	<h1 class="editor-heading-h1 ltr" dir="ltr">
		<span data-lexical-text="true">Microbe Class</span>
	</h1>
	<p class="editor-paragraph ltr" dir="ltr">
		<span data-lexical-text="true">This class represents a microbial taxon, characterised by its taxon_id and associated pathways.</span>
	</p>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Attributes</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">taxon_id (str): The unique identifier for the microbe.</span>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">pathways (list): The metabolic pathways associated with the microbe.</span>
		</li>
	</ul>
	<h1 class="editor-heading-h1 ltr" dir="ltr">
		<span data-lexical-text="true">CreateMicrobes Class</span>
	</h1>
	<p class="editor-paragraph ltr" dir="ltr">
		<span data-lexical-text="true">This class is used to create a list of Microbe objects from provided data.</span>
	</p>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Attributes</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">parent (pandas.DataFrame): The parent data.</span>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">microbes (list): The list of Microbe objects created.</span>
		</li>
	</ul>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Methods</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">create()</span>
		</li>
		<li value="2" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Create Microbe objects from data.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">list: A list of Microbe objects.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
	<h1 class="editor-heading-h1 ltr" dir="ltr">
		<span data-lexical-text="true">Pathways Class</span>
	</h1>
	<p class="editor-paragraph ltr" dir="ltr">
		<span data-lexical-text="true">This class represents the collection of unique metabolic pathways found in the data.</span>
	</p>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Attributes</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">parent (pandas.DataFrame): The parent data.</span>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">pathways (dict): A dictionary where keys are pathway names and values are lists of taxon IDs associated with the pathway.</span>
		</li>
	</ul>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Methods</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">create()</span>
		</li>
		<li value="2" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Create pathways dictionary from data.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">dict: A dictionary of pathways and their associated taxon IDs.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
	<h1 class="editor-heading-h1 ltr" dir="ltr">
		<span data-lexical-text="true">ReadDataFiles Class</span>
	</h1>
	<p class="editor-paragraph ltr" dir="ltr">
		<span data-lexical-text="true">A class used to read and preprocess different data files required for the project.</span>
	</p>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Attributes</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">all_sample_data_path (str): Path to the All Sample Data Excel file.</span>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">taxon_dict_path (str): Path to the Taxon Dictionary Excel file.</span>
		</li>
		<li value="3" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">function_dict_path (str): Path to the Function Dictionary Excel file.</span>
		</li>
		<li value="4" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">parent_path (str): Path to the Parent CSV file.</span>
		</li>
	</ul>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Methods</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">read_excel_file(file_path, usecols=None, skiprows=None, column_names=None)</span>
		</li>
		<li value="2" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Reads an Excel file with specified columns, skipped rows, and column names.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Parameters:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">file_path (str): Path to the Excel file.</span>
						</li>
						<li value="2" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">usecols (list, optional): List of column indices to read. Default is None.</span>
						</li>
						<li value="3" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">skiprows (int, optional): Number of rows to skip at the start. Default is None.</span>
						</li>
						<li value="4" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">column_names (list, optional): List of column names. Default is None.</span>
						</li>
					</ul>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="4" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">df (DataFrame): Pandas DataFrame containing the data read from the Excel file.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">read_all_sample_data()</span>
		</li>
		<li value="3" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Reads and preprocesses the Sample Data file.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">all_sample_data (DataFrame): Pandas DataFrame containing the preprocessed Sample Data.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
		<li value="3" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">read_taxon_dict()</span>
		</li>
		<li value="4" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Reads the Taxon Dictionary file.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">taxon_dict (DataFrame): Pandas DataFrame containing the Taxon Dictionary data.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
		<li value="4" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">read_function_dict()</span>
		</li>
		<li value="5" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Reads the Function Dictionary file.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">function_dict (DataFrame): Pandas DataFrame containing the Function Dictionary data.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
		<li value="5" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">read_parent()</span>
		</li>
		<li value="6" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Reads the Parent file.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">parent (DataFrame): Pandas DataFrame containing the Parent data.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
	<h1 class="editor-heading-h1 ltr" dir="ltr">
		<span data-lexical-text="true">HeatmapData Class</span>
	</h1>
	<p class="editor-paragraph ltr" dir="ltr">
		<span data-lexical-text="true">This class represents the data structure for a heatmap visualisation. It processes sample data for the heatmap and provides a custom Aitchison distance function.</span>
	</p>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Attributes</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">samples (list): A list of sample objects.</span>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">aitchison (function): A function that calculates the Aitchison distance between two vectors.</span>
		</li>
	</ul>
	<h3 class="editor-heading-h3 ltr" dir="ltr">
		<span data-lexical-text="true">Methods</span>
	</h3>
	<ul class="editor-list-ul">
		<li value="1" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">process_heatmap_data(taxon_level=None)</span>
		</li>
		<li value="2" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Processes the sample data to be used for the heatmap visualisation.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Parameters:</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">taxon_level (str): The taxonomic level to aggregate on. Can be one of 'domain', 'phylum', 'class', 'order', 'family', 'genus'. Default is None, in which case no aggregation is performed.</span>
						</li>
					</ul>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Returns:</span>
				</li>
				<li value="4" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">heatmap_data (DataFrame): A pandas DataFrame containing taxa and abundance information for each sample.</span>
						</li>
					</ul>
				</li>
			</ul>
		</li>
		<li value="2" class="editor-listitem ltr" dir="ltr">
			<span data-lexical-text="true">get_aitchison_distance_function()</span>
		</li>
		<li value="3" class="editor-listitem editor-nested-listitem">
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">Defines a custom Aitchison distance function. Aitchison distance is a measure often used in compositional data analysis. </span>
					<br>
						<span data-lexical-text="true">It is computed by transforming the data with a centered log-ratio transformation and then computing the Euclidean distance.</span>
						<br>
							<span data-lexical-text="true">In this function, zero percentages are set to very small finite numbers because the Aitchison calculation has a logarithm operation.</span>
						</li>
					</ul>
				</li>
			</ul>
			<h1 class="editor-heading-h1 ltr" dir="ltr">
				<span data-lexical-text="true">HeatmapPlot Class</span>
			</h1>
			<p class="editor-paragraph ltr" dir="ltr">
				<span data-lexical-text="true">This class is used for creating a heatmap plot from the processed data. It provides methods to search for pathways, check user-specified pathways, and create the heatmap plot.</span>
			</p>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Attributes</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">heatmap_data_object (HeatmapData object): An object of the HeatmapData class.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">heatmap_data (DataFrame): DataFrame containing the preprocessed heatmap data.</span>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">aitchison (function): A function that calculates the Aitchison distance between two vectors.</span>
				</li>
				<li value="4" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">all_pathways (dict): A dictionary of all pathways.</span>
				</li>
				<li value="5" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">function_dict (DataFrame): DataFrame containing the function dictionary.</span>
				</li>
				<li value="6" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">taxon_level (str): The level at which to group taxa.</span>
				</li>
			</ul>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Methods</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">search_pathways(search_string)</span>
				</li>
				<li value="2" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Search for pathways in the function dictionary that contain the search string.</span>
						</li>
						<li value="2" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Parameters:</span>
						</li>
						<li value="3" class="editor-listitem editor-nested-listitem">
							<ul class="editor-list-ul">
								<li value="1" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">search_string (str): The string to search for in the pathway descriptions.</span>
								</li>
							</ul>
						</li>
						<li value="3" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Returns:</span>
						</li>
						<li value="4" class="editor-listitem editor-nested-listitem">
							<ul class="editor-list-ul">
								<li value="1" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">list: A list of pathways that match the search string.</span>
								</li>
							</ul>
						</li>
					</ul>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">check_user_pathways(user_pathways)</span>
				</li>
				<li value="3" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Checks if the user-specified pathways are a list, string, or None and processes them accordingly.</span>
						</li>
						<li value="2" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Parameters:</span>
						</li>
						<li value="3" class="editor-listitem editor-nested-listitem">
							<ul class="editor-list-ul">
								<li value="1" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">user_pathways (str/list/None): The user-specified pathways.</span>
								</li>
							</ul>
						</li>
						<li value="3" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Returns:</span>
						</li>
						<li value="4" class="editor-listitem editor-nested-listitem">
							<ul class="editor-list-ul">
								<li value="1" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">list: A list of user-specified pathways or None.</span>
								</li>
							</ul>
						</li>
						<li value="4" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Raises:</span>
						</li>
						<li value="5" class="editor-listitem editor-nested-listitem">
							<ul class="editor-list-ul">
								<li value="1" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">TypeError: If user_pathways is not a string, list or None.</span>
								</li>
							</ul>
						</li>
					</ul>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">heatmap_plot(user_pathways, threshold, taxon_dict)</span>
				</li>
				<li value="4" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Creates a heatmap plot using seaborn, with user-specified pathways and a given threshold.</span>
						</li>
						<li value="2" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Parameters:</span>
						</li>
						<li value="3" class="editor-listitem editor-nested-listitem">
							<ul class="editor-list-ul">
								<li value="1" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">user_pathways (str/list/None): The user-specified pathways.</span>
								</li>
								<li value="2" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">threshold (float): The threshold for filtering data.</span>
								</li>
								<li value="3" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">taxon_dict (DataFrame): A pandas DataFrame containing the taxon dictionary.</span>
								</li>
							</ul>
						</li>
						<li value="3" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Raises:</span>
						</li>
						<li value="4" class="editor-listitem editor-nested-listitem">
							<ul class="editor-list-ul">
								<li value="1" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">Exception: If there's an issue during the plotting process.</span>
								</li>
							</ul>
						</li>
					</ul>
				</li>
			</ul>
			<h1 class="editor-heading-h1 ltr" dir="ltr">
				<span data-lexical-text="true">LatexTable Class</span>
			</h1>
			<p class="editor-paragraph ltr" dir="ltr">
				<span data-lexical-text="true">This class is used to create a LaTeX formatted table from the function dictionary.</span>
			</p>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Attributes</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">function_dict (DataFrame): DataFrame containing the function dictionary.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">heatmap_plot_instance (HeatmapPlot): An instance of the HeatmapPlot class for searching pathways by string.</span>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">user_pathways (str or list or None): Either a string containing a search term, a list of specific pathways, or None.</span>
				</li>
			</ul>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Methods</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">create_table()</span>
				</li>
				<li value="2" class="editor-listitem editor-nested-listitem">
					<ul class="editor-list-ul">
						<li value="1" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Generate a LaTeX table with the pathways specified by the user.</span>
						</li>
						<li value="2" class="editor-listitem ltr" dir="ltr">
							<span data-lexical-text="true">Returns:</span>
						</li>
						<li value="3" class="editor-listitem editor-nested-listitem">
							<ul class="editor-list-ul">
								<li value="1" class="editor-listitem ltr" dir="ltr">
									<span data-lexical-text="true">str: A string representing the LaTeX table.</span>
								</li>
							</ul>
						</li>
					</ul>
				</li>
			</ul>
			<h1 class="editor-heading-h1 ltr" dir="ltr">
				<span data-lexical-text="true">get_data Function</span>
			</h1>
			<p class="editor-paragraph ltr" dir="ltr">
				<span data-lexical-text="true">Function to read in all data files required for processing.</span>
			</p>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Parameters</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">all_sample_data (str): File path for all sample data.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">taxon_dict (str): File path for the taxon dictionary.</span>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">function_dict (str): File path for the function dictionary.</span>
				</li>
				<li value="4" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">parent (str): File path for the parent file.</span>
				</li>
			</ul>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Returns</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">tuple: A tuple containing the loaded all sample data, taxon dictionary, function dictionary, and parent data.</span>
				</li>
			</ul>
			<h1 class="editor-heading-h1 ltr" dir="ltr">
				<span data-lexical-text="true">create_samples_and_pathways Function</span>
			</h1>
			<p class="editor-paragraph ltr" dir="ltr">
				<span data-lexical-text="true">Function to create samples and pathways.</span>
			</p>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Parameters</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">all_sample_data (DataFrame): DataFrame containing all sample data.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">taxon_dict (DataFrame): DataFrame containing the taxon dictionary.</span>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">parent (DataFrame): DataFrame containing the parent data.</span>
				</li>
				<li value="4" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">sample_list (list): A list of sample names to include.</span>
				</li>
			</ul>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Returns</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">tuple: A tuple containing a list of created Sample objects and a dictionary of all pathways.</span>
				</li>
			</ul>
			<h1 class="editor-heading-h1 ltr" dir="ltr">
				<span data-lexical-text="true">plot_heatmap Function</span>
			</h1>
			<p class="editor-paragraph ltr" dir="ltr">
				<span data-lexical-text="true">Function to create and plot a heatmap, and optionally print a LaTeX table of the pathways.</span>
			</p>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Parameters</span>
			</h3>
			<ul class="editor-list-ul">
				<li value="1" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">samples (list): A list of Sample objects.</span>
				</li>
				<li value="2" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">all_pathways (dict): A dictionary of all pathways.</span>
				</li>
				<li value="3" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">function_dict (DataFrame): DataFrame containing the function dictionary.</span>
				</li>
				<li value="4" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">taxon_dict (DataFrame): DataFrame containing the taxon dictionary.</span>
				</li>
				<li value="5" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">user_pathways (str or list or None): Either a string containing a search term, a list of specific pathways, or None.</span>
				</li>
				<li value="6" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">print_table (bool): Whether to print a LaTeX table of the pathways.</span>
				</li>
				<li value="7" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">threshold (int): The threshold value for percent abundance.</span>
				</li>
				<li value="8" class="editor-listitem ltr" dir="ltr">
					<span data-lexical-text="true">taxon_level (str or None): The level at which to group taxa. If None, no grouping is done. Can be 'domain', 'phylum', 'class', 'order', 'family', or 'genus'.</span>
				</li>
			</ul>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Returns</span>
			</h3>
			<p class="editor-paragraph ltr" dir="ltr">
				<span data-lexical-text="true">None</span>
			</p>
			<h1 class="editor-heading-h1 ltr" dir="ltr">
				<span data-lexical-text="true">main Function</span>
			</h1>
			<p class="editor-paragraph ltr" dir="ltr">
				<span data-lexical-text="true">The main function of the script which runs the entire data processing, plotting, and printing process.</span>
			</p>
			<h3 class="editor-heading-h3 ltr" dir="ltr">
				<span data-lexical-text="true">Parameters</span>
			</h3>
			<p class="editor-paragraph ltr" dir="ltr">
				<span data-lexical-text="true">None</span>
			</p>
		</div>
