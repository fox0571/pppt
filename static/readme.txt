######################################################################

INTEGRATED DELL(TM) REMOTE ACCESS CONTROLLER 6 (iDRAC6) Version 2.30

######################################################################

This document contains updated information about the Integrated Dell
Remote Access Controller 6.

For more information about iDRAC6, including installation and
configuration information, see the "Integrated Dell Remote Access
Controller 6 (iDRAC6) Enterprise for Blade Servers Version 2.2
User Guide" and the "Dell OpenManage(TM) Server Administrator
User's Guide." These documents are located on the Dell Support
website at "support.dell.com/manuals".

######################################################################
TABLE OF CONTENTS
######################################################################

This file contains the following sections: 

* Criticality 

* Minimum Requirements  

* Release Highlights 

* Known Issues 

######################################################################
CRITICALITY
######################################################################

2 - Recommended 

######################################################################
MINIMUM REQUIREMENTS
######################################################################

======================================================================
SUPPORTED SYSTEMS
======================================================================

iDRAC6 is supported on the following Dell PowerEdge(TM) systems
in the Dell PowerEdge M1000e system enclosure:

* Dell PowerEdge M610
* Dell PowerEdge M710
* Dell PowerEdge M910


======================================================================
SUPPORTED MANAGED SERVER OPERATING SYSTEMS
======================================================================
The iDRAC6 is supported by the following operating systems:

* Microsoft(R) Windows Server(R) 2003 family

  The Windows Server 2003 family includes:
  - Windows Server 2003 R2 (Web, Standard, and Enterprise 
    Editions) with SP2 (x86)
  - Windows Server 2003 R2 (Standard, Enterprise, and DataCenter
    Editions) with SP2 (x86_64)
  - Windows Server 2003 R2 SBS (Standard and Premium Editions) with SP2

* Microsoft Windows Server 2008 SP2 with core (Web, Standard, 
  Enterprise, and DataCenter Editions) (x86)

* Microsoft Windows Server 2008 SP2 with core (Standard, Enterprise,
  and DataCenter Editions) (x86_64)

* Microsoft Windows Server 2008 EBS SP2 (Standard and Premium Editions)

* Microsoft Windows Server 2008 R2 (Web, Standard, Enterprise,  
  and DataCenter Editions) (x86_64)

* Microsoft Windows Server 2008 HPC Edition

* SUSE(R) Linux Enterprise Server (SLES) 10 SP3

* SUSE Linux Enterprise Server (SLES) 11

* Red Hat(R) Enterprise Linux (RHEL) 4.8 (x86, x86_64)

* RHEL 5.4 (x86, x86_64) with kernel-2.6.18-164.9.1.el5 or later

* XenServer(TM) 5.5 - SD, USB, HDD

* Hyper-V Server and Hyper-V

* VMware(R) ESX(TM) 3.5 Update 4

* VMware ESX 4.0 Update 1

* ESXi(TM) 3.5 Update5 Flash (M610 and M710 only) (See the Note below.)

* ESXi 4.0 Update1 Flash (See the Note below.)

Note: 
    Use the Dell-customized ESXi 3.5 Update 5 or Dell-customized 
    ESXi 4.0 Update 1 Embedded editions. These images are available 
    at support.dell.com and www.vmware.com. Remote deployment and 
    local installation of ESXi through vMedia is not supported for 
    standard ESXi Embedded version 3.5 Update 4 and ESXi Embedded 
    version 4.0, as the installation may fail with the error 
    message, “Installation failed as more than one USB device
    found.”  


======================================================================
SUPPORTED WEB BROWSERS
======================================================================
* Microsoft Internet Explorer(R) 6.0 with SP2 for Microsoft Windows(R)
  XP, Windows 2003 Server Gold, Windows 2003 Server SP1, and Windows
  2003 Server SP2   

* Microsoft Internet Explorer 7.0 for Windows 2003 Server Gold, 
  Windows 2003 Server SP1, Windows 2003 Server SP2, Windows Server 
  2008, Windows XP, and Windows Vista(R)

* Microsoft Internet Explorer 8.0 for Windows 2003 Server Gold, 
  Windows 2003 Server SP1, Windows 2003 Server SP2, Windows Server 
  2008, Windows Server 2008 R2, Windows XP, and Windows Vista(R).   
  Internet Explorer 8 requires Java(TM) Runtime Environment (JRE)
  version 1.6.14 or later

