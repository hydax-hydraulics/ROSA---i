import os
os.chdir("/home/pi/ROSA---i/")

import threading
import statistics
from os.path import join
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from functools import partial

import cv2
import numpy as np
import PIL

from PIL import ImageTk
from PIL import Image
import glob
import time
import math
import pyttsx3
#import os
import csv
from threading import Timer
from datetime import date,datetime
from subprocess import call
import time
import RPi.GPIO as GPIO
import os
import Adafruit_ADS1x15



root =Tk()
root.title("ROSA - i")
root.resizable(0,0)

root.geometry("790x400+10+10")
root.configure(background="white")

f1=Frame(root,bg="white")
f1.place(relwidth=1,relheight=1)
f1.place(relwidth=1,relheight=1)


label=Label(f1,text="WELCOME TO R O S A - i",font=("comicsansms"," 68", "bold"),fg="#db04a6",background="white")
label.place(relx=-0.25,relwidth=1.5,relheight=0.2)



#canvas=Canvas(root,height=HEIGHT,width=WIDTH)
#canvas.pack()

#the upper canvas should be placed before any otjher customization..

f1=Frame(root,bg="white")
f1.place(relwidth=1,relheight=1)



label=Label(f1,text="R O S A - i",font=("comicsansms"," 68", "bold"),fg="#db04a6",background="white")
label.place(relx=-0.25,relwidth=1.5,relheight=0.2)
pic1=PhotoImage(file="TEACH1.png")
openpicc=PhotoImage(file="OPEN1.png")
helppicc=PhotoImage(file="HELP1.png")
toolspicc=PhotoImage(file="TOOLS1.png")
of=PhotoImage(file="of.png")

def too():
    e=pyttsx3.init()
    e.setProperty('voice','english_rp+f4')
    text="Welcome to ROSA-i"
    e.say(text)
    e.runAndWait()
too()




    







##################################################################################################################
"""def speak_buildup(text):
    tts=gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
speak_buildup("Rosa is ready")
#######################################################################################################
def speak_teach(text):
    tts=gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
def speak_open(text):
    tts=gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)"""

#################################################################################################################
def when_teach():
    global circle1
    global one1
    global two1
    global three1
    global four1
    global donesym1
    global folder1
    global folder2
    global folder3
    global folder4
    global capture_camera
    
    
    
    def teach():
        
    
        e=pyttsx3.init()
        e.setProperty('voice','english_rp+f4')
        text="teach"
        e.say(text)
        e.runAndWait()
    teach()
    
            
    
    window=Toplevel()
    #when creating loop windows ,we must give >> toplevel<< instead creating simple window...

    #window.geometry("900x600")
    window.geometry("790x400+10+10")
    window.configure(bg="white")   #so here,background will be red as bg=red...
    #l11=Label(root,text="R O S A -i",font=("times new roman","39","bold"),bg="white",fg="pink")
    #the above code writes a text creating label and for the texts ,the dimensions are given...
   


        

    circle1=PhotoImage(file="newbackbutton.png")
    mainfolder=PhotoImage(file="mainfolderpic.png")
    capture_camera=PhotoImage(file="capturecamera.png")

    one1=PhotoImage(file="11.png")
    folder1=PhotoImage(file="1_folder.png")

    two1=PhotoImage(file="22.png")
    folder2=PhotoImage(file="2_folder.png")

    three1=PhotoImage(file="33.png")
    folder3=PhotoImage(file="3_folder.png")

    four1=PhotoImage(file="44.png")
    folder4=PhotoImage(file="4_folder.png")

    donesym1=PhotoImage(file="doonesymbol.png")

    label1=Label(window,text="R O S A - i",fg="#db04a6",bg="white",font=("comicsansms"," 40", "bold")).pack()
    #label1.place(relx=0.0,rely=-0.3,relwidth=1,relheight=0.9)


    f1=LabelFrame(window,bg="white",border=0)#.pack(padx=50,pady=8,fill=X)
    f1.place(relx=0.2,rely=0.2,relwidth=0.76,relheight=0.73)

    #l1=Label(f1,bg="pink",border=5) #here the line in the border is pink in color
    #l1.pack()
    l1= Label(f1,border=0,bg="black")
    l1.place(relx=0.0,rely=0.0,relwidth=1,relheight=1)


    pathA =("/home/pi/ROSA---i/train_images/folderA/*.*")
    pathB =("/home/pi/ROSA---i/train_images/folderB/*.*")
    pathC =("/home/pi/ROSA---i/train_images/folderC/*.*")
    pathD =("/home/pi/ROSA---i/train_images/folderD/*.*")


    def close():
        cam.release()
        window.destroy()

    bt1=Button(window,image=circle1,border=0,bg="white",command=close)
    bt1.place(relx=0.04,rely=0.85,relwidth=0.13,relheight=0.09)

    bt_1=Button(window,image=mainfolder,border=0,bg="white")
    bt_1.place(relx=0.019,rely=0.21,relwidth=0.08,relheight=0.099)
