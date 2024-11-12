# Windows Tester Tool

A simple Python-based GUI tool for testing basic system performance and getting essential system information on Windows. Built with Tkinter, this tool provides buttons to check disk usage, CPU usage, memory usage, and general system information. 

## Features

- **System Information**: Retrieve basic information about the Windows system, including OS version, node name, and processor type.
- **Disk Usage**: Check the total, used, and free disk space on the main drive.
- **CPU Usage**: Display the current CPU usage percentage.
- **Memory Usage**: Show the total, available, used memory, and the memory usage percentage.

## Requirements

- **Python 3.6+**
- **Tkinter** (comes installed by default with Python on Windows)
- **psutil** library

## Installation

1. **Clone the repository** or **download the script**.

2. **Install `psutil`** if it's not already installed:

    ```bash
    pip install psutil
    ```

## Usage

1. Open a terminal or command prompt.
2. Run the script with Python:

    ```bash
    python windows_tester_tool.py
    ```

3. The GUI will open, allowing you to click buttons for each system test.

## Functionality

- **Get System Info**: Displays details about the operating system and processor.
- **Check Disk Usage**: Shows total, used, and free space on the main disk drive.
- **Check CPU Usage**: Shows the CPU usage as a percentage.
- **Check Memory Usage**: Displays total, available, used memory, and memory usage percentage.

## Example Output

### System Information
