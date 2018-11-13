#!/usr/bin/env python3
'''
prepare data
'''
import os
import pandas as pd
import netCDF4 as ntc
import xarray as xr
from sys import platform

if platform == "linux" or platform == "linux2":
    sys_f = "/homes/jackcao/"
else:
    sys_f = "/Volumes/jackcao/"

file_path = os.path.join(sys_f,"forecasting/sample/20181026_no_cap_to2100_spline/diabetes_male.nc")

# read in netCDF data
deaths_data = xr.open_dataset(file_path)

# convert to pandas dataframe
df = deaths_data.to_dataframe()