####################################################################

    def onedone():
        donesym1=PhotoImage(file="doonesymbol.png")
        btt1=Button(window,image=donesym1)
        btt1.image=donesym1
        btt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)


    def twodone():
        bt2=Button(window,image=donesym1)
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.088)

    def threedone():
        bt3=Button(window,image=donesym1)
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)

    def fourdone():
        bt4=Button(window,image=donesym1)
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)
###################################################################    
    def est1():
        NonBP=[]
        calc=[]
        i=2
        #print("pass")
        path = ("/home/pi/ROSA---i/train_images/folderA/*.*")
        print("path of file:",path)
        #path = ("/home/pi/test-repo/train/*.*")
        for a in glob.glob(path):
            ab = ("train_images/folderA/img_black_01.jpg")
            photo1 = cv2.imread(ab,0)
            print(photo1)

            bc=("train_images/folderA/img_black_0"+str(int(i))+".jpg")
            photo_all = cv2.imread(bc,0)           
            print(photo_all)
            if photo1.shape==photo_all.shape:
                diff1 = cv2.subtract(photo1,photo_all)
                non_black_pix = np.sum(diff1!=0)

                print("#########")
                print("non_black_pix",non_black_pix)
                NonBP.append(non_black_pix)
                u1=np.array(diff1)
                u4=print(u1)
                print(u4)
                u2=np.std(u1)
                u3=np.max(u1)
                print("standard deviation:",u2)
                print("maximum value :",u3)
                Pvalue=u3 - u2
                u5=int(Pvalue)
                print("Pvalue:",u5)

                i=i+1
                #print("i=",i)
                #print("#####")
                if i==5:
                    print("end of the loop")
                    print(NonBP)
                    u1=np.array(diff1)
                    u4=print(u1)
                    print(u4)
                    u2=np.std(u1)
                    u3=np.max(u1)
                    print("standard deviation:",u2)
                    print("maximum value :",u3)
                    Pvalue=u3 - u2
                    u5=int(Pvalue)
                    print("Pvalue:",u5)
                    break

        ef=("train_images/folderA/img_black_02.jpg")
        gh=("train_images/folderA/img_black_03.jpg")
        photo2 = cv2.imread(ef,0)
        photo3 = cv2.imread(gh,0)
        if photo2.shape==photo3.shape:
            diff1 = cv2.subtract(photo2,photo3)
            other_two_values = np.sum(diff1!=0)
            NonBP.append(other_two_values)
            print("other_two_values",other_two_values)
            print(NonBP)

        Mean = sum(NonBP)/len(NonBP)
        #Var = sum(pow(i_v - Mean,2) for i_v in NonBP)/len(NonBP)
        #Std_dev = math.sqrt(Var)
        #Std_dev=statistics.stdev(NonBP)
        print("Mean is ",Mean)
        #calc.append(Mean)
        #print("Std_dev",Std_dev)
        #calc.append(Std_dev)
        Uthreshold = Mean+u2
        Lthreshold = Mean-u2
        print("Uthreshold",Uthreshold)
        #calc.append(Uthreshold)
        print("Lthreshold",Lthreshold)
        #calc.append(Lthreshold)

        #print("calc=",calc)

        #row_list=[["Mean","Std_dev","Uthreshold","Lthreshold"],[Mean,Std_dev,Uthreshold,Lthreshold]]
        row_list=[Uthreshold]
        ff=("train_images/folderA/4.csv")
        with open(ff,"w",newline="") as file:
              writer = csv.writer(file)
              writer.writerow(row_list)
