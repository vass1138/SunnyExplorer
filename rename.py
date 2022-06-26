# Rename raw data files as Coachmans-

# .env\scripts\activate.bat
# python rename.py data\daily\*
# python rename.py data\monthly\*

import glob
import os
import sys

def rename_files(mypath):

    for f in glob.glob(mypath):

        name = os.path.basename(f)
        path = os.path.dirname(f)

        if not name.startswith('Coachmans-'):

            x  = name.split('-')

            newname = path + '/' + 'Coachmans-' + x[1]
            os.rename(f,newname)
            print(newname)
    
    return

def main():

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <path>")
    
    rename_files(arg)

if __name__ == '__main__':
    main()