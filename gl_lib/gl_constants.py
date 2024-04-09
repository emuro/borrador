# python3
# ################################################################## #
# constants.py (C) 2023 Mainz.
# Author: Enrique M. Muro
# ################################################################## #
#
# ------------------------------------------------------------------------
# Project: gene_length
#
# Purpose: constants used in the project
# ################################################################## #

import os
import matplotlib
import numpy as np
import sys

# external USB disk
###################
USB_DISK_NAME = "Nubya" # or Wes
system = list(os.uname())[0]
if system == 'Linux':
    base_path_in = "/media/emuro/" + USB_DISK_NAME + "/"
elif system == 'Darwin':
    base_path_in = "/Volumes/" + USB_DISK_NAME + "/" 

# Paths
#######
GIT_PROJECT_PATH        = os.path.dirname(__file__) + "/../" 
MAIN_TABLES_PATH        = GIT_PROJECT_PATH + "main_tables/"
SUPPL_TABLES_PATH       = MAIN_TABLES_PATH + "suppl_tables/"
#
EXTRA_TABLES_PATH       = MAIN_TABLES_PATH + "more_tables/" 
#
WORKING_ON_TABLES_PATH  = GIT_PROJECT_PATH + "working_on_tables/"
#
GENES_PROTS_LENGTH_PATH =  base_path_in + "results/geneLength/"

# File names
############
STAT_G_FILE        = MAIN_TABLES_PATH + "stat_protCodGenes.tsv" 
STAT_P_FILE        = MAIN_TABLES_PATH + "stat_proteins.tsv"
STAT_MERGED_FILE   = MAIN_TABLES_PATH + "stat_merged.tsv"
#
STAT_MERGED_MEDIAN_MODE_FILE = WORKING_ON_TABLES_PATH + "stat_merged_protCodGenes_median_mode.tsv"
GROUP_VERT = WORKING_ON_TABLES_PATH +  "stat_protCodGenes_with_ncbiGenomeData_FerGroup.tsv"
#
G_NCBI_GENOME_DATA_FILE       = SUPPL_TABLES_PATH + "stat_protCodGenes_ncbiGenomeAssemblyStatus.tsv"
WRONG_ANNOTATIONS_MERGED_FILE = EXTRA_TABLES_PATH + "noisy_stat_merged.tsv"


# colors for plots
################## colors start
COLOR_FOR_DIST = {
    "genes":    matplotlib.colors.to_hex("#76bdfb", keep_alpha=False),
    "proteins": matplotlib.colors.to_hex("#ffab98", keep_alpha=False)
}
#
ORG_KINGDOMS            = ['archaea',  'bacteria', 'eukaryota']
COLOR_KINGDOMS          = ['#D83B01',  '#002050',   '#0078D7']
#
ORG_GROUPS                = ["bacteria", "archaea", "protists", "fungi", "plants",
                             "invertebrates", "vertebrates"]
PyNB_COLOR_ORG_GROUPS     = ['#D83B01',  '#002050', '#FFA500', '#A80000', '#107C10',
                             '#EF008C', '#0078D7']
COLOR_OF = dict([(key, val) for i, (key, val) in enumerate(zip(ORG_GROUPS, PyNB_COLOR_ORG_GROUPS))])
#
ORG_TIME_GROUPS           = ['Archaea', 'Bacteria', 'protists', 'Fungi', 'Viridiplantae', \
        'Arthropoda', 'Actinopterygii', 'Aves', 'Mammalia', 'Primates']
COLOR_ORG_TIME_GROUPS     = [ '#002050', '#D83B01', '#FFA500', '#A80000', '#107C10', '#EF008C', 'powderblue', 'lightskyblue', 'deepskyblue', 'blue']
# 
ORG_MEAN_GROUPS           = ['Archaea', 'Bacteria', 'Microsporidia', 'Mucuromycota', 'Ascomycota', 'Basidiomycota', 'protists', \
    'Viridiplantae', 'Arthropoda', 'Actinopterygii', 'Aves', 'Mammalia', 'Primates']
#COLOR_ORG_MEAN_GROUPS     = ['#002050', '#D83B01', '#A80000', '#A80000', '#A80000', '#A80000', '#FFA500', \
COLOR_ORG_MEAN_GROUPS     = ['#002050', 'slategray', 'mistyrose', 'darksalmon', 'coral', 'red', '#FFA500', \
'#107C10', '#EF008C', 'powderblue', 'lightskyblue', 'deepskyblue', 'blue']
#'#107C10', '#EF008C', '#0078D7', '#0078D7', '#0078D7', '#0078D7']
#COLOR_ORG_TIME_GROUPS     = [ '#002050', '#D83B01', '#FFA500', '#A80000', '#107C10', '#EF008C', 'powderblue', 'lightskyblue', 'deepskyblue', 'blue']

# Article colors
################
BOOL_USE_ARTICLE_COLORS = 0
if BOOL_USE_ARTICLE_COLORS:
    ARTICLE_COLOR_ORG_GROUPS        = ['#FFFFFF', '#F4B183', '#FFF2CC', '#9DC3E6', '#385723', \
                                       '#D0A8CD', '#F997CE']
    # ARTICLE_COLOR_BORDER_ORG_GROUPS !!! Needs to reorder or eliminate the borders
    ARTICLE_COLOR_BORDER_ORG_GROUPS = ['#D26E2A', '#000000', '#BF9000', '#A9D18E', '#3B64AD',
                                        '#9664A0', '#C00000']  # Apply borders for better results
    COLOR_OF = dict([(key, val) for i, (key, val) in enumerate(zip(ORG_GROUPS, ARTICLE_COLOR_ORG_GROUPS))])
COLOR_ORG_GROUPS = []
for g in ORG_GROUPS: #COLOR_OF:
    COLOR_ORG_GROUPS.append(COLOR_OF[g])
################################# colors end

    
# alpha parameter for plots 
# not in use at the moment
################################# alpha start    
ALPHA_OF ={
    "bacteria": 0.1, "archaea": 1.0,
    "protists": 1.0, "fungi": 0.1,
    "plants": 1.0,
    "invertebrates": 1.0, "vertebrates": 1.0
}
ALPHA_ORG_GROUPS = np.array(
    [ALPHA_OF["bacteria"], ALPHA_OF["archaea"],
     ALPHA_OF["protists"], ALPHA_OF["fungi"],
     ALPHA_OF["plants"],
     ALPHA_OF["invertebrates"], ALPHA_OF["vertebrates"]]
)
################################# alpha end




