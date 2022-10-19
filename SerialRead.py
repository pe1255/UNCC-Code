import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import asksaveasfile
from tkinter import *
import io
import numpy as np
import yaml
import matplotlib.pyplot as plt

import cv2
import numpy as np
import yaml
import os
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import re
#matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
# =======================================
pause = 0


def yamlConstructor(loader, node):
    mapping = loader.construct_mapping(node, deep=True)

    mat = np.array(mapping["data"])

    if mapping["cols"] > 1:

        mat.resize(mapping["rows"], mapping["cols"])

    else:

        mat.resize(mapping["rows"], )

    return mat


def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""

    #   import io

    buf = io.BytesIO()

    fig.savefig(buf)

    buf.seek(0)

    img = Image.show(buf)

    return img


# logo this is where the graph will be located need to fix

def start_plot():


    #camLocationX = []
    camLocationZ = []
    realTime = []
    camLoc = []

    diameter = 168
    tagHeight = 46.5
    outDiameter = 2*tagHeight + diameter
    radius = 83.5
    tagHeight = 46.5
    calcRatio = 0.6789
    centerCam = [0, 12]


    print("Data Received: ")

    global pause

    while True:
        tvec = []
        #rvec = []
        camLocationY = []
        xOffset = []
        zDistance = []
        xyCoord = []
        arcLengthDis = []
        camArcDis = []
        zTotal = 0
        arcTotal = 0


        data = ser.readline()

        #coordinates = coordinates.strip()
        data = data.decode("utf-8")
        print('data= ', data)
        print('pause= ' , pause)
        file = open('cameraCoord.txt','a')
        file.write(data)
        realTime.append(data)
        # When done is found then take data to parse
        if pause == 1:
            ser.close()
            pause = 0
            break
        if ('None\r\n'  in data) :
            print('no tags seen')
            break
        if 'done\r\n' in data :

            realTime = str(realTime)
            #print('cord1= ', realTime)

            # Finds number/ID of Aruco markers detected
            ids = re.findall(r'\[\s\d\]|\[\d\d\]', realTime)
            #ids.append(id)
            print('ids: ', ids)
            #print('realtime = ', realTime)

            # Extracts only numbers from string
            matchNumber = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')
            realTime = [float(x) for x in re.findall(matchNumber, realTime)]
            realTime = [ele for ele in realTime if ele not in {0.0}]
            #print('realtime = ', realTime)

            # Creates our tvec and rvec
            tvecSize = len(ids) * 3 + len(ids)
            #rvecSize = len(ids) * 3 + tvecSize
            # print('tvecsize = ', tvecSize)
            print('realtime data = ', realTime)
            tvec = []
            #rvec = []
            count = len(ids)
            #print('size of tvec', tvecSize)
            #print('size of realTime', np.size(realTime))
            for i in range(len(ids), tvecSize):
                tvec.append(realTime[i])
            #for i in range(tvecSize, rvecSize):
            #    rvec.append(realTime[i])
            tvec = np.reshape(np.array(tvec), (len(ids), 3))
            #rvec = np.reshape(np.array(rvec), (len(ids), 3))
            # print('tvec = ', tvec[0])
            # print('tvec = ', tvec[0,2])
            print('tvec = ', tvec)
            #print('rvec = ', rvec)

            # Create a (x,z) array and an (x) array
            for i in range(0, len(tvec)):
                xyCoord.append([tvec[i, 0], tvec[i, 1]])
                xOffset.append(tvec[i, 0])
                zDistance.append(tvec[i, 2])
            xyCoord = sorted(xyCoord, key=lambda x: x[0])  # Sort (x,y) coordinates from lowest x to highest
            xyCoord = np.asarray(xyCoord)
            #print('xzCoord: ', xyCoord)
            #print('xoffset: ', xOffset)

            for i in range(len(zDistance)):
                zTotal += zDistance[i]
                # print('zTotal: ', zTotal)
            zTotal = round(zTotal / len(ids), 3)
            camLocationZ.append(zTotal)
            # arrayTvec.append(centerCam)
            # jevois.sendSerial('z Distance average {}'.format(zTotal))
            print('ztotal = ', zTotal)

            # Find tag closest to 0, to find location of camera on x-axis
            xCloseZero = min(xOffset, key=abs)
            closestTag0 = np.where(xyCoord == xCloseZero)
            closestTag0 = np.asarray(closestTag0).flatten()
            closestTag0 = closestTag0[0]  # Array element value for tag on left side of center of camera
            #print('clost tag 0: ', closestTag0)
            originTag = xyCoord[0]  # Origin tag is the far left tag
            # print('closest tag pos', closestTag0Pos)
            # print('closest tag neg', closestTag0Neg)
            # print('origin tag1: ', xzCoord)
            # print('closest to 0 tag index value: ', closestTag0)

            outDiameter = 2 * tagHeight + diameter
            ratio = diameter / outDiameter
            arcLengthDis.append(0.0)
            for k in range(0, (len(xyCoord) - 1)):
                start = xyCoord[k]
                end = xyCoord[k + 1]
                curve = np.sum(np.sqrt(np.sum((start - end) ** 2)))
                #print('curve = ', curve)
                curve = curve * calcRatio
                arcTotal += curve
                arcLengthDis.append(arcTotal)
                print('arcLengthDis = ', arcLengthDis)

            for k in range(0, len(xyCoord)):
                if xyCoord[k, 0] < 0:
                    start = xyCoord[k]
                    end = centerCam
                    #print('start center = ', start)
                    #print('end center = ', end)
                    curve = np.sum(np.sqrt(np.sum((start - end) ** 2)))
                    curve = curve * calcRatio
                    camArcDis.append(curve)
                    #print('camArcDis = ', camArcDis)
                elif xyCoord[k, 0] > 0:
                    start = centerCam
                    end = xyCoord[k]
                    #print('start = ', start)
                    #print('end = ', end)
                    curve = np.sum(np.sqrt(np.sum((start - end) ** 2)))
                    curve = curve * calcRatio
                    camArcDis.append(curve)
                    print('camArcDis = ', camArcDis)
            # cam location on pipe
            if xyCoord[closestTag0, 0] > 0:
                camLocationX = arcLengthDis[closestTag0] - camArcDis[closestTag0]
            elif xyCoord[closestTag0, 0] < 0:
                camLocationX = arcLengthDis[closestTag0] + camArcDis[closestTag0]
            camLoc.append(camLocationX)
            print('cam loc pipe = ', camLoc)

            realTime = []

        #Graph
            startTime = time.time()
            #def animate(i, camLoc, camLocationZ):
            #ax.clear()
            #plt.axis([-50, 300, 175, 400])
            #plt.xticks(range(-50, 300, 20))  # Put x axis ticks every 10 units.
            #plt.yticks(range(0, 400, 20))  # Y ticks every 50.  You can provide any list.

            #plt.set_xlabel('Axial')
            #plt.set_ylabel('Circumferential')
            #plt.set_title('Camera Location on Pipe')

            # ani = animation.FuncAnimation(fig, animate, fargs=(camLoc, camLocationZ), interval=50)
            plt.scatter(camLocationX, zTotal)
            canvas.draw_idle()
            #plt.show()
            # print('plot', camLocationX, zTotal)
            #canvas.draw()
            canvas.flush_events()
            ser.reset_input_buffer()
            #plt.pause(0.000001)
            # plt.tight_layout()

            #toolbar = NavigationToolbar2Tk(canvas, root)
            #toolbar.update()
            #canvas._tkcanvas.pack(fill=tk.BOTH, expand=TRUE)

            #plt.show()
            print(f'{time.time()-startTime}')

    return(ser)
            #plt.cla()
    #    plt.xticks(range(-50, 300, 20))  # Put x axis ticks every 10 units.
    #    plt.yticks(range(0, 400, 20))  # Y ticks every 50.  You can provide any list.

    #    plt.xlabel('Axial')
    #    plt.ylabel('Circumferential')
    #    plt.title('Camera Location on Pipe')
            #ani = animation.FuncAnimation(fig, animate, fargs=(camLoc, camLocationZ), interval=50)
    #    plt.scatter(camLoc[i], camLocationZ[i])
        #print('plot', camLocationX, zTotal)
            #fig.canvas.draw()
            #fig.canvas.flush_events()
    #    plt.pause(0.0001)
            #plt.tight_layout()
    #    plt.show()
            #plt.draw()
        #time.sleep(0.0001)

            #fig.canvas.flush_events()
        #print('cord= ', data)


    #########################


