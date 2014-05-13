-- ----------------------------------------------------------
-- MDB Tools - A library for reading MS Access database files
-- Copyright (C) 2000-2011 Brian Bruns and others.
-- Files in libmdb are licensed under LGPL and the utilities under
-- the GPL, see COPYING.LIB and COPYING files respectively.
-- Check out http://mdbtools.sourceforge.net
-- ----------------------------------------------------------

-- That file uses encoding UTF-8

CREATE TABLE `CB-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (160), 
	`Title`			varchar (240), 
	`AutoCounter`			int, 
	`ClutterNumber`			varchar (12), 
	`Keeper`			varchar (20), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `EB-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (8), 
	`Author`			varchar (100), 
	`Title`			varchar (200), 
	`AutoCounter`			int, 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Application`			varchar (100)
);

CREATE TABLE `CCD-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `Choir-DB`
 (
	`ClassNumber`			varchar (20), 
	`Title`			varchar (240), 
	`Author`			varchar (160), 
	`ClutterNumber`			varchar (12), 
	`Volume`			varchar (6), 
	`ResourceNumber`			varchar (10), 
	`CopyNumber`			int, 
	`AutoCounter`			int, 
	`Keeper`			varchar (20), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `ClassNumberLookUpTable old copy - can be deleted later`
 (
	`DeweyClassNumber`			varchar (100), 
	`MCCCPre96ClassNumber`			varchar (100), 
	`AFCcatalogNumber`			varchar (100), 
	`DeweyClassNumberDescription`			varchar (400), 
	`DeweyClassNumberChineseDescription`			varchar (100), 
	`KeeperIndex1`			int, 
	`KeeperIndex2`			int
);

CREATE TABLE `CT-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `CV-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (10), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Application`			varchar (100), 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `DummyRecordTable`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (8), 
	`Author`			varchar (100), 
	`Title`			varchar (200), 
	`AutoCounter`			int, 
	`Keeper`			varchar (40)
);

CREATE TABLE `EB-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (8), 
	`Author`			varchar (100), 
	`Title`			varchar (200), 
	`AutoCounter`			int, 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Application`			varchar (100)
);

CREATE TABLE `ECD-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `ET-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `EV-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Application`			varchar (100)
);

CREATE TABLE `General Purpose Label`
 (
	`UpperLeft`			varchar (20), 
	`FirstLine`			varchar (400), 
	`SecondLine`			varchar (200), 
	`AutoCounter`			int
);

CREATE TABLE `KCB-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (140), 
	`AutoCounter`			int, 
	`ClutterNumber`			varchar (12), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `KCT-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (10), 
	`Title`			varchar (160), 
	`Author`			varchar (120), 
	`AutoCounter`			int, 
	`ISBN`			varchar (100), 
	`RunningTime`			varchar (40), 
	`Series`			varchar (200), 
	`Owner`			varchar (100), 
	`MCCCPurchaseDate`			varchar (100), 
	`PurchasePrice`			varchar (100), 
	`Comment`			varchar (200), 
	`ClutterNumber`			varchar (20), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Comments`			varchar (400)
);

CREATE TABLE `KCV-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (10), 
	`Title`			varchar (160), 
	`Author`			varchar (120), 
	`ISBN`			varchar (100), 
	`RunningTime`			varchar (40), 
	`Series`			varchar (200), 
	`Owner`			varchar (100), 
	`MCCCPurchaseDate`			varchar (100), 
	`PurchasePrice`			varchar (100), 
	`AutoCounter`			int, 
	`Comment`			varchar (200), 
	`ClutterNumber`			varchar (20), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Comments`			varchar (400)
);

CREATE TABLE `KEB-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (160), 
	`AutoCounter`			int, 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `KECD-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `KeeperIndexTable`
 (
	`KeeperIndex`			int, 
	`ChineseName`			varchar (100), 
	`EnglishName`			varchar (100), 
	`TelephoneNumber`			varchar (30), 
	`Comments`			varchar (100)
);

CREATE TABLE `KeeperPreferenceTable`
 (
	`DeweyCallNumber`			varchar (100), 
	`KeeperIndex1`			int, 
	`KeeperIndex2`			int, 
	`KeeperIndex3`			int, 
	`Comments`			varchar (100)
);

CREATE TABLE `KEV-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (10), 
	`Title`			varchar (160), 
	`Author`			varchar (120), 
	`Keeper`			varchar (40), 
	`ISBN`			varchar (100), 
	`RunningTime`			varchar (40), 
	`Series`			varchar (200), 
	`Owner`			varchar (100), 
	`MCCCPurchaseDate`			varchar (100), 
	`PurchasePrice`			varchar (100), 
	`AutoCounter`			int, 
	`Comment`			varchar (200), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Comments`			varchar (400)
);

