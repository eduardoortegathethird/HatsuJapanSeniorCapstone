cd /home/pi/MyCopter
rm mavinit.scr
touch mavinit.scr
python mavinitEditor.py --guideX 0 --guideY 0 --guideZ 1


cd /home/pi
mavproxy.py --master=/dev/serial0  --baudrate 921600 --aircraft MyCopter