##########################################################
    def est2():
        NonBP=[]
        calc=[]
        i=2
        #print("pass")
        path = ("/home/pi/ROSA---i/train_images/folderB/*.*")
        print("path of file:",path)
        #path = ("/home/pi/test-repo/train/*.*")
        for a in glob.glob(path):
            ab = ("train_images/folderB/img_black_01.jpg")
            photo1 = cv2.imread(ab,0)

            bc=("train_images/folderB/img_black_0"+str(int(i))+".jpg")
            photo_all = cv2.imread(bc,0)           

            if photo1.shape==photo_all.shape:
                diff = cv2.subtract(photo1,photo_all)
                non_black_pix = np.sum(diff!=0)

                print("#########")
                print("non_black_pix",non_black_pix)
                NonBP.append(non_black_pix)

                i=i+1
                #print("i=",i)
                #print("#####")
                if i==5:
                    print("end of the loop")
                    print(NonBP)
                    break

        ef=("train_images/folderB/img_black_02.jpg")
        gh=("train_images/folderB/img_black_03.jpg")
        photo2 = cv2.imread(ef,0)
        photo3 = cv2.imread(gh,0)
        if photo2.shape==photo3.shape:
            diff1 = cv2.subtract(photo2,photo3)
            other_two_values = np.sum(diff1!=0)
            NonBP.append(other_two_values)
            print("other_two_values",other_two_values)
            print(NonBP)

        Mean = sum(NonBP)/len(NonBP)
        #Var = sum(pow(i_v - Mean,2) for i_v in NonBP)/len(NonBP)
        #Std_dev = math.sqrt(Var)
        Std_dev=statistics.stdev(NonBP)
        print("Mean is ",Mean)
        #calc.append(Mean)
        print("Std_dev",Std_dev)
        #calc.append(Std_dev)
        Uthreshold = Mean+Std_dev
        Lthreshold = Mean-Std_dev
        print("Uthreshold",Uthreshold)
        calc.append(Uthreshold)
        print("Lthreshold",Lthreshold)
        #calc.append(Lthreshold)

        print("calc=",calc)

        #row_list=[["Mean","Std_dev","Uthreshold","Lthreshold"],[Mean,Std_dev,Uthreshold,Lthreshold]]
        row_list=[Uthreshold]
        ff=("train_images/folderB/4.csv")
        with open(ff,"w",newline="") as file:
              writer = csv.writer(file)
              writer.writerow(row_list)
############################################################
    def est3():
        NonBP=[]
        calc=[]
        i=2
        #print("pass")
        path = ("/home/pi/ROSA---i/train_images/folderC/*.*")
        print("path of file:",path)
        #path = ("/home/pi/test-repo/train/*.*")
        for a in glob.glob(path):
            ab = ("train_images/folderC/img_black_01.jpg")
            photo1 = cv2.imread(ab,0)

            bc=("train_images/folderC/img_black_0"+str(int(i))+".jpg")
            photo_all = cv2.imread(bc,0)           

            if photo1.shape==photo_all.shape:
                diff = cv2.subtract(photo1,photo_all)
                non_black_pix = np.sum(diff!=0)

                print("#########")
                print("non_black_pix",non_black_pix)
                NonBP.append(non_black_pix)

                i=i+1
                #print("i=",i)
                #print("#####")
                if i==5:
                    print("end of the loop")
                    print(NonBP)
                    break

        ef=("train_images/folderC/img_black_02.jpg")
        gh=("train_images/folderC/img_black_03.jpg")
        photo2 = cv2.imread(ef,0)
        photo3 = cv2.imread(gh,0)
        if photo2.shape==photo3.shape:
            diff1 = cv2.subtract(photo2,photo3)
            other_two_values = np.sum(diff1!=0)
            NonBP.append(other_two_values)
            print("other_two_values",other_two_values)
            print(NonBP)

        Mean = sum(NonBP)/len(NonBP)
        #Var = sum(pow(i_v - Mean,2) for i_v in NonBP)/len(NonBP)
        #Std_dev = math.sqrt(Var)
        Std_dev=statistics.stdev(NonBP)
        print("Mean is ",Mean)
        #calc.append(Mean)
        print("Std_dev",Std_dev)
        #calc.append(Std_dev)
        Uthreshold = Mean+Std_dev
        Lthreshold = Mean-Std_dev
        print("Uthreshold",Uthreshold)
        calc.append(Uthreshold)
        print("Lthreshold",Lthreshold)
        #calc.append(Lthreshold)

        print("calc=",calc)

        #row_list=[["Mean","Std_dev","Uthreshold","Lthreshold"],[Mean,Std_dev,Uthreshold,Lthreshold]]
        row_list=[Uthreshold]
        ff=("train_images/folderC/4.csv")
        with open(ff,"w",newline="") as file:
              writer = csv.writer(file)
              writer.writerow(row_list)

