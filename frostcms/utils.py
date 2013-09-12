#encoding=utf-8
'''
Created on 2013年9月10日

@author: frost
'''

from logging import getLogger

log = getLogger(__name__)


def md5(str):
    import md5 
    m = md5.new()
    m.update(str) 
    return m.hexdigest() 
