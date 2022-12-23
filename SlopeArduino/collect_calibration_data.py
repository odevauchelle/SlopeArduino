from SlopeArduino import *
from pylab import nanmean

nb_measurements = 10

arduino = connect_to_arduino()

data_file = 'calibration_angle.csv'

# ~ with open( data_file, 'w' ) as the_file :
	# ~ the_file.write( '# x [mm], raw arduino output\n' )


while True :
	
	angle = input('x? ')
	
	arduino_angles = []
	
	arduino.read_all()
	
	for _ in range( nb_measurements ) :
	
		arduino_angles += [ measure_angle( arduino, calibration = None  ) ]
	
	arduino_angle = nanmean( arduino_angles )
	
	data_line = str( angle ) + ', ' + str( arduino_angle ) + '\n'
	
	with open( data_file, 'a' ) as the_file :
		the_file.write( data_line )
		
	print(data_line)
