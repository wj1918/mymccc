#!/bin/bash
# This script execute following task
# 1. download the mdb file from the server
# 2. convert to sqlite and mysql 
# 3. upload the new sqlite file to the server
#
PROGNAME=$(basename $0)

error_exit()
{

	echo "${PROGNAME}: ${1:-"Unknown Error"}" 1>&2
	exit 1
}

convert_to_sqlite3()
{
	tables=$(mdb-tables $LIBRARY_MDB)
	[[ $tables == *CB-DB* ]] || error_exit "Not found LIB_CB-DB table in $LIBRARY_MDB."

	python access-dump.py $LIBRARY_MDB LIB |sqlite3 $LIBRARY_SQLITE_FILE

	cbdb_count=$(sqlite3 $LIBRARY_SQLITE_FILE 'select count(*) from `LIB_CB-DB`')

	[[ cbdb_count -gt 0 ]]  || error_exit "invalid LIB_CB-DB table"

	curl -T $LIBRARY_SQLITE_FILE -u ${FTP_USER}:${FTP_PASSWORD} ftp://${FTP_SERVER}/data/$LIBRARY_SQLITE_FILE || error_exit "Failed to upload to ftp server"

}

convert_to_mysql()
{
	python access-dump.py $LIBRARY_MDB LIB \
	| sed '/CREATE TABLE .*/ {N; s/CREATE TABLE .*\n (/&\n\t`id` int(10) NOT NULL auto_increment,\n \t PRIMARY KEY  (`id`), /g}' \
	| mysql --default-character-set=utf8 mymccc
}

PATH=$OPENSHIFT_DATA_DIR/usr/bin:$PATH
LIBRARY_MDB=MCCC-Library-Access2000.mdb
LIBRARY_SQLITE_FILE=mccc-library.db

. $OPENSHIFT_DATA_DIR/server.conf
curl -u ${FTP_USER}:${FTP_PASSWORD} ftp://${FTP_SERVER}/data/$LIBRARY_MDB > $LIBRARY_MDB

[[ -f  $LIBRARY_MDB ]] || error_exit "Failed to download $LIBRARY_MDB."

convert_to_sqlite3

convert_to_mysql

echo "done."
