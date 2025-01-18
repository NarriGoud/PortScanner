# Port Scanner

This is a Python-based port scanner that scans all ports (1 to 65535) for a given target host IP address. It utilizes multi-threading to speed up the scanning process, making it more efficient for large ranges of ports.

## Features
- Scans ports from 1 to 65535.
- Efficient scanning with 100 concurrent threads.
- Timeout set to 0.5 seconds per port to optimize speed.
- Identifies and reports open ports.

## Prerequisites

- Python 3.6 or higher.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/port-scanner.git
   cd port-scanner