################################################################

    def est4():
        NonBP=[]
        calc=[]
        i=2
        #print("pass")
        path = ("/home/pi/ROSA---i/train_images/folderD/*.*")
        print("path of file:",path)
        #path = ("/home/pi/test-repo/train/*.*")
        for a in glob.glob(path):
            ab = ("train_images/folderD/img_black_01.jpg")
            photo1 = cv2.imread(ab,0)

            bc=("train_images/folderD/img_black_0"+str(int(i))+".jpg")
            photo_all = cv2.imread(bc,0)           

            if photo1.shape==photo_all.shape:
                diff = cv2.subtract(photo1,photo_all)
                non_black_pix = np.sum(diff!=0)

                print("#########")
                print("non_black_pix",non_black_pix)
                NonBP.append(non_black_pix)

                i=i+1
                #print("i=",i)
                #print("#####")
                if i==5:
                    print("end of the loop")
                    print(NonBP)
                    break

        ef=("train_images/folderD/img_black_02.jpg")
        gh=("train_images/folderD/img_black_03.jpg")
        photo2 = cv2.imread(ef,0)
        photo3 = cv2.imread(gh,0)
        if photo2.shape==photo3.shape:
            diff1 = cv2.subtract(photo2,photo3)
            other_two_values = np.sum(diff1!=0)
            NonBP.append(other_two_values)
            print("other_two_values",other_two_values)
            print(NonBP)

        Mean = sum(NonBP)/len(NonBP)
        #Var = sum(pow(i_v - Mean,2) for i_v in NonBP)/len(NonBP)
        #Std_dev = math.sqrt(Var)
        Std_dev=statistics.stdev(NonBP)
        print("Mean is ",Mean)
        #calc.append(Mean)
        print("Std_dev",Std_dev)
        #calc.append(Std_dev)
        Uthreshold = Mean+Std_dev
        Lthreshold = Mean-Std_dev
        print("Uthreshold",Uthreshold)
        calc.append(Uthreshold)
        print("Lthreshold",Lthreshold)
        #calc.append(Lthreshold)

        print("calc=",calc)

        #row_list=[["Mean","Std_dev","Uthreshold","Lthreshold"],[Mean,Std_dev,Uthreshold,Lthreshold]]
        row_list=[Uthreshold]
        ff=("train_images/folderD/4.csv")
        with open(ff,"w",newline="") as file:
              writer = csv.writer(file)
              writer.writerow(row_list)




    def estimate_button1():
        bt4_est=Button(window,text="ESTIMATE",border=0,bg="white",command=est1)
        bt4_est.place(relx=0.20,rely=0.82,relwidth=0.09,relheight=0.08)
    def estimate_button2():
        bt4_est=Button(window,text="ESTIMATE",border=0,bg="white",command=est2)
        bt4_est.place(relx=0.20,rely=0.82,relwidth=0.09,relheight=0.08)

    def estimate_button3():
        bt4_est=Button(window,text="ESTIMATE",border=0,bg="white",command=est3)
        bt4_est.place(relx=0.20,rely=0.82,relwidth=0.09,relheight=0.08)

    def estimate_button4():
        bt4_est=Button(window,text="ESTIMATE",border=0,bg="white",command=est4)
        bt4_est.place(relx=0.20,rely=0.82,relwidth=0.09,relheight=0.08)

###################################################################################    
    def first_save():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderA/img_black_01"+".jpg"
        cv2.imwrite(file,canny_pics)

    def second_photo():
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[second_save(),twodone(),third_photo()])
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)

    def second_save():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderA/img_black_02"+".jpg"
        cv2.imwrite(file,canny_pics)

    def third_photo():
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[third_save(),threedone(),fourth_photo()])
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)

    def third_save():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderA/img_black_03"+".jpg"
        cv2.imwrite(file,canny_pics)

    def fourth_photo():
        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourth_save(),fourdone(),estimate_button1()])
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)

    def fourth_save():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderA/img_black_04"+".jpg"
        cv2.imwrite(file,canny_pics)



    def firstphoto_second():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderB/img_black_01"+".jpg"
        cv2.imwrite(file,canny_pics)

    def firstphoto_third():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderC/img_black_01"+".jpg"
        cv2.imwrite(file,canny_pics)

    def firstphoto_fourth():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderD/img_black_01"+".jpg"
        cv2.imwrite(file,canny_pics)




    def secondphoto_second():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderB/img_black_02"+".jpg"
        cv2.imwrite(file,canny_pics)

    def secondphoto_third():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderC/img_black_02"+".jpg"
        cv2.imwrite(file,canny_pics)

    def secondphoto_fourth():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderD/img_black_02"+".jpg"
        cv2.imwrite(file,canny_pics)


    def thirdphoto_second():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderB/img_black_03"+".jpg"
        cv2.imwrite(file,canny_pics)

    def thirdphoto_third():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderC/img_black_03"+".jpg"
        cv2.imwrite(file,canny_pics)

    def thirdphoto_fourth():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderD/img_black_03"+".jpg"
        cv2.imwrite(file,canny_pics)


    def fourthphoto_second():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderB/img_black_04"+".jpg"
        cv2.imwrite(file,canny_pics)

    def fourthphoto_third():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderC/img_black_04"+".jpg"
        cv2.imwrite(file,canny_pics)

    def fourthphoto_fourth():
        image=Image.fromarray(img1)
        canny_pics=cv2.Canny(img1,100,40)
        file="/home/pi/ROSA---i/train_images/folderD/img_black_04"+".jpg"
        cv2.imwrite(file,canny_pics)
