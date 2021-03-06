#!/bin/env python 3.6
# -*- encoding: utf-8 -*-
#==============================================================================
# Author:      胡伟锋
# Created:     2018-06-19
# Version:     2.0.0
# E-mail:      674649741@qq.com
# Purpose:     Ploting
#==============================================================================
import mlFunctions as f
import data_information as di
disi=di.SampleInformation()

def main():
    pt=f.MLPloting()
    pt.plot_back_and_all_samples()
    pt.plot_mean_samples()
    pt.plot_PCA(disi.class_num)
    return 0

if __name__=='__main__':
    main()
