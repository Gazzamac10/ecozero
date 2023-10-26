import warnings
import pandas as pd
from azure.data.tables import TableServiceClient
import InputR
from Defs import definitions

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#Create Typology Seven

#Headers
Headers = [
    'NbRd',
    'MbRd',
    'Type',
    'CalcValOne',
    'CalcValTwo'
]

#Calcs from Shear Walls Calc