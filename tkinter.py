# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 13:17:57 2021

@author: Administrator
"""
import tkinter as tk
import time




class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x380")
        self.nowTimeText = tk.StringVar()
        self.nowTimeText.set("当前时间")
        self.nowTemperatureText=tk.StringVar()
        self.nowTemperatureText.set("当前温度")
        self.nowTimeLabel = tk.Label(self.root, textvariable=self.nowTimeText,font="Times 30 bold")
        self.nowTemperatureLabel= tk.Label(self.root, textvariable=self.nowTemperatureText,font="Times 30 bold")
        self.button = tk.Button(self.root,
                                text="取值",
                                command=self.changeText)
        self.button.pack()
        self.nowTimeLabel.pack()
        self.nowTemperatureLabel.pack()
        self.root.mainloop()

    def changeText(self):
       
           
            value="当前时间 : %s" % time.ctime()
            #time.sleep(5)
            self.nowTimeText.set(value) 
            self.nowTemperatureText.set("当前温度")

app=Test()
