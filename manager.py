import pandas as pd
import re
import shutil
import os
from glob import glob

rundir = os.getcwd()

def build(rm=False):
    
    if rm:
        os.chdir('/Volumes/wwwroots/aurii')
        fs = [x for x in os.listdir() if 'photography' not in x]
        for f in fs:
            # print(f'rm -r {f}')
            os.system(f'rm -r {f}')
    
    os.chdir('/Users/bill/Code/aurii')
    os.system('JEKYLL_ENV=production bundler exec jekyll build')
    os.system('cp -r _site/* /Volumes/wwwroots/aurii/')

if __name__ == '__main__':
    build(False)