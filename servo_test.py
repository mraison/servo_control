import RPi.GPIO as GPIO
import time


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
		self.moveToAngle(self._startingAnge)

	# return 0 if everything is fine. if it's anything else...it's an error.
	def moveToAngle(self, degrees):
		if degrees > 180 or degrees < 0:
			return 1
		
		if degrees == self._startingAnge:
			return 0
		
		self._startingAnge = degrees
		#range for servo is from 2 to 12. 7 is 90, 12 is 180, 2 is 0.
		# normalization is servo num = degrees/18 + 2
		# This is the angle writes.
		self._servo.ChangeDutyCycle(
			self._convertDegreesToServo(degrees)
		)
		time.sleep(0.5)
		self._servo.ChangeDutyCycle(0)
		time.sleep(0.5)

	def _convertDegreesToServo(self, degrees):
		return int((degrees / 18) + 2)

	def close(self):
		# This is the tear down...
		self._servo.stop()
		GPIO.cleanup()


servoConfig = {
	"pin":11,
	"Hz": 50
}

servo = ServoClient(servoConfig, 0)

servo.moveToAngle(0)
servo.moveToAngle(90)
servo.moveToAngle(180)
servo.moveToAngle(0)

servo.close()
