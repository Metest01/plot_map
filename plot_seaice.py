# -*- coding: utf-8 -*-
import netCDF4 as nc
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

m = Basemap(projection='npstere',round = True, boundinglat=62,lon_0=360,resolution='l')
data = nc.Dataset('G:/My Drive/PhD/arctic/ERA5/ice/ice_era5_201808.nc')
lons, lats = np.meshgrid(data.variables['longitude'][:], data.variables['latitude'][:]) ; x, y = m(lons, lats)
fig = plt.figure(figsize=(15,7)); m.drawcoastlines() ; m.fillcontinents(color='gray',lake_color='gray')
timestep=20 ; m.pcolor(x,y,data.variables['siconc'][timestep][:]*100,vmin=0,vmax=100,cmap=plt.cm.get_cmap('Blues_r')) #choose time step
clb = plt.colorbar(orientation='horizontal',shrink=0.45,aspect=20,pad=0.05) ; clb.ax.set_title('Sea ice concentration (%)')
