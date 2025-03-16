# Motorcycle Search Engine

## Overview
The Motorcycle Search Engine is a sleek application that leverages the Ninja API to help you discover motorcycles based on your preferences. Search by make, model, year, or type and view all matching results in a neatly organized table. This tool also offers one-click export functionality to save your findings in Excel format.

## Key Features
- **Advanced Search Filters**: Find exactly what you're looking for with customizable parameters
- **Intuitive User Interface**: Clean design for effortless navigation
- **Excel Export**: Easily download and share your search results
- **Organized Data Display**: View all motorcycle details in a sortable table format

## Requirements
To run this application, you'll need:
- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## Installation Guide

### Step 1: Get the Code
```bash
# Clone the repository
git clone https://github.com/Alejo-IA/Api-motorcycle.git

# Navigate to the project directory
cd Api-motorcycle
```

### Step 2: Set Up Your API Key
Create a `.env` file in the root directory with your Ninja API key:
```
API_NINJA_KEY=your_api_key_here
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage Instructions

### Starting the Application
```bash
python run.py
```

### Using the Interface
1. **Search**: Enter your desired motorcycle specifications:
   - Make (e.g., Honda, Yamaha)
   - Model (e.g., CBR, R1)
   - Year (e.g., 2022)
   - Type (e.g., Sport, Cruiser)
2. **View Results**: Click "Search" to display matching motorcycles
3. **Reset Filters**: Use "Clear" to start a new search
4. **Export Data**: Click "Download Excel" to save results to the data folder

## Project Structure
```
motorcycle-search/
├── .env                 # API credentials (not included in repository)
├── requirements.txt     # Required libraries
├── run.py               # Application launcher
├── src/                 # Source code
│   ├── main.py          # Main entry point
│   ├── config.py        # Configuration settings
│   ├── ui/              # User interface components
│   │   └── app.py       # Interface implementation
│   └── api/             # API communication layer
│       └── motorcycles.py  # Motorcycle API functions
└── data/                # Excel export directory
```

## Developer Information
This project is maintained by [Alejo-IA](https://github.com/Alejo-IA).

---

## Troubleshooting

If you encounter any issues:
- Verify your API key is correctly set in the `.env` file
- Ensure all dependencies are properly installed
- Check your internet connection for API communication

## License
This project is available for public use and modification.