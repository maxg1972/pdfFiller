"""
    pdfFiller - PDF form auto filler
    =================================
    Utilities to auto fill pdf forms

    Requires
    -----
    fdfgen modules and pdftk os tool

    Usage
    -----
    Import the pdfFiller.py file into your project and use fill_pdf function

    Authors & Contributors
    ----------------------
        * Massimo Guidi <maxg1972@gmail.com>,

    License
    -------
    This module is free software, released under the terms of the Python
    Software Foundation License version 2, which can be found here:

        http://www.python.org/psf/license/

"""

__author__ = "Massimo Guidi"
__author_email__ = "maxg1972@gmail.com"
__version__ = '1.0'

import os
from fdfgen import forge_fdf

def fill_pdf(data_obj,input_file,output_file):
    """
    Create a filled form pdf file
    @param data_obj: list of dictionary with pdf params and values
    @param input_file: pdf form file name (with path and extension)
    @param output_file: output file name (with path and extension)
    @return: result dictionary: {'code' : <code_value>, 'message' : <msg_value>}
             (<code_value>: 0 -> execution succesful, <> 0 execution error), <msg_value> contains error description if <code_value> is not 0)
    """
    #returning objects
    result = {'code' : 0,  'message': ''}

    #temporrary fdf file name
    temp_name = os.path.splitext(os.path.basename(input_file))[0]
    temp_path = os.path.dirname(os.path.abspath(input_file))
    temp_fdf = "%s/%s" % (temp_path,temp_name)

    #get fileds and values
    fdf = forge_fdf("",data_obj,[],[],[])

    #make temporary file settings fileds with values
    try:
        fdf_file = open(temp_fdf,"w")
        fdf_file.write(fdf)
        fdf_file.close()
    except IOError, (errno, strerror):
        result['code'] = -1
        result['message'] = "Can't write temporary file! I/O error (%s): %s" % (errno, strerror)
    else:
        #exec pdftk and create output pdf file
        try:
            cmd = 'pdftk %s fill_form %s output %s flatten' % (input_file,temp_fdf,output_file)
            os.system(cmd)
        #except OSError as e:
        except OSError, (errno, strerror):
            result['code'] = -1
            result['message'] = "Can't create output file! OS error (%s): %s" % (errno, strerror)

    return result
