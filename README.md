# BitcoinDataVisualizer

## Overview

BitcoinDataVisualizer is a Python project designed to visualize historical Bitcoin price data. It uses `yfinance` to fetch historical Bitcoin data and `plotly` to create interactive graphs that highlight price peaks and troughs.

## Setup Instructions

Follow these steps to set up and run the project on Ubuntu 22.04:

1. **Update and Upgrade System Packages:**

   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```

2. **Install Python 3 and `pip`:**

   If Python 3 and `pip` are not already installed, you can install them using:

   ```bash
   sudo apt install python3 python3-pip -y
   ```

3. **Install Git (if not already installed):**

   ```bash
   sudo apt install git -y
   ```

4. **Clone the Repository:**

   ```bash
   git clone https://github.com/vitaliy-developer//BitcoinDataVisualizer.git
   cd BitcoinDataVisualizer
   ```

5. **Create a Virtual Environment:**

   ```bash
   python3 -m venv btc_venv
   ```

6. **Activate the Virtual Environment:**

   ```bash
   source btc_venv/bin/activate
   ```

7. **Install the Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

8. **Run the Project:**

   Execute the `analysis.py` script to generate and view the interactive Bitcoin price graph:

   ```bash
   python analysis.py
   ```

## Project Structure

- `analysis.py`: Contains the code for downloading Bitcoin data, processing it, and creating the interactive plot.
- `requirements.txt`: Lists the required Python packages for the project.

## Requirements

- `pandas`
- `plotly`
- `yfinance`

## Acknowledgments

- [Plotly](https://plotly.com/python/) for creating interactive visualizations.
- [yfinance](https://pypi.org/project/yfinance/) for accessing financial data.

## Screenshots
![alt text](https://github.com/vitaliy-developer/BitcoinDataVisualizer/blob/main/image.png)