#def save_file():
    #file = asksaveasfile('Untitled.txt',
    #                   defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    #plt.savefig("fig.png",bbox_inches="tight")
    #file.close()
    #return

def pause_file():
    global pause
    #file = asksaveasfile('Untitled.txt',
    #                   defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    #plt.pausefig("fig.png",bbox_inches="tight")
    #file.close()
    pause = 1
    print('pause = ', pause)
    return


def clear_text():
    #diameter.delete(0, END)
    canvas.delete("all")
    x0 = [0, 0, 0]

    y0 = [0, 0, 0]

    plt.plot(x0, y0)

    plt.show()
    return


# =========================================

# MAIN PROGRAM

# ========================================

root = tk.Tk()
root.title("EPRI")
# root.wm_iconbitmap('epri.png')
root.geometry('1000x800')
f = Figure(figsize=(5, 5), dpi=100)
plt = f.add_subplot(111)
plt.axis([-50, 300, 175, 400])
            #plt.xticks(range(-50, 300, 20))  # Put x axis ticks every 10 units.
            #plt.yticks(range(0, 400, 20))  # Y ticks every 50.  You can provide any list.

plt.set_xlabel('Axial')
plt.set_ylabel('Circumferential')
plt.set_title('Camera Location on Pipe')
canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().place(x=75, y=0, width=750, height=550)
canvas.draw()
ser = serial.Serial("COM6", 115200)  # Switch COM port to desired port
ser.reset_input_buffer()
# =============================



#x = [10, 20, 30]

#y = [10, 50, 7]



# start button
startText = tk.StringVar()

startButton = tk.Button(root, textvariable=startText, command=lambda: start_plot(), font="Raleway", bg="green",
                       fg="white", height=2, width=10)

startText.set("start")
startButton.place(x=200, y=600)

# clear button
clearText = tk.StringVar()
clearButton = tk.Button(root, textvariable=clearText, command=lambda: clear_text(), font="Raleway", bg="blue",
                       fg="white", height=2, width=10)

clearText.set("Clear")

clearButton.place(x=400, y=600)
# pause button
pauseText = tk.StringVar()

pauseButton = tk.Button(root, textvariable=pauseText, command=lambda: pause_file(), font="Raleway", bg="red",
                       fg="white", height=2, width=10)

pauseText.set("Pause")

pauseButton.place(x=600, y=600)

root.mainloop()


