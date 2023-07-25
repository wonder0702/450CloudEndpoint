import pyvisa
import time

# Replace 'USB0::0x2A8D::0x1002::MY59001794::0::INSTR' with the actual USB connection address of your E36311A
visa_address = 'USB0::0x2A8D::0x1002::MY59001794::0::INSTR'
# visa_address = 'USB0::0x2A8D::0x1002::MY59001794::INSTR'

import pyvisa
import time
from time import sleep
import os


rm = pyvisa.ResourceManager()
print("Resources detected\n{}\n".format(rm.list_resources()))

#vm = rm.open_resource("USB0::0x2A8D::0x1202::MY61004198::0::INSTR")
vm = rm.open_resource(visa_address)

# Run the test code from the web

vm.write(':FUNCtion:VOLTage:DC')
vm.write(':OUTP CH2,OFF')   # start OFF - safe :)
vm.write(':APPL CH2,0,0.2') # apply 0V, 0.2A

vm.write("OUTP ON")
v = 0
i = 0
while v <= 6.0: # sweep voltage up to 10V
    vm.write(':APPL CH2,' + str(v) + ',0.2')            # Set the voltage
    sleep(0.5)
    vMeasured = float(vm.query(':MEASure:VOLTage:DC?'))  # measure the voltage
    iMeasured = float(vm.query(':MEASure:Current:DC?'))  # measure the current them cai nay
     #vMeasured = float(dmm.query(':MEASure:VOLTage:DC?'))  # measure the voltage

    # Write results to console
    print("{}  {}".format(v, vMeasured))
    print("{}  {}".format(i, iMeasured))
    v += 0.5


# Test complete. Turn supply off and zero the setpoints
sleep(10)
vm.write("OUTP OFF")
vm.write('VOLT 0.0')
vm.write('CURR 0.0')

