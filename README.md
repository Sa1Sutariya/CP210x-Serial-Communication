# CP210x Serial Communication

A Python script for communicating with CP210x USB-to-Serial adapters and displaying received data.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python script is designed for communication with CP210x USB-to-Serial adapters. It allows you to send commands to the connected device and display the received data in both raw and hexadecimal formats. This is useful for debugging and monitoring CP210x devices.

## Prerequisites

Before using this script, ensure you have the following:

- Python 3.x installed on your system.
- The `serial` library for Python. You can install it using pip:

```bash
pip install pyserial
```

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Sa1Sutariya/send_hex_to_microcontroller.git
```

2. Change into the project directory:
```bash
cd send_hex_to_microcontroller
```

## Usage

1. Connect a CP210x USB-to-Serial adapter to your computer.
2. Run the script by executing:

```python
python cp210x_communication.py
```


