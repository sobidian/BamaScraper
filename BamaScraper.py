import json
import requests
from bs4 import BeautifulSoup

url = "https://bama.ir/car/detail-xdj7kins-toyota-camry-gl-2007"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

# عنوان و سال
title = soup.select_one(".bama-ad-detail-title__section h1").text.strip()
model_brand, model_variant = (title.split("،", 1)[0].strip(), title.split("،", 1)[1].strip()) if "،" in title else (title, None)
year = soup.select_one(".bama-ad-detail-title__subtitle").text.strip()

# قیمت و مدل دقیق
price = soup.select_one(".bama-ad-detail-price__price-text").text.strip()
detailed_model_elem = soup.select_one(".bama-ad-detail-title__subtitle-holder span:nth-child(3)")
detailed_model = detailed_model_elem.text.strip() if detailed_model_elem else None

# مشخصات (کیلومتر، سوخت، گیربکس، رنگ)
specs = {"کارکرد": None, "سوخت": None, "گیربکس": None, "رنگ بدنه": None}

for item in soup.select(".bama-vehicle-detail-with-icon > div"):
    try:
        label = item.select_one("span").text.strip()
        value = item.select_one("p").text.strip()
        
        if "کارکرد" in label:
            specs["کارکرد"] = value.replace("km", "").strip()
        elif "سوخت" in label:
            specs["سوخت"] = value
        elif "گیربکس" in label:
            specs["گیربکس"] = value
        elif "رنگ بدنه" in label:
            specs["رنگ بدنه"] = value
    except:
        continue

# اضافه کردن selector جدید برای div:nth-child(4)
additional_info_elem = soup.select_one(".bama-vehicle-detail-with-icon > div:nth-child(4) > p")
additional_info = additional_info_elem.text.strip() if additional_info_elem else None

# ذخیره (با فیلد اضافی)
data = {
    "model_brand": model_brand,
    "model_variant": model_variant,
    "year": year,
    "detailed_model": detailed_model,
    "gearbox": specs["گیربکس"],
    "price": price,
    "kilometer": specs["کارکرد"],
    "fuel_type": specs["سوخت"],
    "body_color": specs["رنگ بدنه"],
    "additional_info": additional_info 
}

with open("bama_car_final.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("ذخیره شد:", data)