#####################################################################

    def fourth_button():
        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto_second(),fourdone(),estimate_button2()])
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)

    def third_button():
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto_second(),threedone(),fourth_button()])
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)        
    def second_button():
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto_second(),twodone(),third_button()])
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)

########################################################################
    def fourth_snap():
        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto_third(),fourdone(),estimate_button3()])
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)

    def third_snap():
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto_third(),threedone(),fourth_snap()])
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)    
    def second_snap():
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto_third(),twodone(),third_snap()])
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)
##########################################################################        
    def fourth_snap4():
        bt4=Button(window,image=four1,border=0,bg="white",command=lambda :[fourthphoto_fourth(),fourdone(),estimate_button4()])
        bt4.place(relx=0.11,rely=0.69,relwidth=0.06,relheight=0.08)

    def third_snap4():
        bt3=Button(window,image=three1,border=0,bg="white",command=lambda :[thirdphoto_fourth(),threedone(),fourth_snap4()])
        bt3.place(relx=0.11,rely=0.58,relwidth=0.06,relheight=0.08)
    def second_snap4():
        bt2=Button(window,image=two1,border=0,bg="white",command=lambda :[secondphoto_fourth(),twodone(),third_snap4()])
        bt2.place(relx=0.11,rely=0.47,relwidth=0.06,relheight=0.08)


#############################################################################        

    def folder1_path():

        bt_1=Button(window,image=capture_camera,border=0,bg="white")
        bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[first_save(),onedone(),second_photo()])
        bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)

    def folder2_path():
        bt_1=Button(window,image=capture_camera,border=0,bg="white")
        bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto_second(),onedone(),second_button()])
        bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)

    def folder3_path():
        bt_1=Button(window,image=capture_camera,border=0,bg="white")
        bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto_third(),onedone(),second_snap()])
        bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)



    def folder4_path():
        bt_1=Button(window,image=capture_camera,border=0,bg="white")
        bt_1.place(relx=0.11,rely=0.21,relwidth=0.07,relheight=0.099)

        bt1=Button(window,image=one1,border=0,bg="white", command=lambda:[firstphoto_fourth(),onedone(),second_snap4()])
        bt1.place(relx=0.11,rely=0.34,relwidth=0.06,relheight=0.08)



    bt_1=Button(window,image=folder1,border=0,bg="white",command = folder1_path)
    bt_1.place(relx=0.03,rely=0.34,relwidth=0.06,relheight=0.08)

    for ab in glob.glob(pathA):
        print(ab)
        if len(pathA)>0:
            bt_1.configure(state="disabled")


    bt_2=Button(window,image=folder2,border=0,bg="white",command = folder2_path)
    bt_2.place(relx=0.03,rely=0.47,relwidth=0.06,relheight=0.08)

    for bc in glob.glob(pathB):
        print(bc)
        if len(pathB)>0:
            bt_2.configure(state="disabled")




    bt_3=Button(window,image=folder3,border=0,bg="white",command = folder3_path)
    bt_3.place(relx=0.03,rely=0.58,relwidth=0.06,relheight=0.08)

    for cd in glob.glob(pathC):
        print(cd)
        if len(pathC)>0:
            bt_3.configure(state="disabled")


    bt_4=Button(window,image=folder4,border=0,bg="white",command = folder4_path)
    bt_4.place(relx=0.03,rely=0.69,relwidth=0.06,relheight=0.08)    

    for de in glob.glob(pathD):
        print(de)
        if len(pathD)>0:
            bt_4.configure(state="disabled")


    cam = cv2.VideoCapture(0)
    
    def change_resol():
        cam.set(3,320)
        cam.set(4,240)
    change_resol()
    
    while True:
        _ , frames = cam.read()
        img1 = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img1,100,40)
        edgesvid = ImageTk.PhotoImage(Image.fromarray(edges))
        #edgesvid1 = ImageTk.PhotoImage(Image.fromarray(edges))
        l1["image"] = edgesvid

        window.update()

        if cv2.waitKey(1)& 0xFF==ord('q'):
            break
    cam.release() 
    cv2.destroyAllWindows()
    
    
    




####################################################################################################################


