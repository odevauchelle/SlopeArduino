from pylab import *
import json

import sys

sys.path.append('/home/olivier/git/LeastSquareCalib/')
import LeastSquareCalib as LSC

################
#
# collect data
#
################

p = dict(
    data_file = 'calibration_angle.csv',
    calibration_file = 'calibration_angle.json',
    rotation_radius = 165 # mm
    )

x, arduino_tension = loadtxt( p['data_file'], delimiter = ',').T

index = argsort(arduino_tension)
x = x[index]
arduino_tension = arduino_tension[index]

angle = arctan( x/p['rotation_radius'] ) # radians
angle *= 180/pi # degrees

################
#
# fit data
#
################

calib = LSC.CalibSeries().from_dict([
    dict( expression = 'x**i', coeffs = [0]*2 ),
    #dict( expression = 'np.sin(2*np.pi*(i-1)*x)', coeffs = [0]*8 )
    ], safe = True )

calib.fit_to_data( arduino_tension, angle )

################
#
# plot_data
#
################

arduino_tension_fit = linspace( min(arduino_tension), max(arduino_tension), 300 )

plot( arduino_tension, angle, 'o')

xlabel('Arduino tension')
ylabel('Angle [deg]')

plot( arduino_tension_fit, calib.evaluate( arduino_tension_fit ), '--' )

figure()
plot( arduino_tension, angle - calib.evaluate( arduino_tension ), 'o-m' )
xlabel('Arduino tension')
ylabel('Error Angle [deg]')

# ~ ###############
# ~ #
# ~ # save fit
# ~ #
# ~ ###############

p['calibration'] = calib.to_dict()

with open( p['calibration_file'], 'w' ) as the_file :
	json.dump( p, the_file ) 



show()
