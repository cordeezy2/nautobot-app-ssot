"""Constants for LibreNMS SSoT."""

from django.conf import settings

# Import config vars from nautobot_config.py
PLUGIN_CFG = settings.PLUGINS_CONFIG["nautobot_ssot"]

librenms_status_map = {
    0: "Offline",
    1: "Active",
    True: "Active",
    False: "Offline",
}

os_manufacturer_map = {
    # Other types
    "ping": "Generic",
    "hpe-ilo": "HP",
    "proxmox": "Proxmox",
    # Types from LibreNMS/OS php files
    "aen": "Accedian OS",
    "airos": "Ubiquiti",
    "airosaf": "Ubiquiti",
    "airosaf60": "Ubiquiti",
    "airosafltu": "Ubiquiti",
    "airport": "Apple",
    "aix": "IBM",
    "alcoma_almp": "Alcoma",
    "alfo80hd": "Siae Microelettronica",
    "allied": "Allied Telesis",
    "allworxvoip": "Allworx",
    "aos": "Alcatel-Lucent",
    "apc": "APC",
    "apexlynx": "Apex",
    "apexplus": "Apex",
    "aprisa": "4RF",
    "apsoluteos": "Radware",
    "arbos": "Aruba Networks",
    "areca": "Areca",
    "arrisc4": "Arris",
    "arriscm": "Arris",
    "arrisdsr4410md": "Arris",
    "arubainstant": "Aruba Networks",
    "arubaos": "Aruba Networks",
    "arubaoscx": "Aruba Networks",
    "asa": "Cisco",
    "asuswrtmerlin": "Asus",
    "asyncos": "Cisco",
    "aviatwtm": "Aviat Networks",
    "avocent": "Avocent",
    "awplus": "Allied Telesis",
    "axos": "Calix",
    "baicellsod04": "Baicells",
    "barracudangfirewall": "Barracuda",
    "bats": "BAT",
    "beagleboard": "BeagleBoard",
    "boss": "Beijer Electronics",
    "brother": "Brother",
    "ceraos": "Ceragon",
    "cienarls": "Ciena",
    "cienasds": "Ciena",
    "ciscosb": "Cisco",
    "ciscowlc": "Cisco",
    "cnpilote": "Cambium Networks",
    "comware": "HPE",
    "coriant": "Coriant",
    "cumulus": "Cumulus Networks",
    "cyberpower": "CyberPower",
    "danthermos": "Dantherm",
    "ddwrt": "DD-WRT",
    "deliberant": "Deliberant",
    "delllaser": "Dell",
    "dhcpatriot": "DHCPatriot",
    "dlink": "D-Link",
    "dlinkap": "D-Link",
    "dnos": "Dell EMC",
    "edgecos": "Edgecore",
    "edgeos": "Ubiquiti",
    "edgeosolt": "Ubiquiti",
    "edgeswitch": "Ubiquiti",
    "ekinops": "Ekinops",
    "eltexmes23xx": "Eltex",
    "eltexmes24xx": "Eltex",
    "engenius": "EnGenius",
    "enterasys": "Enterasys",
    "epmp": "Cambium Networks",
    "ericsson6600": "Ericsson",
    "ericssonml": "Ericsson",
    "ericssontn": "Ericsson",
    "eurostor": "Eurostor",
    "ewc": "Extreme Networks",
    "exa": "Exa Networks",
    "extendair": "ExtendAir",
    "extremeware": "Extreme Networks",
    "f5": "F5 Networks",
    "fabos": "Brocade",
    "fortiadc": "Fortinet",
    "fortiap": "Fortinet",
    "fortiextender": "Fortinet",
    "fortigate": "Fortinet",
    "fortios": "Fortinet",
    "fortiwlc": "Fortinet",
    "fscentec": "FS",
    "fsgbn": "FS",
    "fsswitch": "FS",
    "ftos": "Dell EMC",
    "gaia": "Check Point",
    "generic": "Generic",
    "gepulsar": "Ge",
    "harmonyenhanced": "Harmony",
    "helios": "Helios",
    "himoinstags": "Himoinsa",
    "hiveoswireless": "HiveOS",
    "horizoncompact": "Dragonwave",
    "horizoncompactplus": "Dragonwave",
    "horizonduo": "Dragonwave",
    "hpmsm": "HP",
    "hpvc": "HP",
    "icros": "Advantech",
    "ifotec": "Ifotec",
    "infineragroove": "Infinera",
    "infinity": "Infinity",
    "ios": "Cisco",
    "iosxe": "Cisco",
    "iosxr": "Cisco",
    "ipolis": "Samsung",
    "ird": "IRD",
    "ironware": "Brocade",
    "jetdirect": "HP",
    "junos": "Juniper",
    "junose": "Juniper",
    "lcos": "Lancom",
    "lcoslx": "Lancom",
    "lcossx": "Lancom",
    "linux": "Linux",
    "mimosa": "Mimosa Networks",
    "mni": "MNI",
    "moxaetherdevice": "Moxa",
    "mrvod": "MRV",
    "netscaler": "Citrix",
    "netsure": "NetSure",
    "nios": "Infoblox",
    "nitro": "Citrix",
    "nsbsd": "BSD",
    "ocnos": "OcNOS",
    "okilan": "Oki",
    "openbsd": "BSD",
    "openwrt": "OpenWrt",
    "packetlight": "PacketLight",
    "panos": "Palo Alto",
    "pbn": "PBN",
    "pbncp": "PBN",
    "pepwave": "Peplink",
    "pfsense": "PfSense",
    "pmp": "Cambium Networks",
    "poweralert": "APC",
    "powerconnect": "Dell EMC",
    "procurve": "HPE",
    "protelevisiont1": "ProTelevision",
    "ptp250": "Cambium Networks",
    "ptp500": "Cambium Networks",
    "ptp600": "Cambium Networks",
    "ptp650": "Cambium Networks",
    "ptp670": "Cambium Networks",
    "ptp800": "Cambium Networks",
    "pulse": "PulseSecure",
    "qnap": "QNAP",
    "quanta": "Quanta",
    "quantastor": "QuantaStor",
    "radlan": "Radlan",
    "radwin": "Radwin",
    "ray": "Racom",
    "ray3": "Racom",
    "riverbed": "Riverbed",
    "routeros": "Mikrotik",
    "ruckuswireless": "Ruckus",
    "ruckuswirelesshotzone": "Ruckus",
    "ruckuswirelesssz": "Ruckus",
    "ruckuswirelessunleashed": "Ruckus",
    "rutos2xx": "Teltonika",
    "rutosrutx": "Teltonika",
    "saf": "Saf Tehnika",
    "safcfm": "Saf Tehnika",
    "safintegrab": "Saf Tehnika",
    "safintegrae": "Saf Tehnika",
    "safintegraw": "Saf Tehnika",
    "safintegrax": "Saf Tehnika",
    "scalance": "Siemens",
    "schleifenbauer": "Schleifenbauer",
    "screenos": "Juniper",
    "secureplatform": "Check Point",
    "serveriron": "Brocade",
    "sgos": "Symantec",
    "siklu": "Siklu",
    "siteboss": "SiteBoss",
    "siteboss550": "SiteBoss",
    "smos": "Microchip",
    "smartax": "Huawei",
    "smartaxmdu": "Huawei",
    "socomecups": "Socomec",
    "sonicwall": "SonicWall",
    "speedtouch": "Thomson",
    "stellar": "Stellar",
    "supermicrobmc": "Supermicro",
    "svos": "Supermicro",
    "symbol": "Symbol",
    "tachyon": "Tachyon Networks",
    "taitinfra93": "Tait",
    "teldat": "Teldat",
    "terra": "Terra",
    "threecom": "3Com",
    "timos": "Nokia",
    "topvision": "TopVision",
    "ucos": "UC-OS",
    "unifi": "Ubiquiti",
    "valere": "Valere",
    "viptela": "Cisco",
    "vmwareesxi": "VMware",
    "vrp": "Huawei",
    "windows": "Microsoft",
    "xerox": "Xerox",
    "xirrusaos": "Xirrus",
    "xos": "Extreme Networks",
    "zebra": "Zebra",
    "zxdsl": "ZTE",
    "zynos": "Zyxel",
    "zywall": "Zyxel",
    "zyxelnwa": "Zyxel",
    "zyxelwlc": "Zyxel",
}