def whenopen():

    global list1
    global circle1
    global one1
    global two1
    global three1
    global four1
    global test1
    global live1
    
    
    def whenopen():
        e=pyttsx3.init()
        e.setProperty('voice','english_rp+f4')
        text="open"
        e.say(text)
        e.runAndWait()
    whenopen()
    
    

    window2=Toplevel()

    window2.geometry("790x400+10+10")
    window2.configure(background="white")


    label1=Label(window2,text="R O S A - i",fg="#db04a6",bg="white",font=("comicsansms"," 38", "bold"))
    label1.place(relx=0.0,rely=-0.35,relwidth=1,relheight=0.9)

    ft2=Frame(window2,bg="white",padx=25)
    ft2.place(relx=0.16,rely=0.2,relwidth=0.75,relheight=0.78)


    bt1= Label(ft2,border=0,bg="black")
    bt1.place(relx=0.0,rely=0.0,relwidth=1,relheight=1)
    
    
    
    def close():
        window2.destroy()
        cam.release()

    circle1=PhotoImage(file="newbackbutton.png")
    circle1btn=Button(window2,image=circle1,border=0,bg="white",command=close)

    circle1btn.image=circle1
    circle1btn.place(relx=0.04,rely=0.90,relwidth=0.13,relheight=0.09)

    def choosethefolder():
        global l1
        global l3
        global l4
        global buttonclick
        global buttonclick1
        
        def choosethefolder():
            e=pyttsx3.init()
            e.setProperty('voice','english_rp+f4')
            text="choose folder"
            e.say(text)
            e.runAndWait()
        choosethefolder()
        
        files=[]
        #cam.release()
        #fla=filedialog.askdirectory(initialdir="C:/Users/acer/Desktop",title="select the image",filetypes=[(".csv Files", "*.csv"),("image files","*.jpg")])
        #
        fla=filedialog.askdirectory(parent=window2,initialdir="/home/pi/ROSA---i/train_images")

        print(fla)##files.append(fla)
        #print("files are",files)
        path_for_img_grayed = (fla+"/img_black_01.jpg")
        print(path_for_img_grayed)
        path_for_csvfile = (fla+"/4.csv")
        print(path_for_csvfile)
        print("pass")
        path_for_img_grayed_1=(fla+"/img_black_01.jpg")
        print(path_for_img_grayed_1)
        path_for_csvfile=(fla+"/4.csv")
        print(path_for_csvfile)
        print("pass")
        
        
        


        buttonclick = 0
        buttonclick1=0
        
        def count():
            global buttonclick
            global l3
            buttonclick += 1
            l3.configure(text= " 0" + str(buttonclick))
                  
                 
        def count1():
            global buttonclick1
            global l1
            buttonclick1 += 1
            l1.configure(text= " 0" + str(buttonclick1))
        
        
    
        
        def folderB():
            e=pyttsx3.init()
            e.setProperty('voice','english_rp+f4')
            text="folderB chosen"
            e.say(text)
            e.runAndWait()
        folderB()
            
            


    

        
        def testing():
        #cam.release()
            global l1
            global buttonclick
            global l3
            global buttonclick1
            image=Image.fromarray(hellovid)
            canny_pics=cv2.Canny(hellovid,100,40)
            file="/home/pi/ROSA---i/test/img00"+".jpg"
            cv2.imwrite(file,canny_pics)

            imggrayed= cv2.imread(path_for_img_grayed,0)
            print(imggrayed,"imggrayed")
            print("photo of first photo for comparing")
            #i took trained image here ...........
            template = cv2.imread("test/img00.jpg",0)
            print(template,"template")
            print("Taken the test pic")

            #i need to load csv file here
            filee = path_for_csvfile
            print(filee,"this path is for csv file")
            with open(filee,"r") as letscsv:
                csv_reader = csv.reader(letscsv)
                for line in csv_reader:
                    print(line,":")
                    print(len(line))
                    compute_value=line.pop(0)
                    print("compute_value",compute_value)
                    Uthreshold = int(float(compute_value))
                    print(type(Uthreshold))
                    break
                
            imggrayed_1= cv2.imread(path_for_img_grayed_1,0)
            print(imggrayed_1,"imggrayed_1")
            print("photo of first photo for comparing")
            #i took trained image here ...........
            template_1 = cv2.imread("test/img00.jpg",0)
            print(template_1,"template_1")
            print("Taken the test pic")
            
            
            ab=("train_images/folderB/img_black_01.jpg")
            photo2=cv2.imread(ab,0)
            NonBP=[]
                



            if imggrayed_1.shape == template_1.shape:
                diffe1 = cv2.subtract(imggrayed_1,template_1)
                cv2.imshow('img',diffe1)
                non_black_pix=np.sum(diffe1!=0)
                print("non_black_pix",non_black_pix)
                NonBP.append(non_black_pix)
                x1=np.array(diffe1)
                x4=print(x1)
                print(x4)
                x2=np.std(x1)
                x3=np.max(x1)
                print("standard deviation: ",x2)
                print("Maximum value:",x3)
                Pvalue=x3 - x2
                x5=int(Pvalue)
                print("Pvalue:",x5)
                if Pvalue >x5:
                    print("it has a greater values")
                else:
                    print("it has a lower values")
                

                x= np.sum(diffe1!=0)
                #print(difference.shape)
                print("non_black_pixels",x)
                non_black_pixels = x.item(0)
                print(type(non_black_pixels))
                cv2.imshow('image',non_black_pixels)
                
                def hello():
                    e=pyttsx3.init()
                    e.setProperty('voice','english_rp+f4')
                    text="rejected"
                    e.say(text)
                    e.runAndWait()
                    
                def accep():
                    e=pyttsx3.init()
                    e.setProperty('voice','english_rp+f4')
                    text="accepted"
                    e.say(text)
                    e.runAndWait()

                
                    
                


                def delete_img1():
                    circleebtn.place_forget()
                def delete_img2():
                    circle2btn.place_forget()
               
                
                ff = (fla+"/Result.csv")
                #ff=("/home/pi/ROSA---i/train_images/folderA/Results.csv")
                with open(ff,"a",newline="") as file:
                    if non_black_pixels > Uthreshold:
                        print("non black pixel is greater than uthreshold")
                        circlee= PhotoImage(file="reject1.png")
                        difference = abs(non_black_pixels - Uthreshold)
                        quotient = difference/Uthreshold
                        percentage = quotient * 100
                        #print("percentage:",  percentage)
                        formatted_num = format(percentage, ".2f")
                        l4.configure(text="" + str(formatted_num)+ "%")
                        circleebtn=Button(window2,image = circlee,border=0,bg="white")
                        circleebtn.image = circlee
                        circleebtn.place(relx=0.4,rely=0.5,relwidth=0.27,relheight=0.12)
                        count()
                        hello()
                        today = datetime.now()
                        d1 = today.strftime("%d/%m/%Y %H:%M:%S")
                        row_list = ['Rejected',formatted_num,d1]
                        writer = csv.writer(file)
              #currentdatetime = datetime.now()
                        writer.writerow(row_list)
                        window2.update()
                        window2.after(2000,delete_img1())
                    else:
                        print("this statement is for lthreshold")
                        circle2=PhotoImage(file="accept1.png")
                        difference = abs(non_black_pixels - Uthreshold)
                        quotient = difference/Uthreshold
                        percentage = quotient * 100
                        #print("percentage:",  percentage)
                        formatted_num = format(percentage, ".2f")
                        l4.configure(text="" + str(formatted_num)+ "%")
                        circle2btn=Button(window2,image = circle2,border =0,bg="white")
                        circle2btn.image = circle2
                        circle2btn.place(relx=0.4,rely=0.5,relwidth=0.30,relheight=0.12)
                        count1()
                        accep()
                        today1 = datetime.now()
                        d2 = today1.strftime("%d/%m/%Y %H:%M:%S")
                        row_list = ['Accepted',formatted_num,d2]
                        
                        writer = csv.writer(file)
              #currentdatetime = datetime.now()
                        writer.writerow(row_list)
                        window2.update()
                        window2.after(2000,delete_img2())
                        
                            
            try:
                os.remove("test/img00.jpg")
            except:
                pass

            #Timer(5,testing).start()
            
            


