'''
Lists of PIL Supported Image Filetypes

This module lists the image filetypes PIL supports as of v6.2.1.
Each filetype is on its own line.
'''

def rw_types():
    '''
    Returns a list of all types that have READ/WRITE support.
    :return: (list) rw_types
    '''
    rw_types = [
        '.bmp',
        '.dib',
        '.eps',
        '.gif',
        '.icns',
        '.ico',
        '.im',
        '.j2p',
        '.j2x',
        '.jpeg',
        '.jpg',
        '.msp',
        '.pcx',
        '.pdf',
        '.png',
        '.ppm',
        '.sgi',
        '.spi',
        '.tga',
        '.tiff',
        '.webp',
        '.xbm'
    ]
    return rw_types


def r_types():
    '''
    Returns a list of all types that have READ-ONLY support.
    :return: (list) r_types
    '''
    r_types = [
    '.blp',
    '.cur',
    '.dcx',
    '.dds',
    '.flc',
    '.fli',
    '.fpx',
    '.ftex',
    '.gbr',
    '.gd',
    '.gd',
    '.imt',
    '.iptc',
    '.mcidas',
    '.mic',
    '.mpo',
    '.pcd',
    '.pixar',
    '.psd',
    '.wal',
    '.xpm',
]
    return r_types


def w_types():
    '''
    Returns a list of all types that have WRITE-ONLY support.
    :return: (list) w_types
    '''
    w_types = [
       '.palm',
       '.pdf'
    ]
    return w_types


def i_types():
    '''
    Returns a list of all types that have IDENTIFY-ONLY support.
    :return: (list) i_types
    '''
    i_types = [
        '.bufr',
        '.fits',
        '.mpeg',
        '.wmf',
    ]
    return i_types
