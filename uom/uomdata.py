"""UOM DataFrame."""
from pandas import read_csv
from pkg_resources import resource_filename

DF_UOM = read_csv(resource_filename('uom', 'uom.csv'), index_col=0)
