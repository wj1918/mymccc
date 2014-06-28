 python access-dump.py MCCC-Library-Access2000.mdb LIB >mymccc.sql
 mysql -u root --password=admin mymccc< mymccc.sql 