#######################################################################################################
        test1=PhotoImage(file="test1.png")
        b1=Button(window2,image=test1,border=0,bg="white",command=testing)
        b1.image=test1
        b1.place(relx=0.04,rely=0.50,relwidth=0.10,relheight=0.17) 
        
        l1=Label(window2,text = "0", bg = "white",fg="green")
        l1.place(relx=0.02,rely=0.1,relwidth=0.1,relheight=0.10)

        l2=Label(window2,text = "/", bg = "white",fg="black",)
        l2.place(relx=0.10,rely=0.1,relwidth=0.05,relheight=0.10)

        l3=Label(window2,text = "0", bg = "white",fg="red")
        l3.place(relx=0.15,rely=0.1,relwidth=0.1,relheight=0.10)
        
        l4=Label(window2,text = "0", bg = "white",fg="black")
        l4.place(relx=0.05,rely=0.3,relwidth=0.1,relheight=0.10)
    test1=PhotoImage(file="choose1.png")
    b1=Button(window2,image=test1,border=0,bg="white",command=choosethefolder)
    b1.image=test1
    b1.place(relx=0.04,rely=0.65,relwidth=0.10,relheight=0.17)


    cam=cv2.VideoCapture(0)
    
    def change_resol():
        cam.set(3,320)
        cam.set(4,240)
    change_resol()
    
    while True:
        _,frame =cam.read()

        hellovid= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        lower_red = np.array([30,150,50])
        upper_red = np.array([255,255,180])

        mask = cv2.inRange(hellovid,lower_red,upper_red)
        res = cv2.bitwise_and(frame,frame,mask=mask)
        edges1 =cv2.Canny(hellovid,100,40)
        edgesvid2 = ImageTk.PhotoImage(Image.fromarray(hellovid))
        edgesvid1 = ImageTk.PhotoImage(Image.fromarray(edges1))
        bt1["image"]=edgesvid1
        key = cv2.waitKey(1) & 0xFF
        if key==32:
            break


        window2.update()


    cv2.destroyAllWindows()
    cam.release()
    



