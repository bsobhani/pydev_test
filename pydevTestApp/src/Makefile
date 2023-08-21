TOP=../..

include $(TOP)/configure/CONFIG
include $(PYDEVICE)/configure/CONFIG.PyDevice
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = pydevTest
# pydevTest.dbd will be created and installed
DBD += pydevTest.dbd

# pydevTest.dbd will be made up from these files:
pydevTest_DBD += base.dbd

# Include dbd files from all support applications:
#pydevTest_DBD += xxx.dbd
pydevTest_DBD += pydev.dbd

# Add all the support libraries needed by this IOC
#pydevTest_LIBS += xxx
pydevTest_LIBS += pydev

# pydevTest_registerRecordDeviceDriver.cpp derives from pydevTest.dbd
pydevTest_SRCS += pydevTest_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
pydevTest_SRCS_DEFAULT += pydevTestMain.cpp
pydevTest_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#pydevTest_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
pydevTest_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