* Mozilla(R) Firefox(R) 3.0 on Windows 2003 Server Gold, Windows 2003 
  Server SP1, Windows 2003 Server SP2, Windows 2000 Professional, Windows XP,  
  Windows Server 2008, Windows Vista, RHEL 4, RHEL 5, SLES 10, and
  SLES 11


======================================================================
FIRMWARE VERSIONS
======================================================================
Recommended firmware versions for CMC and BIOS:

* CMC Firmware: 2.3
* Dell PowerEdge M610 BIOS: 1.3.x or later
* Dell PowerEdge M710 BIOS: 1.3.x or later
* Dell PowerEdge M910 BIOS: 1.0.x or later


######################################################################
RELEASE HIGHLIGHTS (FIRMWARE VERSION 2.30)
######################################################################

* Provides support for M910 system
* Add redundancy support for internal SD module (M910 only)
* Regular Maintenance


######################################################################
IMPORTANT NOTES AND KNOWN ISSUES FOR iDRAC6 2.30
######################################################################
This section provides important notes and additional information about 
known issues for the iDRAC6 Firmware version 2.30:

* Remote Services: When using TFTP to download an ISO image to the 
  vFlash, if the image exceeds the partition size, no error message 
  is flagged. However, subsequent operations on the ISO will fail.

* Remote Services: Currently, installing SLES 11 remotely is not functional.

* If you reconfigure your client system’s display language, ensure 
  that the “Language for non-Unicode programs” setting matches the 
  selected “Display language”. If these settings do not match, some 
  or all of the ActiveX(TM) vKVM display elements (menu items, dialogs, 
  and so on) may not display properly. For more information about
  setting the display language and system locale, see the Windows
  Help and Support center on your system.

* On certain hardware configurations, firmware downgrades are 
  not allowed in this release.
 
* For Remote Enablement auto-discovery, ensure that you do not 
  assign a user ID with spaces on the provisioning server. This is 
  because even though this user ID will be successfully downloaded
  and provisioned on iDRAC6 during the auto-discovery process, the 
  account will not be usable as  iDRAC6 rejects any user ID with
  spaces.

* For ESX 4.0, if you try to install Dell Update Packages (DUPs),
  Systems Build and Update Utility or OpenManage(TM) Server Administrator
  (OMSA) using vMedia, the installation fails. To work around this
  issue, disable the "System Services" using iDRAC6 Configuration 
  Utility (Ctrl-E) in POST, and then use the OpenManage DVD. The "System
  Services" can be re-enabled after the OpenManage DVD installation is
  complete.

* If you run DUPs when vFlash is in use, the vFlash is disconnected
  and reconnected. If a write operation is in progress, this action
  can corrupt the vFlash contents. If this occurs, the vFlash card 
  will have to be re-initialized. 

* Reboot the managed system running on VMware ESX 3.x operating
  system after an iDRAC6 update is completed. This ensures that
  the VMware ESX operating system re-enumerates the virtual 
  devices and enables virtual floppy and virtual CD-ROM 
  features of the iDRAC6. After the reboot, virtual devices
 including virtual floppy, work as expected.

* The iDRAC6 can be updated using the DOS utility when DOS is booted
  using PXE. However, the new firmware image has to be on a
  local media on the system for this to work properly. Local 
  media can be a RAMDISK, HD, or a USB key on the server.  
  Alternatively, the update of iDRAC6 on multiple systems has
  to be sequenced. It should be done one system after the other, 
  with the first system completing update and the second system 
  starting update and on to the third after the second is done, 
  and fourth after the third is done, and so on.

* On systems running Windows operating systems, the Internet
  Explorer window(s) for any media will not close by 
  themselves if you remove the media. You must close the 
  window(s) after you remove the media.

  On systems running Linux operating systems, the Internet
  Explorer window(s) for any media will close by 
  themselves if you remove the media.

* iDRAC6 Linux DUPs do not support VMware ESX 4.0 operating 
  systems. If the Linux DUP for iDRAC6 is run on VMware 
  ESX 4.0, the DUP will fail. 

  You can update iDRAC6 using one of the following methods:

    - CMC GUI-based update

    - iDRAC6 GUI-based update

    - Remote RACADM-based update

