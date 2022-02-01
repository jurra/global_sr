#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:07:43 2021

@author: vanoorschot
"""

#%% 
import numpy as np
import pandas as pd
import glob

#%% concat separate files 
fol = '/home/vanoorschot/Documents/treecover_gsim_shapes/'

# tree cover
li=[]
tc_files = glob.glob(f'{fol}Tree_cover_*.csv')
for filename in tc_files:
    df = pd.read_csv(filename,index_col=1)
    df = df.drop(columns={'system:index','.geo'})
    if 'Id' in df.columns:
        df = df.drop(columns={'Id'})
    df.index = df.index.rename('catch_id')
    df = df.rename(columns={'mean':'mean_tc','min':'min_tc','max':'max_tc','stdDev':'std_tc'})
    li.append(df)
tc = pd.concat(li,axis=0)

# non tree cover
li=[]
tc_files = glob.glob(f'{fol}Nontree_cover_*.csv')
for filename in tc_files:
    df = pd.read_csv(filename,index_col=1)
    df = df.drop(columns={'system:index','.geo'})
    if 'Id' in df.columns:
        df = df.drop(columns={'Id'})
    df.index = df.index.rename('catch_id')
    df = df.rename(columns={'mean':'mean_ntc','min':'min_ntc','max':'max_ntc','stdDev':'std_ntc'})
    li.append(df)
ntc = pd.concat(li,axis=0)

# concat tree and nontree cover
c = pd.concat([tc,ntc],axis=1)
c['mean_nonveg'] = 100-c.mean_tc-c.mean_ntc
c.to_csv(f'{fol}gsim_shapes_treecover.csv')

