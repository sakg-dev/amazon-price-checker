# Amazon Price Tracker

A simple, automated Amazon price tracker that monitors products and sends you an email alert when the price drops below your target.

Built with a real goal in mind: making every dollar count and stretching a Hack Club grant far enough to afford a laptop.

---

## Features

* Track multiple products using ASINs
* Automatically converts your USD budget into INR (or other currencies)
* Fetches live Amazon prices using ScraperAPI
* Sends instant email notifications when prices drop
* Can run locally or be automated with GitHub Actions

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sakg-dev/amazon-price-checker
cd amazon-price-checker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
USD_AMT=your_budget_in_usd
SCRAPERAPI_KEY=your_api_key
SEND_EMAIL=sender_email
USER_EMAIL=receiver_email
FROM_EMAIL_PASS=sender_email_app_password
```

### 4. Add products to track

`products.json` should be an array of ASINs (Amazon product IDs).

Example:

```json
[
  "B0XXXXXXX",
  "B0YYYYYYY"
]
```

### 5. Run the tracker

```bash
python main.py
```

---

## How It Works

1. Fetches product price data using ScraperAPI
2. Converts your USD budget into INR (or configured currency)
3. Compares the current price with your target
4. Sends an email alert if the price drops below your threshold

---

## Known Issues

* Amazon scraping may occasionally fail depending on API reliability
* Price fluctuations or page structure changes may affect accuracy

---

## Future Improvements

* Robust error handling
* Logging system for tracking runs and failures
* Support for additional marketplaces
* Web-based UI dashboard

---

## Motivation

This project was built to solve a practical problem: tracking laptop prices efficiently while working within a tight budget. Instead of manually checking prices, this tool automates the process and notifies you when it matters.

---

## License

MIT License
