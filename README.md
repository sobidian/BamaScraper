# Bama.ir Car Data Scraper

A Python script for extracting car information from Bama.ir website.

## 📋 Description

This project is a Python script that extracts detailed car information from vehicle detail pages on Bama.ir website. The script uses `requests` and `BeautifulSoup` libraries to collect required data and save it in JSON format.

## ✨ Features

- Extracts comprehensive car information including:
  - Car brand and model
  - Manufacturing year
  - Price
  - Mileage (kilometers)
  - Fuel type
  - Transmission type
  - Body color
- Output in JSON format
- HTTP request management with proper headers
- Data processing and cleaning of extracted information

## 🛠 Technologies

- **Python 3**
- **BeautifulSoup4** - for HTML parsing
- **Requests** - for HTTP requests
- **JSON** - for data storage

## 🚀 Installation & Usage

1. Install required libraries:
```bash
pip install requests beautifulsoup4
```

2. Run the script:
```bash
python bama_scraper.py
```

## 📊 Sample Output

```json
{
    "model_brand": "Toyota",
    "model_variant": "Land Cruiser Four Door",
    "year": "2013",
    "detailed_model": "6 Cylinder 4.0",
    "gearbox": "Automatic",
    "price": "Negotiable",
    "kilometer": "85,000",
    "fuel_type": "Gasoline",
    "body_color": "Black"
}
```

## 📁 Project Structure

```
bama-scraper/
│
├── bama_scraper.py    # Main script file
├── bama_car_final.json # Sample output file
└── README.md          # This file
```

## ⚠️ Important Notes

- This script is intended for educational purposes only
- Respect website's robots.txt and terms of service
- Consider adding delays between requests to avoid overloading the server
- Web scraping may be subject to legal restrictions in some jurisdictions

## 🔧 Customization

You can modify the script to:
- Extract additional car specifications
- Handle different URL patterns
- Add error handling for missing elements
- Implement pagination for multiple listings

## 📄 License

This project is for educational purposes. Please check Bama.ir's terms of service before using this script.
