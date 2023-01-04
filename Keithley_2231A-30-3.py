import pyvisa

rm = pyvisa.ResourceManager()
Source_meter = rm.open_resource('ASRL5::INSTR') #USB address
print(rm.list_opened_resources()) #For checking the address
print(Source_meter.query("*IDN?")) #For checking the response
