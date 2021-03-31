

import os

def ensureFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
        
        
ensureFolder('./create_folder_tut/inner/')



"""
import os
os.makedirs(directory, exist_ok = True)
? (thanks @EricHedengren for correction below! ;)

exist ok = True checks for existence and makes dir created if not existing

"""