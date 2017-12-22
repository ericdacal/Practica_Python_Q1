import xml.etree.ElementTree as ET
import urllib.request
import argparse
from ast import literal_eval

class Event:
    'classe que conté events infantisl amb nom,adreça,dia,hora i edad'
    def __init__(self, name, address, day, hour, age):
        self.name = name
        self.address = address
        self.day = day
        self.hour = hour
        self.age = age

def search(root_esd,elem):
    'Search elem in a uml'
    for actes in root_esd.iter('acte'):
        name = actes.find('nom').text
        address = actes.find('lloc_simple').find('adreca_simple').find('carrer')
        day = actes.find('data').find('data_proper_acte').text
        hour = actes.find('data').find('hora_fi').text
        e = Event(name,address,day,hour,"None")
        #age = age

def getroots():
    'Returns root of a XML tree of the urls'
    html = urllib.request.urlopen("http://w10.bcn.es/APPS/asiasiacache/peticioXmlAsia?id=199")
    xml = ET.parse(html)
    root_esd = xml.getroot()
    html = urllib.request.urlopen("http://opendata-ajuntament.barcelona.cat/resources/bcn/TRANSPORTS%20GEOXML.xml")
    xml = ET.parse(html)
    root_par = xml.getroot()
    return root_esd, root_par


def process_list(l,root_esd, root_par):
    for elem in l:
        if isinstance(elem,str): res = search(root_esd,elem)
        elif isinstance(elem,list): res = process_list(elem,root_esd, root_par)
        else: res = process_list(elem,root_esd, root_par)
        
        return res
        #literal_eval(elem)
        #elem = literal_eval(elem)
        #if isinstance(elem,str): print(elem) #search(root_esd,elem)
        #search(root_esd,elem)
        #if isinstance(inp,list): print("list")
        #elif isinstance(inp,tuple): print("tuple")
        #else: print("st")


def process_input(inp,root_esd,root_par):
    'Funcion para procesar entrada'
    inp = literal_eval(inp)
    if isinstance(inp,list): process_list(inp,root_esd, root_par)
    elif isinstance(inp,tuple): print("tuple")
    else: print("st")








parser = argparse.ArgumentParser(description='Create html table with selected parameters')
parser.add_argument("--key", type=str, required=True, help = "Indica les claus")
parser.add_argument("--date", type=str, help = "Indica un rang de datas")
parser.add_argument("--metro", type=str, help = "Indica lineas de metro")

#Take roots of xmls
root_esd, root_par = getroots()
args = parser.parse_args()    
process_input(args.key,root_esd, root_par)


