# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km ...
# Text explaining script usage
# Parameters:
#  lat_deg: geodetic latitude in degrees
#  lon_deg: longitude in degrees
#  hae_km: height above ellipsoid in km
#  ...
# Output (Prints the following):
#  r_x_km: ECEF x-component in km 
#  r_y_km: ECEF y-component in km 
#  r_z_km: ECEF z-component in km 
# 
# Written by Mandar Ajgaonkar
# Other contributors: None
#
# See the LICENSE file for the license  

# import Python modules
import math  # math module
import sys   # argv

# "constants"
R_E_KM = 6378.1363 # radius of Earth in km
E_E = 0.081819221456 # unitless

# helper functions

# function description

## calculate denominator 
def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0 - (ecc**2.0) * (math.sin(lat_rad))**2)

# initialize script arguments
lat_deg = float('nan')  # geodetic latitude (deg)
lon_deg = float('nan')  # longitude (deg)
hae_km = float('nan')  # height above ellipsoid (km)

# parse script arguments 
if len(sys.argv) == 4:
    try:
        lat_deg = float(sys.argv[1])
        long_deg = float(sys.argv[2])
        hae_km = float(sys.argv[3])
    except ValueError:
        print("Error: lat_deg, long_deg and hae_km must be numeric.")
        exit()
else:
    print('Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km')
    exit()

# convert longitude and latitude to degrees
lat_rad = lat_deg * math.pi / 180.0
long_rad = long_deg * math.pi / 180.0

# perform calculations to get components of r in ECEF reference frame
denominator = calc_denom(E_E, lat_rad)
c_E = R_E_KM / denominator
s_E = R_E_KM * (1.0 - E_E * E_E) / denominator
r_x_km = (c_E + hae_km) * math.cos(lat_rad) * math.cos(long_rad)
r_y_km = (c_E + hae_km) * math.cos(lat_rad) * math.sin(long_rad)
r_z_km = (s_E + hae_km) * math.sin(lat_rad)

# output results
print(r_x_km)
print(r_y_km)
print(r_z_km)