####################################################################################################################################################
def whenhelp():
    window3=Toplevel()

    window3.geometry("790x400+10+10") 
    window3.configure(background="white")
    
    

    global wifi1
    global pass1
    global conn1
    
    def whenhelp():
        e=pyttsx3.init()
        e.setProperty('voice','english_rp+f4')
        text="help"
        e.say(text)
        e.runAndWait()
    whenhelp()



    label1=Label(window3,text="R O S A -i",fg="#db04a6",bg="white",font=("comicsansms"," 60"))
    label1.place(relx=0.0,rely=-0.3,relwidth=1,relheight=0.9)

    ft3=Frame(window3,bg="white")
    ft3.place(relx=0.25,rely=0.3,relwidth=0.5,relheight=0.45)


    wifi1=PhotoImage(file="wifipic.png")
    wifi1btn=Button(window3,image=wifi1,border=0,bg="white")
    wifi1btn.image=wifi1
    wifi1btn.place(relx=0.4,rely=0.31,relwidth=0.396,relheight=0.12)



    pass1=PhotoImage(file="passpic.png")
    pass1btn=Button(window3,image=pass1,border=0,bg="white")
    pass1btn.image=pass1
    pass1btn.place(relx=0.4,rely=0.45,relwidth=0.38,relheight=0.12)



    conn1=PhotoImage(file="connpic.png")
    conn1btn=Button(window3,image=conn1,border=0,bg="white")
    conn1btn.image=conn1
    conn1btn.place(relx=0.4,rely=0.6,relwidth=0.39,relheight=0.12)


    circle1=PhotoImage(file="newbackbutton.png")
    circle1btn=Button(window3,image=circle1,border=0,bg="white",command=window3.destroy)
    circle1btn.image= circle1
    circle1btn.place(relx=0.1,rely=0.75,relwidth=0.14,relheight=0.09)
    

    
def task1():
    pi_gpio_out_09 =21
    pi_gpio_out_22 =15
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pi_gpio_out_09, GPIO.OUT)
    GPIO.setup(pi_gpio_out_22, GPIO.OUT)
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN_BATTERY =2/3
    RATIO_BATTERY =0.1875
    print('Reading ADS1x15 values, press Ctrl-C to quit...')
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
    print('-' * 37)
    while True:
        GPIO.output(pi_gpio_out_09, True)
        values = [0]*4
        value_Current =[0]*4
        value_Voltage =[0]*4
        value_Voltage_Battery =0
        value_battery_channel =0
        values[1] = adc.read_adc(1,1)
        value_battery_channel = adc.read_adc(0,GAIN_BATTERY)
        time.sleep(0.9)
        value_Current[1] =((values[1]*0.125)/100)+0.0289999999999999
        value_Voltage[1]=(values[1]*0.125/1000)
        value_Voltage_Battery=(value_battery_channel*RATIO_BATTERY/1000)+((value_battery_channel*RATIO_BATTERY/1000)*0.24)-.03
        print(round(value_Voltage_Battery,2))
        if round(value_Voltage_Battery,2)<=3.9:
            GPIO.output(pi_gpio_out_22, True)
            call("sudo shutdown -h now", shell=True)
        else:
            GPIO.output(pi_gpio_out_22, False)
            time.sleep(0.5)
    t1=threading.Thread(target=task1,name='t1')
    t2=threading.Thread(target=task2,name='t2')
    
    t1.start()
    t2.start()
    

    
    
    root=tkinter.Tk()

def onClick():
    answer=messagebox.askquestion("askquestion", 'power off?')
    print(answer)
    if answer == 'yes':
        task1()
    elif answer =='no':
        root.quit()

    
    


    


###################################################################################33


b1=Button(f1,image=pic1,border=0,bg="white",command=when_teach,cursor="hand2")
b1.place(relx=0.05,rely=0.25,relwidth=0.44,relheight=0.30)



b2=Button(f1,image=openpicc,border=0,bg="white",command=whenopen,cursor="dot")
b2.place(relx=0.52,rely=0.25,relwidth=0.43,relheight=0.30)


b3=Button(f1,image=helppicc,border=0,bg="white",command=whenhelp,cursor="man")
b3.place(relx=0.05,rely=0.6,relwidth=0.43,relheight=0.30)



b4=Button(f1,image=toolspicc,border=0,bg="white",cursor="diamond_cross")
b4.place(relx=0.52,rely=0.6,relwidth=0.44,relheight=0.30)

b5=Button(root,image=of,command=onClick)
b5.grid(row=1,column=1,sticky=NW)



root.mainloop()