CREATE TABLE `Pre96CB-DB`
 (
	`Pre96AssessionNumber`			varchar (100), 
	`Keeper`			varchar (20), 
	`Pre96ClassNumber`			varchar (20), 
	`Title`			varchar (140), 
	`Author`			varchar (60), 
	`Volume`			varchar (6), 
	`AutoCounter`			int, 
	`KeeperIndex`			int
);

CREATE TABLE `Pre96EB-DB-old`
 (
	`Pre96AssessionNumber`			varchar (100), 
	`Pre96ClassNumber`			varchar (20), 
	`Title`			varchar (140), 
	`Author`			varchar (80), 
	`Volume`			varchar (6), 
	`AutoCounter`			int, 
	`Keeper`			varchar (20), 
	`KeeperIndex`			int
);

CREATE TABLE `RomanPinInTable`
 (
	`ChineseCharacter`			varchar (10), 
	`ClutterNumber`			varchar (12)
);

CREATE TABLE `VBSTapes`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int
);

CREATE TABLE `YCM-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (100), 
	`Title`			varchar (140), 
	`AutoCounter`			int, 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `YCV-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `YearIndexTable`
 (
	`YearIndex`			varchar (8), 
	`Year`			varchar (12)
);

CREATE TABLE `YEB-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (60), 
	`Title`			varchar (200), 
	`AutoCounter`			int, 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `YEV-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `書架編目`
 (
	`DeweyClassNumber`			varchar (20), 
	`DeweyClassNumberDescription`			varchar (400), 
	`DeweyClassNumberChineseDescription`			varchar (200), 
	`AutoCounter`			int
);

CREATE TABLE `書架編目old`
 (
	`DeweyClassNumber`			varchar (20), 
	`DeweyClassNumberDescription`			varchar (400), 
	`DeweyClassNumberChineseDescription`			varchar (200), 
	`AutoCounter`			int
);

CREATE TABLE `CCD-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `Choir-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Title`			varchar (240), 
	`Author`			varchar (160), 
	`ClutterNumber`			varchar (12), 
	`Volume`			varchar (6), 
	`ResourceNumber`			varchar (10), 
	`CopyNumber`			int, 
	`AutoCounter`			int, 
	`Keeper`			varchar (20), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `ClassNumberLookUpTable1 old copy - can be deleted later`
 (
	`DeweyClassNumber`			varchar (100), 
	`MCCCPre96ClassNumber`			varchar (100), 
	`AFCcatalogNumber`			varchar (100), 
	`DeweyClassNumberDescription`			varchar (400), 
	`DeweyClassNumberChineseDescription`			varchar (100), 
	`KeeperIndex1`			int, 
	`KeeperIndex2`			int
);

CREATE TABLE `CT-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `CV-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (10), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Application`			varchar (100), 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `DummyRecordTable1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (8), 
	`Author`			varchar (100), 
	`Title`			varchar (200), 
	`AutoCounter`			int, 
	`Keeper`			varchar (40)
);

CREATE TABLE `EB-DB2`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (8), 
	`Author`			varchar (100), 
	`Title`			varchar (200), 
	`AutoCounter`			int, 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Application`			varchar (100)
);

CREATE TABLE `ECD-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `ET-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `EV-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Application`			varchar (100)
);

CREATE TABLE `General Purpose Label1`
 (
	`UpperLeft`			varchar (20), 
	`FirstLine`			varchar (400), 
	`SecondLine`			varchar (200), 
	`AutoCounter`			int
);

