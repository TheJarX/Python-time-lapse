from datetime import datetime as dt
import time
from base64 import b64decode
import os


"""
General variables,
These variables will be used in all documents, consider these as 'constants' that you can change.
"""
CURRENT_MS = int(round(time.time() * 1000))

# DAILY_DIR = os.path.dirname( './img/{}'.format( dt.now().strftime('%d-%m-%Y') ) )
DAILY_DIR = './img/{}'.format( dt.now().strftime('%d-%m-%Y') ) 

BASE_FILENAME = 'GOPRO-{}{}.png'.format( dt.now().strftime('%H%M%S'), \
    CURRENT_MS )



"""
Save the image from a base 64 encoded String

Args:
    b64encoded_str (str): base64 encoded string from the image, usually the result
                    of _util_gopro.get_as_bas64()

Raises:
    ValueError: If an error occurred while the creation of directory for the images,
        or when saving the image

Returns:
    A string with 'Ok' message and aditional data
"""

def save_data(b64encoded_str):

    img = b64decode(b64encoded_str)

    # Create the directory to save images
    if( os.path.exists( DAILY_DIR ) ):
        print('Already exists! dir: %s'%os.getcwd() )
    else:
        try:
            os.mkdir( DAILY_DIR )
        except OSError:
            print('Failed creation of directory! {}'.format(OSError))
        else:
            print('Now exists the directory!')
    # Try to save the image
    try:
        with open(DAILY_DIR + '/' + BASE_FILENAME, 'wb+' ) as f:
            #TODO: ! Ask if there are a file with the same name
                f.write( img )
    except ValueError:
        print('An error has occurred! {}'.format(ValueError))
        exit()


    return 'Ok'


"""
Compare 2 or more files with a md5 hash.
!! Don't use, this function wasn't tested yet.

Args:
    fst_file (str): Route of the first file
    scnd_file (str): Route of the second file

Returns:
    True if both files are the same or if found a similar file; False if not.
"""
def compare_files (fst_file, scnd_file = ''):
    if not scnd_file:
        #Here i'ld iterate with each file in the directory
        pass
    else:
        import hashlib
        digests = []
        for filename in [fst_file, scnd_file]:
            hasher = hashlib.md5()
            with open(filename, 'rb') as f:
                buff = f.read()
                hasher.update(buff)
                hex_value = hasher.hexdigest()
                digests.append(hex_value)
        if digests[0] == digests[1]:
            print('Archivo existente')
            return True
    return False
        
        

