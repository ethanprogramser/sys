from tkinter import *
import psutil
import os

class app:
    def __init__(self):
        self.cpu = psutil.cpu_percent(interval=1)
        self.cpu_ =psutil.cpu_count(logical=True)

        self.total_ram  = psutil.virtual_memory().total / (1024 ** 3)
        self.ram_used = psutil.virtual_memory().used / (1024 ** 3)
        self.ram_percentage = self.ram_used / self.total_ram * 100
    
        self.osm = os.uname().sysname
        self.arch = os.uname().machine
        self.kernel = os.uname().release

        self.win = Tk()
        self.win.geometry("900x200")
        self.win.title = "system health"

        self.ram_label = Label(self.win, text="RAM Usage")
        self.total_ram_ = Label(self.win, text=str(self.total_ram) + "GB total Memory")
        self.ram_usage = Label(self.win, text=str(self.ram_used) + "GB Memory Used")
        self.ram_per = Label(self.win, text=str(self.ram_percentage) + "% of Memory being used")
        self.cpu_label = Label(self.win, text="CPU Usage")
        self.cpu_per = Label(self.win, text=str(self.cpu) + "% of CPU Usage")
        self.total_cores = Label(self.win, text=str(self.cpu_) + " total cores")
        self.system_info = Label(self.win, text="System Info")
        self.os_label = Label(self.win, text= "Operating system: " + self.osm)
        self.arcut = Label(self.win, text="Architecture: " + self.arch)
        self.kern = Label(self.win, text="Kernel Version: " + self.kernel)

        self.refresh = Button(self.win, text="Refresh", command=self.refresh)
        
        self.ram_label.grid(row=1, column=1, padx=40)
        self.cpu_label.grid(row=1, column=2, padx=40)
        self.system_info.grid(row=1, column=3, padx=40)
        self.total_ram_.grid(row=2, column=1, padx=40)
        self.ram_usage.grid(row=3, column=1, padx=40)
        self.ram_per.grid(row=4, column=1, padx=40)
        self.cpu_per.grid(row=2, column=2, padx=40)
        self.total_cores.grid(row=3, column=2, padx=40) 
        self.os_label.grid(row=2, column=3, padx=40)
        self.arcut.grid(row=3, column=3, padx=40)
        self.kern.grid(row=4, column=3, padx=40)
        
        self.refresh.grid(row=5, column=2, padx=40)
        self.win.mainloop()

    def refresh(self):
        self.cpu = psutil.cpu_percent(interval=1)
        self.ram_used = psutil.virtual_memory().used / (1024 ** 3)
        self.ram_percentage = self.ram_used / self.total_ram * 100

        self.ram_usage.config(text=str(self.ram_used) + "GB Memory Used")
        self.ram_per.config(text=str(self.ram_percentage) + "% of Memory being used")
        self.cpu_per.config(text=str(self.cpu) + "% of CPU Usage")

app()