CREATE TABLE `KCB-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (140), 
	`AutoCounter`			int, 
	`ClutterNumber`			varchar (12), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `KCT-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (10), 
	`Title`			varchar (160), 
	`Author`			varchar (120), 
	`AutoCounter`			int, 
	`ISBN`			varchar (100), 
	`RunningTime`			varchar (40), 
	`Series`			varchar (200), 
	`Owner`			varchar (100), 
	`MCCCPurchaseDate`			varchar (100), 
	`PurchasePrice`			varchar (100), 
	`Comment`			varchar (200), 
	`ClutterNumber`			varchar (20), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Comments`			varchar (400)
);

CREATE TABLE `KCV-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (10), 
	`Title`			varchar (160), 
	`Author`			varchar (120), 
	`ISBN`			varchar (100), 
	`RunningTime`			varchar (40), 
	`Series`			varchar (200), 
	`Owner`			varchar (100), 
	`MCCCPurchaseDate`			varchar (100), 
	`PurchasePrice`			varchar (100), 
	`AutoCounter`			int, 
	`Comment`			varchar (200), 
	`ClutterNumber`			varchar (20), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Comments`			varchar (400)
);

CREATE TABLE `KEB-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (160), 
	`AutoCounter`			int, 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `KECD-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `KeeperIndexTable1`
 (
	`KeeperIndex`			int, 
	`ChineseName`			varchar (100), 
	`EnglishName`			varchar (100), 
	`TelephoneNumber`			varchar (30), 
	`Comments`			varchar (100)
);

CREATE TABLE `KeeperPreferenceTable1`
 (
	`DeweyCallNumber`			varchar (100), 
	`KeeperIndex1`			int, 
	`KeeperIndex2`			int, 
	`KeeperIndex3`			int, 
	`Comments`			varchar (100)
);

CREATE TABLE `KEV-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (10), 
	`Title`			varchar (160), 
	`Author`			varchar (120), 
	`Keeper`			varchar (40), 
	`ISBN`			varchar (100), 
	`RunningTime`			varchar (40), 
	`Series`			varchar (200), 
	`Owner`			varchar (100), 
	`MCCCPurchaseDate`			varchar (100), 
	`PurchasePrice`			varchar (100), 
	`AutoCounter`			int, 
	`Comment`			varchar (200), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30), 
	`Comments`			varchar (400)
);

CREATE TABLE `Pre96CB-DB1`
 (
	`Pre96AssessionNumber`			varchar (100), 
	`Keeper`			varchar (20), 
	`Pre96ClassNumber`			varchar (20), 
	`Title`			varchar (140), 
	`Author`			varchar (60), 
	`Volume`			varchar (6), 
	`AutoCounter`			int, 
	`KeeperIndex`			int
);

CREATE TABLE `Pre96EB-DB`
 (
	`Pre96AssessionNumber`			varchar (100), 
	`Pre96ClassNumber`			varchar (20), 
	`Title`			varchar (140), 
	`Author`			varchar (80), 
	`Volume`			varchar (6), 
	`AutoCounter`			int, 
	`Keeper`			varchar (20), 
	`KeeperIndex`			int
);

CREATE TABLE `RomanPinInTable1`
 (
	`ChineseCharacter`			varchar (10), 
	`ClutterNumber`			varchar (12)
);

CREATE TABLE `VBSTapes1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int
);

CREATE TABLE `YCM-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (100), 
	`Title`			varchar (140), 
	`AutoCounter`			int, 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `YCV-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `YearIndexTable1`
 (
	`YearIndex`			varchar (8), 
	`Year`			varchar (12)
);

CREATE TABLE `YEV-DB1`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (280), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (160), 
	`Comments`			varchar (510), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `書架編目1`
 (
	`DeweyClassNumber`			varchar (20), 
	`DeweyClassNumberDescription`			varchar (400), 
	`DeweyClassNumberChineseDescription`			varchar (200), 
	`AutoCounter`			int
);

CREATE TABLE `書架編目old1`
 (
	`DeweyClassNumber`			varchar (20), 
	`DeweyClassNumberDescription`			varchar (400), 
	`DeweyClassNumberChineseDescription`			varchar (200), 
	`AutoCounter`			int
);

CREATE TABLE `EDVD-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `CDVD-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `CB-DB的複本`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (160), 
	`Title`			varchar (240), 
	`AutoCounter`			int, 
	`ClutterNumber`			varchar (12), 
	`Keeper`			varchar (20), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `KEDVD-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `KCDVD-DB`
 (
	`ClassNumber`			varchar (20), 
	`Volume`			varchar (6), 
	`Author`			varchar (120), 
	`Title`			varchar (400), 
	`ClutterNumber`			varchar (10), 
	`AutoCounter`			int, 
	`Time`			varchar (40), 
	`Series`			varchar (100), 
	`Comments`			varchar (400), 
	`Keeper`			varchar (40), 
	`KeeperIndex`			int, 
	`InputDate`			varchar (30)
);

CREATE TABLE `ClassNumberLookUpTable`
 (
	`DeweyClassNumber`			varchar (100), 
	`MCCCPre96ClassNumber`			varchar (100), 
	`AFCcatalogNumber`			varchar (100), 
	`DeweyClassNumberDescription`			varchar (400), 
	`DeweyClassNumberChineseDescription`			varchar (100), 
	`KeeperIndex1`			int, 
	`KeeperIndex2`			int
);

CREATE TABLE `貼上錯誤`
 (
	`DeweyClassNumber`			varchar (510), 
	`MCCCPre96ClassNumber`			varchar (510), 
	`AFCcatalogNumber`			varchar (510), 
	`DeweyClassNumberDescription`			varchar (510), 
	`DeweyClassNumberChineseDescription`			varchar (510), 
	`KeeperIndex1`			int, 
	`KeeperIndex2`			int
);


