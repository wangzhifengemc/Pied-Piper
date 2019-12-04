#coding=utf8
import time
import picamera
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    try:
        camera.start_preview()
#        camera.exposure_compensation = 2
#        camera.exposure_mode = 'spotlight'
#        camera.meter_mode = 'matrix'
#        camera.image_effect = 'gpen'
        # 初始化预热摄像头
        time.sleep(2)
        camera.capture('foo.jpg')
        camera.stop_preview()
        print "ok"
    finally:
        print "ok1"
        camera.close()
