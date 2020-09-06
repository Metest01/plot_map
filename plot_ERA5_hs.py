import netCDF4 as nc
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
m = Basemap(projection='cyl', llcrnrlat=-90, urcrnrlat=90,llcrnrlon=0, urcrnrlon=360, resolution='l') #choose projection of the map - cyl = Equidistant Cylindrical 
data = nc.Dataset('./hs_era5_20160901.nc') #select netcdf file
lons, lats = np.meshgrid(data.variables['longitude'][:], data.variables['latitude'][:]) ; x, y = m(lons, lats) #transform latlon variables to chosen projection
fig = plt.figure(figsize=(16,12)); m.drawcoastlines() ; m.fillcontinents(color='gray',lake_color='gray')
timestep=2 ;  m.pcolor(x,y,data.variables['swh'][timestep][:],vmin=0,vmax=8,cmap=plt.cm.get_cmap('jet')) #choose timestep and select variable (swh is significant wave height)
clb = plt.colorbar(orientation='horizontal',shrink=0.45,aspect=20,pad=0.05) ; clb.ax.set_title('Hs (m)') #plot colorbar and write title
