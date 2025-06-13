# Leaf-resource-acquisition-strategies
•	Data/LeafArea/Johanna_2015_PLA_Raw contains the downloaded Projected Leaf Area raw data as it is.  
•	Data/Branching/pheno_pilot_adj_trans2_2 contains branching data from Yang’s RDM uploaded data
•	Data/Branching/pheno_pilot_adj2_3 contains branching data from Yang’s RDM uploaded data in vertical format
•	Data/LeafArea/Control_PLA_J15 and Data/LeafArea/drought_PLA_J15 contains the treatment ABR and PLA28 from the easyGWAS_2017Raw
•	Data/Scripts/correlation.py is a generic script for correlation analysis
•	Data/Scripts/join_mean.py is a generic script for joining a field and storing mean of other fields in a few file
•	Data/LeafArea/Mean_Control_PLA_J15 contains mean leaf area data calculated using join_mean.py script
•	Data/Branching/Schmitt_Sci_molEcol13_PNAS19  contains raw data from https://www.pnas.org/doi/full/10.1073/pnas.1902731116  
•	Data/Branching/branching_easyGWAS_Dominik_2016 contains raw data from 
https://academic.oup.com/plcell/article/29/1/5/6099036?login=true and changed IID to ID column name
•	Data/Branching/Schmitt_PNAS19_Br contains only the branching data from the file  Data/Branching/Schmitt_Sci_molEcol13_PNAS19   and changed EcotypeID to ID column name
•	Data/Branching/br_pilot2_2 contains only branching data from Data/Branching/pheno_pilot_adj_trans2_2
•	Scripts/join_only.py  joins any files based on column name given to it.
•	Scripts/csv2xlsx.py takes a csv or tsv file and return a xlsx file.
•	Data/Climate/climatic_impute_data.xlsx contains raw climate data from rdm  
•	Data/Climate/cli.xlsx  and Data/Climate/cli_nullhand.xlsx  contains selected data from climatic Data/Climate/climatic_impute_data.xlsx and Data/Climate/cli_mean.xlsx contains joined files based on CS_number  
•	Data/Branching/m mean joined with mean taken for fields
•	Data/Branching/Branch_j combines all 3 mean branching data
•	Data/Branching/Br2_j doesnt not have the mbr_pilot2_2
•	Script/categorize.py creates categories in form of low average and high
•	Data/BrCli_cat.xlsx contains categorized in form of BrCli.xlsx
•	Scripts/cate_sep_file.py create separate file for each category that we want to predict
•	Folder FT has 2 files, one with ft time data and other with the climate data extracted using R
•	Pheno_env combines all datas and pheno_env_withoutLA contains no PLA data as there are no matchings
•	Folder Br_prd_cross has all the data after combining



