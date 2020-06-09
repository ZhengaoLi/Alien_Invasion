import pygame
import urllib2

pygame.mixer.init(frequency=8000, size=-16, channels=4)
URL = (
    "http://api.microsofttranslator.com/V2/Http.svc/Speak?language=zh-chs&appid=Tz49xk_OIwzAAeH91ExsdbHBruQdwsi5C2ssKhwhttRerOg__1cm_J-fxFJXAIME2&text=%e4%b8%ba%e4%bb%80%e4%b9%88%e8%bf%99%e6%a0%b7%e5%ad%90%ef%bc%8c%e4%bd%a0%e5%a5%bd%e5%a5%bd&format=audio/wav&options=MaxQuality")
response = urllib2.urlopen(URL)
waveFile = response.read()
pygame.mixer.Sound(waveFile).play()
while pygame.mixer.get_busy():
    print('playing...')