manufacturer_os_map = {
    # Other Types
    "Proxmox": ["proxmox"],
    "Generic": ["generic", "ping"],
    # Types imported from LibreNMS/OS php files
    "4RF": ["aprisa"],
    "3Com": ["threecom"],
    "Accedian OS": ["aen"],
    "Advantech": ["icros"],
    "Alcatel-Lucent": ["aos"],
    "Alcoma": ["alcoma_almp"],
    "Allied Telesis": ["allied", "awplus"],
    "Allworx": ["allworxvoip"],
    "APC": ["apc", "poweralert"],
    "Apple": ["airport"],
    "Aruba Networks": ["arbos", "arubainstant", "arubaos", "arubaoscx"],
    "Areca": ["areca"],
    "Arris": ["arrisc4", "arriscm", "arrisdsr4410md"],
    "BAT": ["bats"],
    "Baicells": ["baicellsod04"],
    "Barracuda": ["barracudangfirewall"],
    "BeagleBoard": ["beagleboard"],
    "Beijer Electronics": ["boss"],
    "Brother": ["brother"],
    "Brocade": ["fabos", "ironware", "serveriron"],
    "BSD": ["nsbsd", "openbsd"],
    "Cambium Networks": [
        "epmp",
        "pmp",
        "ptp250",
        "ptp500",
        "ptp600",
        "ptp650",
        "ptp670",
        "ptp800",
    ],
    "Calix": ["axos"],
    "Ceragon": ["ceraos"],
    "Check Point": ["gaia", "secureplatform"],
    "Ciena": ["cienarls", "cienasds"],
    "Citrix": ["netscaler", "nitro"],
    "Cisco": [
        "asa",
        "asyncos",
        "ciscosb",
        "ciscowlc",
        "fortigate",
        "ios",
        "iosxe",
        "iosxr",
        "viptela",
    ],
    "Cyberpower": ["cyberpower"],
    "D-Link": ["dlink", "dlinkap"],
    "Dantherm": ["danthermos"],
    "DD-WRT": ["ddwrt"],
    "Dell": ["delllaser"],
    "Dell EMC": ["dnos", "powerconnect", "ftos"],
    "Dragonwave": ["horizoncompact", "horizoncompactplus", "horizonduo"],
    "Eltex": ["eltexmes23xx", "eltexmes24xx"],
    "EnGenius": ["engenius"],
    "Enterasys": ["enterasys"],
    "Ericsson": ["ericsson6600", "ericssonml", "ericssontn"],
    "Ekinops": ["ekinops"],
    "Eurostor": ["eurostor"],
    "Extreme Networks": ["extremeware", "ewc", "xos"],
    "Exa Networks": ["exa"],
    "FS": ["fscentec", "fsgbn", "fsswitch"],
    "F5 Networks": ["f5"],
    "Fortinet": [
        "fortiadc",
        "fortiap",
        "fortiextender",
        "fortigate",
        "fortios",
        "fortiwlc",
    ],
    "Ge": ["gepulsar"],
    "Harmony": ["harmonyenhanced"],
    "Helios": ["helios"],
    "Himoinsa": ["himoinstags"],
    "HPE": ["comware", "procurve"],
    "Huawei": ["smartax", "smartaxmdu", "vrp"],
    "IBM": ["aix"],
    "Infinera": ["infineragroove"],
    "Infinity": ["infinity"],
    "Juniper": ["junos", "junose", "screenos"],
    "Lancom": ["lcos", "lcoslx", "lcossx"],
    "Linux": ["linux"],
    "Mikrotik": ["routeros"],
    "Mimosa Networks": ["mimosa"],
    "Microsoft": ["windows"],
    "MRV": ["mrvod"],
    "NetSure": ["netsure"],
    "Nokia": ["timos"],
    "OpenWrt": ["openwrt"],
    "PacketLight": ["packetlight"],
    "Palo Alto": ["panos"],
    "Peplink": ["pepwave"],
    "PfSense": ["pfsense"],
    "PulseSecure": ["pulse"],
    "QNAP": ["qnap"],
    "Quanta": ["quanta"],
    "QuantaStor": ["quantastor"],
    "Racom": ["ray", "ray3"],
    "Radlan": ["radlan"],
    "Radwin": ["radwin"],
    "Ruckus": [
        "ruckuswireless",
        "ruckuswirelesshotzone",
        "ruckuswirelesssz",
        "ruckuswirelessunleashed",
    ],
    "Saf Tehnika": [
        "saf",
        "safcfm",
        "safintegrab",
        "safintegrae",
        "safintegraw",
        "safintegrax",
    ],
    "Samsung": ["ipolis"],
    "Schleifenbauer": ["schleifenbauer"],
    "Siemens": ["scalance"],
    "SiteBoss": ["siteboss", "siteboss550"],
    "Supermicro": ["supermicrobmc", "svos"],
    "Symbol": ["symbol"],
    "Tachyon Networks": ["tachyon"],
    "Teltonika": ["rutos2xx", "rutosrutx"],
    "Terra": ["terra"],
    "Thomson": ["speedtouch"],
    "Ubiquiti": [
        "airos",
        "airosaf",
        "airosaf60",
        "airosafltu",
        "edgeos",
        "edgeosolt",
        "edgeswitch",
        "unifi",
    ],
    "VMware": ["vmwareesxi"],
    "Xirrus": ["xirrusaos"],
    "Xerox": ["xerox"],
    "Zebra": ["zebra"],
    "ZTE": ["zxdsl"],
    "Zyxel": ["zynos", "zywall", "zyxelnwa", "zyxelwlc"],
}
