#!/usr/bin/python3
from sensors import BME680
# uses python3 and sensors module to the temprature humidity pressure
bme680 = BME680()
print("Temperature: %0.1f C" % bme680.getTemperature())
print("Gas: %d ohm" % bme680.getGas())
print("Humidity: %0.1f %%" % bme680.getHumidity())
print("Pressure: %0.3f hPa" % bme680.getPressure())

print("----- Atmospheric sensors test complete -----")
