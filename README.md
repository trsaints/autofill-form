# Autofill Form

This project is a Python script that automates the process of filling out a form. It's intended for users who need to fill out the same form multiple times with the same or similar data.

> **Note:** This script is designed to work on Windows platforms only.

## Installation

To install the necessary dependencies for this project, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To use the script, run the following command:

```bash
py autofill_form.py -p [PID]
```
Where `[PID]` stands for the Process ID of the program you want to automate


## How it works 

Autofill Forms works as a configuration as a code, where the user declares the commands to be executed by the program in a Comma-Separated Value (CSV) file.

A `commands.csv` file has to be created at the root of the project as it is the base file where commands will be interpreted from.

The CSV columns are defined as follows:

| Column Name | Description |
|-------------|-------------|
| Key         | The key or text to be typed by the program             |
| Presses     | How many times the key or text has to be pressed       |
| Sleep       | A countdown timer to be executed after the key pressed |
| Interval    | A countdown timer to be executed for each key pressed given a text content         |

An valid example would be as the following:

```csv
key,presses,sleep,interval
enter,3,0,0
down,1,0,0
tab,4,0,0
capslock,1,1,0
tab,3,0,0
enter,1,1,0
tab,3,0,0
hello,1,1,0.25
```

> **Note:** The first line at the CSV file has to a label as the given example, once the program is designed to ignore the first line. Passing actual content to be interpreted will cause the program to ignore it.
