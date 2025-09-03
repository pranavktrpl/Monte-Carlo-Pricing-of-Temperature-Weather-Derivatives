import xarray as xr
from datetime import datetime
import pandas as pd
import numpy as np

# dataset = xr.open_dataset("cvl_data/54.nc")
# Print the list of attributes for each data variable
# for var_name, variable in dataset.data_vars.items():
#     print(f"Attributes for {var_name}: {variable.attrs}")


# Check the time variable and print the range of dates
# if 'date' in dataset:
#     time_var = dataset['date']
#     start_date = time_var.min().values
#     end_date = time_var.max().values
#     print(f"Data is available from {start_date} to {end_date}.") ==> 1981 to 2020
#     print(f"Number of datapoints in between these dates is {len(time_var)}")

#     days_between = (end_date - start_date).astype('timedelta64[D]').item()  # Calculate days
#     print(f"Number of days between the dates: {days_between}")  # Print the result
# else:
#     print("No date variable found in the dataset.")

def extractTemperature(stationFile):
    dataset = xr.open_dataset(stationFile)
    # Extract maxTemp and minTemp
    maxTemp = np.array(dataset['maxTemp'])
    minTemp = np.array(dataset['minTemp'])
    avgTemp = (maxTemp+minTemp)/2

    # Create a dataframe with maxT, minT and the date
    Temperatures = pd.DataFrame({'date': dataset['date'], 'Tmax': maxTemp, 'Tmin': minTemp, 'T': avgTemp})
    return Temperatures

def extractPrecipitation(stationFile):
    dataset = xr.open_dataset(stationFile)
    # Extract maxTemp and minTemp
    Merra = np.array(dataset['prcpMerra'])
    Chirps = np.array(dataset['prcpChirps'])
    imd = np.array(dataset['prcpImd'])
    avgppt = (Merra+Chirps+imd)/3

    # Create a dataframe with maxT, minT and the date
    Precipitations = pd.DataFrame({'date': dataset['date'], 'PrcpMerra': Merra, 'prcpChirps': Chirps, 'prcpIMD': imd, 'Precipitation': avgppt})
    return Precipitations

def extractPrecipitation(stationFile):
    dataset = xr.open_dataset(stationFile)
    # Extract maxTemp and minTemp
    Merra = np.array(dataset['prcpMerra'])
    Chirps = np.array(dataset['prcpChirps'])
    imd = np.array(dataset['prcpImd'])
    avgppt = (Merra+Chirps+imd)/3

    # Create a dataframe with maxT, minT and the date
    Precipitations = pd.DataFrame({'date': dataset['date'], 'PrcpMerra': Merra, 'prcpChirps': Chirps, 'prcpIMD': imd, 'Precipitation': avgppt})
    return Precipitations

def extractHumidity(stationFile):
    dataset = xr.open_dataset(stationFile)
    # Extract maxTemp and minTemp
    hum = np.array(dataset['relHum'])
    
    # Create a dataframe with maxT, minT and the date
    Humidity = pd.DataFrame({'date': dataset['date'], 'Relative Humidity': hum})
    return Humidity

def extractPressure(stationFile):
    dataset = xr.open_dataset(stationFile)
    # Extract maxTemp and minTemp
    pres = np.array(dataset['pres'])
    
    # Create a dataframe with maxT, minT and the date
    Precipitations = pd.DataFrame({'date': dataset['date'], 'Pressure': pres})
    return Precipitations
