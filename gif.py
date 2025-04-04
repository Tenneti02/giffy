import imageio.v3 as iio

fn=['t1.png','t2.png']
img=[]
for f in fn:
    img.append(iio.imread(f))
iio.imwrite('t.gif', img, duration = 500, loop = 0)    
