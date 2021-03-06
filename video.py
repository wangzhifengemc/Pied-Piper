import picamera
import os


with picamera.PiCamera() as camera:
    camera.resolution=(640,480)
    camera.start_preview()
    camera.start_recording('foo.h264')
    camera.wait_recording(10)
    camera.stop_recording()
    camera.stop_preview()
    camera.close()

#将H.264文档转换为MP4
os.system("sudo MP4Box -add foo.h264 foo.mp4 0>null 1>null 2>null")