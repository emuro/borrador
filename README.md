# The emergence of eukaryotes as an evolutionary algorithmic phase transition

This repository contains the data and programs needed to reproduce the results reported in our article. Here, it is also described how to obtain the annotations from public repositories.  

**The structure of this repository is the next:**  
 - **README.md** guides you all over this repository.
 - **main_tables** that are needed to reproduce the main figures.  
        - **suppl_tables** for the supplementary material.  
        - **suppl_tables__extra** some extra data that can be helpful (ie. taxonomical ids).  
 - **main_work** contains the programs needed to reproduce the main results.  
        - **suppl_work**, where the programs for the supplementary material are.
        - **suppl_work__extra**, where some extra programs that complement the supplementary material are.

---
### Data: the annotations were downloaded from public repositories

#### Proteins
The [reference proteomes](https://www.uniprot.org/proteomes/?query=*&fil=reference%3Ayes) were downloaded from the Universal Protein Resource ([Uniprot](https://www.uniprot.org/)). Each proteome has a unique Uniprot-identifier (UPID). A [description](https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/README) of the proteomes is also provided. It contains a table with information on every proteome: UPIDs, taxonomy_ids, species names, etc. All the reference proteomes were downloaded from [Uniprot FTP repository](https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/) on 28.5.2021. Note that viruses were not downloaded and that Uniprot is updated regularly, every eight weeks.  

Then, for each species a fasta file containing its reference proteome was downloaded, preserving the directory structure of the repository. For instance, for _Homo sapiens_ (UPID: UP000005640 and taxonomy id:9606): 
```
UP000005640_9606.fasta.gz @
our_mnt_dir + /data/compressed/ + "ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/reference_proteomes/Eukaryota/UP000005640/"
```
our_mnt_dir is the local directory where the data were downloaded.

#### Protein coding genes 
The protein coding gene annotations were obtained from different webservers provided by Ensembl: [prokaryotes (archaea, bacteria)](https://bacteria.ensembl.org), [protists](https://protists.ensembl.org), [plants](https://plants.ensembl.org), [fungi](http://fungi.ensembl.org/), [metazoa (invertebrates)](https://metazoa.ensembl.org), [vertebrates](https://ensembl.org/index.html). Then, any paraphyletic categorization in groups of organisms is already established by Ensembl. 


| Ensembl ftp site by Kingdom/division                                          | Release            |  
| :---------------------------------------------------------------------------  | :----------------- |  
| [prokaryotes: archaea, bacteria](http://ftp.ensemblgenomes.org/pub/bacteria/) | ensemblgenomes 49  |  
| [protists](http://ftp.ensemblgenomes.org/pub/protists/)                       | ensemblgenomes 49  |  
| [plants](http://ftp.ensemblgenomes.org/pub/plants/)                           | ensemblgenomes 49  |  
| [fungi](http://ftp.ensemblgenomes.org/pub/fungi/)                             | ensemblgenomes 49  |  
| [metazoa (invertebrates)](http://ftp.ensemblgenomes.org/pub/metazoa/)                         | ensemblgenomes 49  |  
| [vertebrates](https://ftp.ensembl.org/pub/)                                   | ensembl 98         |  

The gzip compressed *.gtf.gz (General Transfer Format) gene annotation files were downloaded for the different species preserving the structure of the directories (FTP Ensembl repositories). For instance, for _Homo sapiens_: 
```
Homo_sapiens.GRCh38.98.gtf.gz @
our_mnt_dir + data/compressed/ + "ftp.ensembl.org/pub/release-98/gtf/homo_sapiens/"
```
our_mnt_dir is, as above, the local directory where all the data were downloaded.

##### Taxonomy ids of the different species annotated in Ensembl
The taxonomy id of each species has been downloaded from Ensembl for each division: [prokaryotes (archaea, bacteria)](http://ftp.ensemblgenomes.org/pub/bacteria/release-49/species_EnsemblBacteria.txt), [protists](http://ftp.ensemblgenomes.org/pub/protists/release-49/species_EnsemblProtists.txt), [plants](http://ftp.ensemblgenomes.org/pub/plants/release-49/species_EnsemblPlants.txt), [fungi](http://ftp.ensemblgenomes.org/pub/fungi/release-49/species_EnsemblFungi.txt), [metazoa (invertebrates)](http://ftp.ensemblgenomes.org/pub/metazoa/release-49/species_EnsemblMetazoa.txt), [vertebrates](https://ftp.ensembl.org/pub/release-98/species_EnsemblVertebrates.txt).  

---
#### The lengths of protein coding genes and proteins
The length of any protein coding gene or protein for all the used species can be accessed from our server:   
[https://genford.uv.es:5001/sharing/P79EcUfhE](https://genford.uv.es:5001/sharing/P79EcUfhE)

---
### main_tables
The files for protein coding genes, proteins, and the intersection set between them (merged) are provided in standard [tab-separated values](https://en.wikipedia.org/wiki/Tab-separated_values) (*.tsv):
- stat_protCodGenes.tsv (header line + 33627 entries).  
- stat_proteins.tsv (header line + 9913 entries).  
- stat_merged (header line + 6519 entries).  

Also, a file for the merged set with the mean gene length vs. rho (fraction of nCDS within the protein coding genes). The entries are ordered by ascending mean gene length:  
- rho_vs_gene.dat (three header lines + 6519 entries).

#### **Number of entries per taxonomical division:**
stat_protCodGenes.tsv (header line + 33627 entries):  

| counts | regnum                       |  
|-----:  |:----------                   |
| 31943  | bacteria<sup>*</sup>         |
| 237    | protists                     |
| 96     | plants                       |
| 1014   | fungi                        |
| 115    | metazoa (invertebrates)      |
| 222    | vertebrates                  |
33627 entries in total  

<sup>*</sup>Note that Ensembl Bacteria is a browser for bacterial and archaeal genomes. Then, the 31943 entries are divided, using the taxonomy classification, in 30714 Bacteria and 1229 Archaea.  

stat_proteins.tsv (header line + 9,913 entries):  

| counts | domain |  
|-----:|:-------- |
| 330  | archaea  |
| 7997 | bacteria |
| 1586 | eukaryota<sup>*</sup> |
9913 entries in total

<sup>*</sup>In the annotations from Uniprot, eukaryota includes: protists (156), plants (184), fungi (772), invertebrates (226), vertebrates (248). That is, the 1586 eukaryota has been classified using the taxonomy. Moreover, we validated that the last 156 species were protists, but protists is not a taxon, then we double-checked that Ensembl had them classified as protists too. 

stat_merged.tsv (header line + 6519 entries):  

| counts | regnum      |  
|-----:  |:----------  |
| 5468   | bacteria    |
| 227    | archaea     |
| 91     | protists    |
| 59     | plants      |
| 533    | fungi       |
| 49     | metazoa (invertebrates) |
| 92     | vertebrates |
6519 entries in total  

#### suppl_tables
- gene_length_vs_divergenece_time.tsv
- protCodGenes_averageLg_perGoOrg.txt
- proteins_averageLp_perGoOrg.txt

#### suppl_tables__extra
- species_Ensembl.tsv. The file contains the taxonomy ids of the different species annotated in Ensembl, [see above](https://github.com/emuro/borrador/blob/main/README.md#taxonomy-ids-of-the-different-species-annotated-in-ensembl). The files for the different divisions have been concatenated into species_Ensembl.tsv, maintaining only the first header. Finally, the file has been slimmed-down reducing its columns to species, species name and taxonomy_id.  
- genes.xlsx, proteins.xlsx, and genes_proteins_combined.xlsx. The main_tables in Microsoft Excel format, for the sake of those that use MS formats.  
- 480lognormal.dat. Initial seed for the gene growth model: 5000 gene lognormally distributed with mean 480
- clade_fraction_per_mean_length.xlsx data to represent Figs. S8 and S9
- Homo_sapiens_CDS_nCDS.xlsx data needed to compare the length frequency distribution for coding (CDS) and non-coding (nCDS) genetic sequences, see Fig. S10

---
### main_work
- [protCodGenes_lognormDist.ipynb](https://github.com/emuro/borrador/blob/main/main_work/protCodGenes_lognormDist.ipynb) and [proteins_lognormDist.ipynb](https://github.com/emuro/borrador/blob/main/main_work/proteins_lognormDist.ipynb): the distributions of the lengths of the protein coding genes (genes hereafter) and proteins respectively. See Fig.1, also S1, S2, and S7.  
- [protCodGenes_taylorLaw.ipynb](https://github.com/emuro/borrador/blob/main/main_work/protCodGenes_taylorLaw.ipynb) and [proteins_taylorLaw.ipynb](https://github.com/emuro/borrador/blob/main/main_work/proteins_taylorLaw.ipynb): the observed Taylor law in the distributions of the lengths of genes and proteins (variance vs mean in $log_{10}$ representation) for the different species. See Fig. 2.  
- [relation_proteins_protCodGenes_lengths.ipynb](https://github.com/emuro/borrador/blob/main/main_work/relation_proteins_protCodGenes_lengths.ipynb): threshold in the relationship between the mean gene length and the mean protein length for the different species. See Fig. 3.   
- [rho_nCDS_within_protCodGenes_lengths.ipynb](https://github.com/emuro/borrador/blob/main/main_work/rho_nCDS_within_protCodGenes_lengths.ipynb). Second-order phase transition in the density ($\rho$) of non-coding sequences within protein coding genes with the mean gene length as control parameter. See Fig. 4. 
- allowed_states.f. It calculates the allowed states of Fig. 4.
 
#### suppl_work  
- reliability_fit.ipynb: calculates the log-likelihood that fits the different distributions compared in the figures. See, Figs. S? and Fig. S? 
-  [mean_vs_time.ipynb](https://github.com/emuro/borrador/blob/main/main_work/suppl_work/mean_vs_time.ipynb). It is represented, along the evolutionary history of life, the average (for the genomes that compose each group of organisms) of the mean gene lengths against their divergence time from LUCA. Similarly, it is displayed the average (group of organisms) of the mean of the gene lengths' logarithm against the evolutionary divergence time from LUCA. That is,  $\overline{<L>}$ (nt) and $\overline{<log L>}$ (nt) vs. divergence time from LUCA (Mya).
 
- [protCodGenes_2nd_order_momentum.ipynb](https://github.com/emuro/borrador/blob/main/main_work/suppl_work/protCodGenes_2nd_order_momentum.ipynb). The observed generalized Taylor law for the protein coding gene length's distributions for the different genomes:  
 $(\sigma^{2} + <L_{g}>^{2})$ vs $<L_{g}>$ in $log_{10}$ representation; the second order momentum $<L_{g}^{2}>$ that corresponds to extended data Fig. 4 that complements the main Fig 2.  
- [proteins_2nd_order_momentum.ipynb](https://github.com/emuro/borrador/blob/main/main_work/suppl_work/proteins_2nd_order_momentum.ipynb) proteins_2nd_order_momentum.ipynb. The same for proteins, that is the observed generalized Taylor law for the protein length's distributions for the different species:  
 $(\sigma^{2} + <L_{p}>^{2})$ vs $<L_{p}>$ in $log_{10}$ representation); the second order momentum $<L_{p}^{2}>$ that corresponds to extended data Fig. 4 that complements the main Fig 2.
- [protCodGenes_meanOfLog_logOfMean.ipynb](https://github.com/emuro/borrador/blob/main/main_work/suppl_work/protCodGenes_meanOfLog_logOfMean.ipynb). Comparison for the protein coding gene length's distributions for the different genomes between: the mean of the log of the lengths and the log of the mean of lengths  
 $<log L>$ vs $log<L>$ in $log_{10}$ representation); it corresponds to the extended data Fig. 5.  
 - [average_mean_lengths__order.ipynb](https://github.com/emuro/borrador/blob/main/main_work/suppl_work/average_mean_lengths__order.ipynb). Fig 6a. Order of the average mean gene lengths for the different groups of organisms; Fig 6b. Same representations for the average protein gene lengths.
 - [meanLg_distribution__perGofOrg.ipynb](https://github.com/emuro/borrador/blob/main/main_work/suppl_work/meanLg_distribution__perGofOrg.ipynb). Distribution of the mean gene lengths to Fungi (1014 genomes); it corresponds to the extended data Fig. 9a. Note: Fig. 9b was calculated using code from the main_work section, see [relation_proteins_protCodGenes_lengths.ipynb](https://github.com/emuro/borrador/blob/main/main_work/relation_proteins_protCodGenes_lengths.ipynb).
- entropy.f: calculates the entropy of the allowed states of the unitary density on non-coding genetic sequences. See, Fig. S?  

#### suppl_work__extra  
- [merged_taylorLaw.ipynb](https://github.com/emuro/borrador/blob/main/main_work/suppl_work__extra/merged_taylorLaw.ipynb). The observed Taylor law in the merged set for the different species for which we have records in both proteins and protein coding genes (variance vs mean in $log_{10}$ representation). This is an extension of Fig. 2.  
- gene_growth_simulator.f for the sake of Fig. S? and Fig. S?  
- variance.f: calculates the variance of the states of the unitary density on non-coding genetic sequences. See, Fig. S?  
- random_scale_shape.f bla, bla, bla