* If you receive the message "A webpage is not responding on
  the following website" in Internet Explorer 8.0, see:

  "http://blogs.msdn.com/ie/archive/2009/05/04
  /ie8-in-windows-7-rc-reliability-and-telemetry.aspx"

  "http://support.microsoft.com/?kbid=970858"

* In Internet Explorer 7.0, if several tabs are open and you launch
  the iDRAC6 remote console, all the tabs are hidden while 
  the remote console is open. If the tab warning is turned off and
  you close the remote console, all the tabs and the browser will
  close without warning. 

  To prevent this, go to "Internet Properties" > "Tabs" > 
  "Settings" and select the "Warn me when closing multiple tabs"
  option.
  
* If multiple iDRAC6 web GUI sessions are launched through CMC 
  single sign-on, "racadm getssninfo" will show information
  only for the first session.
  
* To use iVMCLI on Microsoft Windows Vista operating systems, 
  the user requires administrator privileges. If iVMCLI is run on 
  Vista to connect a CD or ISO image without administrator 
  privileges, it appears to be working, but will eventually
  timeout and ask the user to check network/proxy settings. 
  This same command will work if the 'cmd' prompt is opened
  with administrator privileges. 
  
* If a vMedia drive is disconnected using the "OS eject" option, 
  then the drive may not be available until the operating 
  system re-enumerates the USB devices. For the operating system
  to auto-detect the vMedia drive, the iDRAC6 vMedia device 
  can be reattached by doing the following:

  Go to "System" > "Console/media" >"Configuration", select 
  "Set Attach Virtual Media to Detach" and click "Apply". 
  Next, "Set Attach Virtual Media to Attach" and click
  "Apply".

* The "racresetcfg" command in RACADM restores all properties to
  their default values except "cfgDNSRacName" in the
  "cfgLanNetworking" group.

* The actual time for the "racresetcfg" command within racadm
  to execute may vary depending on the network speed.

* The iDRAC6 Linux DUP cannot be run on 64-bit RHEL 4 Update 7 
  due to known issues in that operating system. See the Red Hat 
  KB article at "http://kbase.redhat.com/faq/docs/DOC-3402" to 
  use the DUP on RHEL 4 Update 7.

* Smart Card login fails after a logout from the same browser window. 
  Open a new browser window to login.

* When using RACADM to configure iDRAC6 when using a configuration
  file, indexed groups will not operate properly. 

* When using remote RACADM to configure iDRAC6 when using a
  configuration file, changing objects that affect the network
  connection will stop the rest of the configuration file
  from taking effect.

######################################################################

Information in this document is subject to change without notice.
(C) 2010 Dell Inc. All rights reserved.

Reproduction of these materials in any manner whatsoever without
the written permission of Dell Inc. is strictly forbidden.

Trademarks used in this text: "Dell", "OpenManage", and "PowerEdge"
are trademarks of Dell Inc.; "Microsoft", "Windows", "Internet
Explorer", "Windows Server", "Windows Vista", "ActiveX", 
"Hyper-V Server", "Hyper-V", and "Active Directory" are either 
trademarks or registered trademarks of Microsoft Corporation 
in the United States and/or other countries; "Intel" is
a registered trademark of Intel Corporation in the United States
and other countries; "SUSE" is a registered trademark of Novell
Corporation; "Red Hat" and "Red Hat Enterprise Linux" are registered 
trademarks of Red Hat, Inc. in the United States and other countries; 
"VMware", "ESX Server", and "ESXi Server” are registered trademarks 
or trademarks of VMware, Inc. in the United States and/or other 
jurisdictions; "XenServer" is a trademark of Citrix Systems, Inc. in the 
United States and/or other countries; "Java" is a trademarks of Sun 
Microsystems, Inc. in the United States and other countries; "Mozilla" 
and "Firefox" are either registered trademarks or trademarks of Mozilla 
Foundation.


Other trademarks and trade names may be used in this document to refer
to either the entities claiming the marks and names or their products.  
Dell Inc. disclaims any proprietary interest in trademarks and trade 
names other than its own.

March 2010