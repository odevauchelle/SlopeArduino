import serial
from pylab import *
import json

import sys

sys.path.append('/home/olivier/git/LeastSquareCalib/')
import LeastSquareCalib as LSC


#######################
#
# Parameters
#
#######################

local_path = '/'.join( __file__.split('/')[:-1] ) + '/'

identity = LSC.CalibSeries().from_dict( [ dict( expression = 'x**i', coeffs = [0,1] ) ] , safe = True )

calibration_file = 'calibration_angle.json'

#######################
#
# load calibration
#
#######################

try :
    
    with open( local_path + calibration_file ) as the_file :
        
        p = json.load( the_file )
              
        calibration = LSC.CalibSeries().from_dict( p['calibration'], safe = True )
        
    print('Using ' + local_path + calibration_file + ' for calibration.' )
    
except :
    
    calibration = identity
    
    print('No angle calibration!')

########################
#
# Functions
#
#########################

def connect_to_arduino( nb_try = 3 ) :

    for i in range(nb_try) :
        
        try :
            port = '/dev/ttyACM' + str(i)
            
            arduino = serial.Serial( port = port )
            
            arduino.read_all()
            
            print( 'Connected to ' + port )
            
            return arduino
            
        except :
            pass


def arduino_to_degrees( measurement, nbMeasurement, calibration = calibration ) :

    if calibration is None :
        calibration = identity

    angle = int( measurement )/int( nbMeasurement ) # 0 -- 1023

    return calibration.evaluate( angle )


def measure_angle( arduino, calibration = calibration ) :

    measurement, nbMeasurement = arduino.readline().decode().split(',')
    
    return arduino_to_degrees( measurement, nbMeasurement, calibration = calibration )    



if __name__ == '__main__' :

    arduino = connect_to_arduino()

    while True :
        print( measure_angle(arduino) )
         
