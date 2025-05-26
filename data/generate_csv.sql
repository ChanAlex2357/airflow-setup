SELECT * FROM paiements
INTO OUTFILE '/home/chan-alex/projects/Airflow/paiements.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
