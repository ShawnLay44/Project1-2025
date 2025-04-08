from gpiozero import LED
led = LED(4)
led.on()
sleep(5)
led.off()
