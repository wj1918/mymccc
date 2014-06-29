python access-dump.py MCCC-Library-Access2000.mdb LIB >mymccc.sql
sed '/CREATE TABLE .*/ {N; s/CREATE TABLE .*\n (/&\n\t`id` int(10) NOT NULL auto_increment,\n \t PRIMARY KEY  (`id`), /g}' mymccc.sql 

CREATE DATABASE mymccc CHARACTER SET utf8;
mysql --default-character-set=utf8 -u root --password=admin mymccc< mymccc.sql 


