import os
import shutil

PROJECT_DIR=os.path.dirname(os.path.abspath(__file__))
try:
    shutil.rmtree(PROJECT_DIR+'\\blocks')
except FileNotFoundError:
    pass
try:
    os.remove(PROJECT_DIR+'\\result.txt')
except FileNotFoundError:   
    pass

f=open(PROJECT_DIR+'\\setting.txt','w')
f.write("mapName=\n")
f.write("blockLength=\n")
f.write("blockWidth=\n")
f.write("threshold=50\n")
f.write("interval=\",\"\n")
f.close()

os.mkdir(PROJECT_DIR+'\\blocks')