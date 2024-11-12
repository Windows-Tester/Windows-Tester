import tkinter as tk
from tkinter import messagebox
import platform
import psutil
import shutil

# Initialize the main application window
root = tk.Tk()
root.title("Windows Tester Tool")
root.geometry("400x300")

# Function to get system information
def get_system_info():
    sys_info = (
        f"System: {platform.system()}\n"
        f"Node Name: {platform.node()}\n"
        f"Release: {platform.release()}\n"
        f"Version: {platform.version()}\n"
        f"Machine: {platform.machine()}\n"
        f"Processor: {platform.processor()}\n"
    )
    messagebox.showinfo("System Information", sys_info)

# Function to check disk usage
def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    disk_info = (
        f"Total Disk Space: {total // (2**30)} GB\n"
        f"Used Disk Space: {used // (2**30)} GB\n"
        f"Free Disk Space: {free // (2**30)} GB\n"
    )
    messagebox.showinfo("Disk Usage", disk_info)

# Function to check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    messagebox.showinfo("CPU Usage", f"Current CPU Usage: {cpu_usage}%")

# Function to check memory usage
def check_memory_usage():
    memory_info = psutil.virtual_memory()
    mem_info = (
        f"Total Memory: {memory_info.total // (2**20)} MB\n"
        f"Available Memory: {memory_info.available // (2**20)} MB\n"
        f"Used Memory: {memory_info.used // (2**20)} MB\n"
        f"Memory Usage: {memory_info.percent}%\n"
    )
    messagebox.showinfo("Memory Usage", mem_info)

# Create GUI Elements
tk.Label(root, text="Windows Tester Tool", font=("Helvetica", 16)).pack(pady=10)

# Add buttons for each test
tk.Button(root, text="Get System Info", command=get_system_info, width=20).pack(pady=5)
tk.Button(root, text="Check Disk Usage", command=check_disk_usage, width=20).pack(pady=5)
tk.Button(root, text="Check CPU Usage", command=check_cpu_usage, width=20).pack(pady=5)
tk.Button(root, text="Check Memory Usage", command=check_memory_usage, width=20).pack(pady=5)

# Run the application
root.mainloop()
