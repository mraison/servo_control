import RPi.GPIO as GPIO
import time
import numpy


class ServoClient(object):
#These are the config steps

	def __init__(self, servoconfig, startingAnge):
		self._servoconfig = servoconfig
		# use P1 header pin numbering convention
		GPIO.setmode(GPIO.BOARD)
		# Set up the GPIO channels - one input and one output
		GPIO.setup(self._servoconfig["pin"], GPIO.OUT)

		# Hz = 50, pin = 11
		self._servo = GPIO.PWM(self._servoconfig["pin"], self._servoconfig["Hz"])
		self._servo.start(0) # @todo replace init value to...some correct value...
		self._startingAnge = startingAnge
		
		# configure servo system constants
		self._max_duty_cycle = 22
		self._min_duty_cycle = 2
		self._neutral_position_duty_cycle = 0
		self._startingDutyCycle = 0
		startingDutyCycle = self._convertDegreesToServo(startingAnge)
		
		# self._convertDegreesToServo(self._startingAnge)
		self._servo.ChangeDutyCycle(
			startingDutyCycle
		)
		# self.setDutyCycle(startingDutyCycle)
		#self.moveToAngle(self._startingAnge)
		
	# def setDutyCycle(self, newDutyCycle=0, stepSize=0):
	# 	if newDutyCycle > self._max_duty_cycle or newDutyCycle < self._min_duty_cycle:
	# 		return 1
	#
	# 	if newDutyCycle == self._startingDutyCycle:
	# 		return 0
	#
	# 	current_duty_cycle = self._startingDutyCycle
	# 	self._startingDutyCycle = newDutyCycle
	#
	# 	# while current_duty_cycle < newDutyCycle:
	# 	max_r = max(current_duty_cycle, newDutyCycle)
	# 	min_r = min(current_duty_cycle, newDutyCycle)
	# 	do_flip = current_duty_cycle > newDutyCycle
	# 	r = numpy.arange(min_r, max_r, stepSize)
	# 	if do_flip:
	# 		r = numpy.flip(r)
	#
	# 	for i in r:
	# 		self._servo.ChangeDutyCycle(
	# 			i
	# 		)
	# 		time.sleep(0.5)
	#
	# 	self._servo.ChangeDutyCycle(0)

	## return 0 if everything is fine. if it's anything else...it's an error.
	# def moveToAngle(self, degrees):
	# 	if degrees > 180 or degrees < 0:
	# 		return 1
	#
	# 	if degrees == self._startingAnge:
	# 		return 0
	#
	# 	self._startingAnge = degrees
	# 	#range for servo is from 2 to 12. 7 is 90, 12 is 180, 2 is 0.
	# 	# normalization is servo num = degrees/18 + 2
	# 	# This is the angle writes.
	# 	self._servo.ChangeDutyCycle(
	# 		self._convertDegreesToServo(degrees)
	# 	)
	# 	time.sleep(0.5)
	# 	self._servo.ChangeDutyCycle(0)
	# 	time.sleep(0.5)

	def _convertDegreesToServo(self, degrees):
		return int(round(((degrees / 18) + 2)))
		
	def _convertServoToDegrees(self, dutyCycle):
		return int(round((dutyCycle - 2) * 18))

	def close(self):
		# This is the tear down...
		self._servo.stop()
		GPIO.cleanup()


#servoConfig = {
#	"pin":11, # 11
#	"Hz": 50
#}

#servo = ServoClient(servoConfig, 0) # btw there's a bug here with how the initializer is working

#servo.moveToAngle(0)
#servo.moveToAngle(90)
#servo.moveToAngle(180)
#servo.moveToAngle(0)

#servo.close()
#servo._servo.ChangeDutyCycle(2)
#time.sleep(0.5)
#current_duty_cycle = 2.0
#max_duty_cycle = 8.0
#step = 0.1
#servo.setDutyCycle(max_duty_cycle, step)
#servo.setDutyCycle(2, step)

#time.sleep(0.5)
#servo.close()
