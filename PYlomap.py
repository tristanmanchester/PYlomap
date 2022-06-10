# Heatmap Generation from MicroOrganism Data - QUIME 2 AddOn
# By William Pearson and Hannah Eccleston

#Import Packages
from openpyxl import load_workbook
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import hashlib


###Define Class###
class DataSet:
    def __init__(self, workBookName, workSheetName, documentName, iDColumnStart, dataRowStart, iDColumnEnd, dataRowEnd, relativeAbundanceColumn):
        self.workBookName = workBookName
        self.workSheetName = workSheetName
        self.documentName = documentName
        self.iDColumnStart = iDColumnStart
        self.iDColumnEnd = iDColumnEnd
        self.relativeAbundanceColumn = relativeAbundanceColumn
        self.dataRowStart = dataRowStart
        self.dataRowEnd = dataRowEnd
        self.MicroOrganisms = None

    def AddMicroOrganismList(self, microOrganismList):
        self.MicroOrganisms = microOrganismList
        
    def FullDataSetInformation(self):
        return ("Name - " + self.documentName +
                " | " + self.iDColumnStart + self.dataRowStart + ":" + self.iDColumnEnd + self.dataRowEnd +
                " | " + self.relativeAbundanceColumn + self.dataStart +
                ":" + self.relativeAbundanceColumn + self.dataRowEnd)

    def RelativeAbundanceColumnRange(self):
        return (self.relativeAbundanceColumn + self.dataRowStart + ":" + self.relativeAbundanceColumn + self.dataRowEnd)

    def BacteriaNameColumnRange(self):
        return (self.iDColumnStart + self.dataRowStart + ":" + self.iDColumnEnd + self.dataRowEnd)

    def ReturnRelativeAbundanceOfMicroOraganism(self, microOrganismIDToCheck_Hash):
        for microOrganism in self.MicroOrganisms:
            hashIDToCheck = microOrganism.hashID
            if(hashIDToCheck == microOrganismIDToCheck_Hash):
                return microOrganism.relativeAbundance
        #else
        return 0

    def CreateMicroOrganismList(self, BacteriaNameList, RelativeAbundanceList):
        #Takes a 1-Dimensional OpenPyxl List and converts it into a python list
        #Intialise the List that will be filled with python values
        microOrganismList = []

        #For every item in the openpyxl List, grab the value of that item and append it to the Python List
        for i in range(len(RelativeAbundanceList)):
            #Grab the relevant values at every row
            newDomain = BacteriaNameList[i][0].value
            newPhylum = BacteriaNameList[i][1].value
            newClassification = BacteriaNameList[i][2].value
            newOrder = BacteriaNameList[i][3].value
            newFamily = BacteriaNameList[i][4].value
            newGenus =BacteriaNameList[i][5].value
            newRelativeAbundance = RelativeAbundanceList[i][0].value

            #Create a new MicroOrganism object
            newMicroOrganism = MicroOrganism(newDomain,
                                             newPhylum,
                                             newClassification,
                                             newOrder,
                                             newFamily,
                                             newGenus,
                                             newRelativeAbundance)
            #Generate the Hash ID for the Microorganism
            newMicroOrganism.GenerateSelfHashID()

            #Add the new Microogranim to the list of microorganisms
            microOrganismList.append(newMicroOrganism)

        #Return list microOrganism's
        return microOrganismList  

    def PopulateDataSetWithMicroOrganisms(self):
        #Load the Data set's Workbook
        excelWorkBook = load_workbook(filename=self.workBookName, data_only=True)

        #Load the Data set's Sheet
        excelSheet = excelWorkBook[self.workSheetName]

        #Load the Data set's Relative Abundance
        openpyxlList_BacteriaName = excelSheet[self.BacteriaNameColumnRange()]
        openpyxlList_RelativeAbundance = excelSheet[self.RelativeAbundanceColumnRange()]

        #Create a microOrganism List
        microOrganismList = self.CreateMicroOrganismList(openpyxlList_BacteriaName, openpyxlList_RelativeAbundance)
            
        #Add the new Microbe List to the provided DataSet
        self.AddMicroOrganismList(microOrganismList)
        
    
