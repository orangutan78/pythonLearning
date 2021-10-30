from PIL import Image
file_name=['orangutan\\AI\\camera1','orangutan\\AI\\camera2']
turn=0
for i in range(2):
    f=Image.open(file_name[turn]+'.png')
    f.save(file_name[turn]+'.ppm')
    turn+=1