import datetime
from gpiozero import MotionSensor

pir = MotionSensor(21)

while True:
        pir.wait_for_motion()
        print(f'{datetime.datetime.now()} - Motion Detected')
        pir.wait_for_no_motion()