class MicroOrganism:
    def __init__(self, domain, phylum, classification, order, family, genus, relativeAbundance):
        self.domain = domain
        self.phylum = phylum
        self.classification = classification
        self.order = order
        self.family = family
        self.genus = genus
        self.relativeAbundance = relativeAbundance
        self.hashID = None

    def FullBacteriaID(self):
        return (self.domain +";"+
                self.phylum +";"+
                self.classification +";"+
                self.order +";"+
                self.family +";"+
                self.genus)

    def HighestNameStructure(self):
        if(self.genus == "__") or (self.genus == "g__uncultured"):
            if(self.family == "__") or (self.family == "f__uncultured"):
                if(self.order == "__") or (self.order == "o__uncultured"):
                    if(self.classification == "__") or (self.classification == "c__uncultured"):
                        if(self.phylum == "__") or (self.phylum == "p__uncultured"):
                            return self.domain
                        else:
                            return self.phylum
                    else:
                        return self.classification
                else:
                    return self.order
            else:
                return self.family
        else:
            return self.genus
    
    def RelativeAbundance(self):
        return self.relativeAbundance

    def GenerateSelfHashID(self):
        self.hashID = hashlib.md5(self.FullBacteriaID().encode()).hexdigest()


###Define Functions###   
def MakeHeatMap(dataSets, LinewidthOveride = 0, PercentToIgnore = 0):
    #Initialise the parts of the Data Frame, a list of RA for each DataSet,
    #   and a list of names for the data sets.
    RALists = []
    dataSetNameLists = []
    microOrganismNameList = []

    #Initialise cut down lists at the same time to make them the same size
    cutdownRALists = []
    cutdownMicroOrganismNameList = []

    #Populate lists
    for dataSet in dataSets:
        RALists.append([])
        cutdownRALists.append([])
        
        dataSetNameLists.append(dataSet.documentName)

    #Initialise a list of all microbacteria that appear (Note this uses hashTables for optimisation)
    #   Add a hashID to the HashID list to make searching faster, also add the highest order name ID.
    allMicrobacteriaPresent = []

    for dataSet in dataSets:
        for i in range(len(dataSet.MicroOrganisms)):
            hashIDToCheck = dataSet.MicroOrganisms[i].hashID
            if(hashIDToCheck not in allMicrobacteriaPresent):
                microOrganismNameList.append(dataSet.MicroOrganisms[i].HighestNameStructure())
                allMicrobacteriaPresent.append(hashIDToCheck)

    #Now go through the entire mO list and add the relative abundance of that mO of each data set
    #   If there is no entry for that data set then the value returned is 0
    
    for mO in allMicrobacteriaPresent:
        for i in range(len(dataSets)):
            RALists[i].append(dataSets[i].ReturnRelativeAbundanceOfMicroOraganism(mO))
            
    #You now have; a list of relative abundances for each data set (RALists)
    #              a list of microorganism names (microOrganismNameList)
    #              a list of dataSet names (dataSetNameLists)

    #Cut down the list to ignore any values that are below x%
    for i in range(len(microOrganismNameList)):
        includeMicroOrganism = False
        for RAList in RALists:
            if (RAList[i] > (PercentToIgnore/100)):
                includeMicroOrganism = True

        if (includeMicroOrganism):
            cutdownMicroOrganismNameList.append(microOrganismNameList[i])
            for j in range(len(RALists)):
                if(RALists[j][i] > (PercentToIgnore/100)):
                    cutdownRALists[j].append(RALists[j][i] * 100)
                else:
                    cutdownRALists[j].append(0)


    
    #Now Create a pandas frame work to hold all this information
    pandaFrameWork = pd.DataFrame(cutdownRALists, columns=cutdownMicroOrganismNameList, index=dataSetNameLists)
    pandaFrameWork_transpose = pandaFrameWork.transpose()

    #Plot Data
    HeatMapPlot(pandaFrameWork_transpose, LinewidthOveride)

def HeatMapPlot(data, linewidthOveride):
    sns.heatmap(data, annot=True, linewidths=linewidthOveride, cmap="YlGnBu", yticklabels=True)
    plt.tight_layout()
    plt.show()



###INITIALISE DATASETS###
CW1 = DataSet("HannahExcelData.xlsx", "Sheet1", "CW1", "A", "3", "F", "203", "G",)
CW2 = DataSet("HannahExcelData.xlsx", "Sheet1", "CW2", "A", "3", "F", "203", "G",)


###FINALISE DATASETS###
CW1.PopulateDataSetWithMicroOrganisms()
CW2.PopulateDataSetWithMicroOrganisms()

###Plot HeatMap###
MakeHeatMap([CW1, CW2], LinewidthOveride = 0, PercentToIgnore = 1)














