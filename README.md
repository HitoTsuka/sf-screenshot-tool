# SF Screenshot Tool
The Salesforce Screenshot Tool is a Python script designed to automatically capture screenshots of specified Salesforce pages, organize them by date, and save them efficiently. 
This tool is especially useful for tasks requiring regular screenshots of Salesforce dashboards or reports. It uniquely captures a full-page screenshot first and then crops it to the dimensions of a specified element using the element's coordinates for precise extraction.

## Features
Captures screenshots of specific elements within Salesforce pages.
First takes a full-page screenshot, then crops it based on the coordinates of the specified Salesforce element.
Automatically organizes screenshots into folders by date.
Manages the storage of screenshots efficiently.

## Getting Started
Follow these steps to get the project up and running on your local machine.

### Prerequisites
You must have Python installed on your machine. Additionally, the following Python libraries are required:
- selenium
- Pillow
- tkinter

These libraries can be installed using the following command:

```
pip install selenium Pillow
```
### Installation
1. Clone or download this repository.
```
git clone https://github.com/HitoTsuka/sf-screenshot-tool.git
cd sf-screenshot-tool
```
2. Install the required libraries.
```
pip install -r requirements.txt
```

### Usage
To run the script, use the following command:
```
python src/sf_screenshot.py
```

### Configuration
To customize how the script operates, adjust the settings within src/utils.py.
For example, you can change the URLs or identifiers of the Salesforce elements from which screenshots are to be taken.

## Author
HitoTsuka
