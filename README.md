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

```bash
python cp210x_communication.py
```

1. The script will detect the CP210x port, send a predefined command, and display the received data in raw and hexadecimal formats.
2. Press Enter to continue reading data.
3. If no CP210git checkout -b feature/your-feature-name
x port is found, the script will keep trying to find it and display a list of available ports.

## Contributing

Contributions are welcome! If you'd like to improve this script or fix any issues, please follow these steps:
1. Fork the repository.
2. Create a new branch with a descriptive name:

```bash
git checkout -b feature/your-feature-name
```
3. Make your changes and commit them:
```bash
git commit -m 'Add some feature'
```
4. Push your changes to your fork:

```bash
git push origin feature/your-feature-name
```

5. Create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


```css
Make sure to replace `your-username` and `your-repo-name` with your actual GitHub username and repository name. Also, ensure you have a `LICENSE` file in your repository if you want to use the MIT License, or update the license section accordingly.
```
