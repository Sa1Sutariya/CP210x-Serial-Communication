# CP210x Serial Communication

![GitHub repo size](https://img.shields.io/github/repo-size/Sa1Sutariya/send_hex_to_microcontroller)
![GitHub stars](https://img.shields.io/github/stars/your-username/your-repo-name?style=social)
![GitHub forks](https://img.shields.io/github/forks/your-username/your-repo-name?style=social)
![GitHub issues](https://img.shields.io/github/contributors/badges/shields)
![GitHub pull requests](https://img.shields.io/github/issues-pr/your-username/your-repo-name)

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
