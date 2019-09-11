LOAD DATA INFILE 'C:database_research\\teledyne-Instrument-CONCENTRATIONS-08282019.txt'
INTO TABLE teledyne_instrument
FIELDS TERMINATED BY ' ;\t' 
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
