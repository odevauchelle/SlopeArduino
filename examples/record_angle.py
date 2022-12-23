# encoding: utf8

from pylab import *
from datetime import datetime

import sys
sys.path.append('../SlopeArduino/')

import SlopeArduino as SA


arduino = SA.connect_to_arduino( port = '/dev/ttyACM0' )



tag = str( rand() )[2:]
data_file = 'angle_' + tag + '.csv'

with open( data_file, 'w' ) as the_file :
    
    the_file.write( '# fit coefficients: ' + str(  SA.calibration.to_dict() ) + '\n' )
    the_file.write( '# time, angle [deg]\n' )


while True :
    
    angle = SA.measure_angle( arduino )
    time = datetime.now()
    
    data_line = time.isoformat() + ', ' + str( angle ) + '\n'
    
    with open( data_file, 'a' ) as the_file :
        the_file.write( data_line )
        
    print( data_line[:-1] )
