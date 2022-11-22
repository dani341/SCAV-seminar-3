# Interface to do both parts of the seminar
# First you have to select the video you want to encode
# Next, you have to choose the encoder
# When you select the encoder the codification wil start.
# If you don't select a video  and directly select an encoder, first video option will be choosen
# You also can do a combo of four videos by clicking the last buton

#Daniel de Vargas Medina nia:233273 Seminar-3

import tkinter as tk
from tkinter import *
import subprocess


# Functions video_1, video_2, video_3 and video_4 are used to change the variable
# of the stringvar video, which contains the name of the video selected
def video_1(vid):
    vid.set("bbb_160x120.mp4")


def video_2(vid):
    vid.set("bbb_360x240.mp4")


def video_3(vid):
    vid.set("bbb_480p.mp4")


def video_4(vid):
    vid.set("bbb_720p.mp4")

#convert_to_VP8/VP9/h265/AV1() first needs to extract the value(string) of the strvar video (name of video selected)
#Then uses this name as an imput dor the ffmpeg call and the name without the extension for the output.

def convert_to_VP8(video_input):
    name = ""
    name += str(video_input.get())
    name1 = name.replace(".mp4", "")
    vp8 = name1 + "vp8.webm "
    subprocess.call("ffmpeg -i " + name + " -c:v libvpx -b:v 1M -c:a libvorbis " + vp8 + " -y", shell=True)


def convert_to_VP9(video_input):
    name = ""
    name += str(video_input.get())
    name1 = name.replace(".mp4", "")
    vp9 = name1 + "vp9.webm "
    subprocess.call("ffmpeg -i " + name + " -c:v libvpx-vp9 -crf 30 -b:v 0 " + vp9 + " -y", shell=True)


def convert_to_h265(video_input):
    name = ""
    name += str(video_input.get())
    name1 = name.replace(".mp4", "")
    h265 = name1 + "h265.mp4 "
    subprocess.call("ffmpeg -i " + name + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k " + h265 + " -y", shell=True)


def convert_to_AV1(video_input):
    name = ""
    name += str(video_input.get())
    name1 = name.replace(".mp4", "")
    av1 = name1 + "av1.mkv "
    subprocess.call("ffmpeg -i " + name + " -c:v libaom-av1 -crf 30 -b:v 0 " + av1 + " -y", shell=True)

#combo function first creates the encoded video files before to merge with the lowest quality video for
#a lower computational cost.
def combo(video_input):
    name = ""
    name += str(video_input.get())
    name1 = name.replace(".mp4", "")
    vp8 = name1 + "vp8.webm "
    vp9 = name1 + "vp9.webm "
    h265 = name1 + "h265.mp4 "
    av1 = name1 + "av1.mkv "
    output = name1 + "_combo.mp4"
    subprocess.call("ffmpeg -i " + name + " -c:v libvpx -b:v 1M -c:a libvorbis " + vp8 + " -y", shell=True)
    print("vp8 done")
    subprocess.call("ffmpeg -i " + name + " -c:v libvpx-vp9 -crf 30 -b:v 0 " + vp9 + " -y", shell=True)
    print("vp9 done")
    subprocess.call("ffmpeg -i " + name + " -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k " + h265 + " -y", shell=True)
    print("h256 done")
    subprocess.call("ffmpeg -i " + name + " -c:v libaom-av1 -crf 30 -b:v 0 " + av1 + " -y", shell=True)
    print("av1 done")
    subprocess.call("ffmpeg -i "
                    + name + " -i "
                    + vp8 + " -i "
                    + vp9 + " -i "
                    + h265 + " -i "
                    + name + ' -filter_complex "[0:v][1:v]hstack[t];[2:v][3:v]hstack[b];[t][b]vstack[v]" -map "[v]" -map 4:a -c:a copy -shortest ' + output + " -y", shell=True)

#Here the interface starts.
#Creation of the main window
window = tk.Tk()
#size of the window
window.geometry("600x525")
#initialization of the video value to after introduce it to the encoders
video = StringVar()
video.set("bbb_160x120.mp4")
#select video button and label section:
label_1 = tk.Label(window, text="1st Choose your video", font='Helvetica 16 bold', bg="blue", foreground="white")
label_1.pack(fill=tk.X)
#buttons call the function that renames the video stringvar with the indicated name respectively
v1 = tk.Button(
    text="bbb_160x120.mp4",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: video_1(video),
)
v1.pack()

v2 = tk.Button(
    text="bbb_360x240.mp4",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: video_2(video),
)
v2.pack()
print(video)

v3 = tk.Button(
    text="bbb_480p.mp4",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: video_3(video),
)
v3.pack()

v4 = tk.Button(
    text="bbb_720.mp4",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: video_4(video),
)
v4.pack()
# select encoder button and label section:
label_1 = tk.Label(window, text="2nd Choose your codec!", font='Helvetica 16 bold', bg="blue", foreground="white")
label_1.pack(fill=tk.X)
# every button calls the encoding function that uses the encoder indicated respectively and uses as input
# the video selected lastly or the default one
button_VP8 = tk.Button(
    text="VP8",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: convert_to_VP8(video),
)
button_VP8.pack()

button_VP9 = tk.Button(
    text="VP9",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: convert_to_VP9(video),
)
button_VP9.pack()

button_h265 = tk.Button(
    text="h265",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: convert_to_h265(video),
)
button_h265.pack()

button_AV1 = tk.Button(
    text="AV1",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: convert_to_AV1(video),
)
button_AV1.pack()
#combo button and label section:
label_2 = tk.Label(window, text="3rd Merge all videos into one!", font='Helvetica 16 bold', bg="blue", foreground="white")
label_2.pack(fill=tk.X)
#just calls the combo function
button_combo = tk.Button(
    text="Combine",
    width=25,
    height=2,
    bg="blue",
    fg="yellow",
    command=lambda: combo(video),
)
button_combo.pack()


#end of window main loop
window.mainloop()
