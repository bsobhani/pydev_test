#!../../bin/linux-x86_64/pydevTest

#- You may have to change pydevTest to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/pydevTest.dbd"
pydevTest_registerRecordDeviceDriver pdbbase

## Load record instances
dbLoadRecords("db/pydev_bug_test.template","P=q8i:")
dbLoadRecords("db/pydev_bug_test.template","P=q8i2:")
dbLoadRecords("db/pydev_bug_test.template","P=q8i3:")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=q8i"

pydev("import sys")
#pydev("sys.path.append('/SNS/users/q8i/iocs/pydev_test')")
pydev("sys.path.append('/home/q8i/iocs/pydev_test2/pydev_test')")
pydev("import bug_test")
