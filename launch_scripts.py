#!/usr/bin/python

import os,sys,platform,time

distro_support_list = [ "CentOS" ]

current_versions_dict = { "CentOS":"6.3" }

def validate(distro, version):
        if distro not in distro_support_list:
                print "OS is not supported"
                sys.exit()

        up_to_date = 1
        if version != current_versions_dict[distro]:
                up_to_date = 0

        openvz = 0
        if os.path.isfile('/proc/vz/veinfo') == True:
                openvz = 1

        return(up_to_date, openvz)

 
def distro_update(openvz_check, distro, version):
        if openvz_check == 1:
                print "OpenVZ Detected\nDistro Detected: %s \nVersion Detected: %s \nUpdating System Now" % (distro, version)
                time.sleep(1)
                os.system("yum -y update")
                print "System update is complete\n\nPlease restart ./launch.py after reboot is compelte"
                time.sleep(1)
                os.system("reboot")

distro_obj = platform.linux_distribution()

validate_check = validate(distro_obj[0], distro_obj[1])


if validate_check[0] == 0:
        distro_update(validate_check[1], distro_obj[0], distro_obj[1])


