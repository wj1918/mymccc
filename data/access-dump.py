#!/usr/bin/env python
#
# AccessDump.py
# A simple script to dump the contents of a Microsoft Access Database.
# It depends upon the mdbtools suite:
#   http://sourceforge.net/projects/mdbtools/
 
import sys, subprocess, os
 
DATABASE = sys.argv[1]
NAMESPACE = sys.argv[2]
 
# Get the list of table names with "mdb-tables"
table_names = subprocess.Popen(["mdb-tables", "-1", DATABASE],
                               stdout=subprocess.PIPE).communicate()[0]
tables = table_names.splitlines()

for table in tables:
    if table != '':
        print "DROP TABLE IF EXISTS `{0}_{1}`;".format(NAMESPACE,table)

sys.stdout.flush()

# Dump the schema for the DB
subprocess.call(["mdb-schema", "-N", NAMESPACE , DATABASE, "mysql"])

print "BEGIN;" # start a transaction, speeds things up when importing
 
sys.stdout.flush()
 
# Dump each table as a CSV file using "mdb-export",
# converting " " in table names to "_" for the CSV filenames.
for table in tables:
    if table != '':
        subprocess.call(["mdb-export", "-N", NAMESPACE, "-I", "mysql", DATABASE, table])
 
print "COMMIT;" # end the transaction
sys.stdout.flush()
