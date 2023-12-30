import sys, socket, random
from threading import Thread
from PIL import Image
from multiprocessing import Process

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
sock.connect((sys.argv[1], int(sys.argv[2])))

#sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock2.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
#sock2.connect((sys.argv[1], int(sys.argv[2])))

pixel_str = ""

def pixel(x,y,r,g,b,a=255):
  if a == 255:
    return str('PX %d %d %02x%02x%02x\n' % (x,y,r,g,b))
  else:
    return str('PX %d %d %02x%02x%02x%02x\n' % (x,y,r,g,b,a))


im = Image.open(sys.argv[3]).convert('RGBA')
_,_,w,h = im.getbbox()
for i in range(200):
    pos1 = random.randint(0, 1920-w)
    pos2 = random.randint(0, 1080-h)
    for x in range(w):
      for y in range(h):
         r,g,b,a = im.getpixel((x,y))
         pixel_str += pixel(x+pos1,y+pos2,r,g,b,a)

p = pixel_str.encode()

print("Start")
while True:
    t = Thread(target=sock.send, args=[p])
    t.run()
    #t2 = Thread(target=sock2.send, args=[p])
    #t2.run()
