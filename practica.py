import argparse


def process_input(str):
   "This take input and transform"
   print(str)
   return



parser = argparse.ArgumentParser(description='Create html table with selected parameters')
parser.add_argument("--key", type=str, required=True, help = "Indica les claus")
parser.add_argument("--date", type=str, help = "Indica un rang de datas")
parser.add_argument("--metro", type=str, help = "Indica lineas de metro")

args = parser.parse_args()    
process_input(args.key)
