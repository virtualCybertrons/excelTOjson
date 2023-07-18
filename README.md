# VC Dev Essentials

VC Dev Essentials is a collection of essential tools and libraries for developers, designed to streamline the development process and enhance productivity.

## Features

- Excel to JSON Converter: Convert Excel files into JSON format with a user-friendly interface.

## Installation

To use the Excel to JSON Converter, please follow the installation instructions below based on your operating system.

### Prerequisites

- Python 3.6 or above
- pip package manager

### Ubuntu-based systems

1. Install Python:
   - Check if Python is already installed by running the following command in the terminal:
    
     python3 --version
    
   - If Python is not installed, you can install it using the following command:
    
     sudo apt-get install python3
    

2. Install pip:
   - Check if pip is already installed by running the following command in the terminal:
    
     pip3 --version
    
   - If pip is not installed, you can install it using the following command:
    
     sudo apt-get install python3-pip
    

3. Install Tkinter:
   - Install the Tkinter package using the following command:
    
     sudo apt-get install python3-tk
    

4. Clone or download this repository to your local machine.

5. Open a terminal and navigate to the project directory.

6. Create a new virtual environment (optional):
   - Create a new directory for your project (if not already created) and navigate to it in the terminal.
   - Create a new virtual environment using the following command:
    
     python3 -m venv venv
    
   - Activate the virtual environment using the command:
    
     source venv/bin/activate
    

7. Install the required packages:
   - Ensure that you have a `requirements.txt` file in the project directory with the necessary dependencies (including `pandas`, `numpy`, `tk`, and `openpyxl`).
   - Run the following command to install the dependencies using pip:
    
     pip install -r requirements.txt
    

## Usage

1. Open a terminal and navigate to the project directory.

2. Activate the virtual environment (if you created one) using the command:

    source venv/bin/activate


3. Run the following command to start the tool:

    python script.py


4. The tool will launch, and a window titled "Excel to JSON Converter" will appear.

5. Click the "Select Excel File" button to choose an Excel file using the file dialog.

6. In the "Select Key and Value Columns" window, select the desired key and value columns by checking the corresponding checkboxes.

7. Click the "Process Excel" button to convert the Excel file to JSON format.

8. Choose a filename and location to save the generated JSON file using the file dialog.

9. The JSON file will be saved with the selected columns as key-value pairs.

## Troubleshooting

- If you encounter any issues or errors during installation or execution, please make sure you have followed the installation steps correctly and that you have the necessary dependencies installed.

- If you face any further problems, feel free to contact the author or open an issue in the GitHub repository.

## Contributions

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
