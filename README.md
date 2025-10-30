# SonicWall Captive Portal Auto-Login

A Python script that automates login to SonicWall captive portals using Selenium WebDriver (Firefox). Use this only on networks you own or are authorized to test.

---

## 🚀 Features

- **Automated Login** — fills credentials and submits the portal form.
- **Random Credential Selection** — picks credentials at random from a pool for testing.
- **Browser Automation** — uses Selenium with Firefox (GeckoDriver).
- **Smart Waiting** — explicit waits for element availability.
- **Basic Error Handling** — success/failure detection and retries.

---

## 📋 Prerequisites

- Python 3.7+
- Firefox browser installed
- GeckoDriver for Firefox (compatible version)
- Access to the SonicWall captive portal network

---

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/sonicwall-auto-login.git
cd sonicwall-auto-login
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Download GeckoDriver**

- Get it from Mozilla's GeckoDriver releases and add it to your system `PATH` or place it in the project root.

4. **Create credentials file**

Create `credentials.txt` in the project root. Each line: `username,password` (comma-separated).

Example `credentials.txt`:

```
user1,password123
user2,pass456
john_doe,securepass
```

---

## 🛠️ Usage

1. Update the target URL in the script if needed:

```python
# inside sonicwall_login.py
driver.get("https://your-sonicwall-portal-url")
```

2. Run the script:

```bash
python sonicwall_login.py
```

What it does:
- Launches Firefox
- Navigates to the captive portal
- Selects random credentials from `credentials.txt`
- Enters username & password
- Submits the form and waits for confirmation

---

## 📁 File structure

```
sonicwall-auto-login/
├── sonicwall_login.py    # Main automation script
├── credentials.txt       # Credentials (create this) - DO NOT commit
├── geckodriver*          # GeckoDriver binary (download separately)
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

---

## ⚙️ Configuration

### Customizing selectors

If the portal's HTML changes, update selectors in the script (example):

```python
# Username field selector
username_field = driver.find_element(By.CSS_SELECTOR, '[placeholder="Enter your username..."]')

# Password field selector
password_field = driver.find_element(By.CSS_SELECTOR, '[placeholder="Enter your password..."]')
```

### Adjusting wait times

Increase waits for slow networks:

```python
WebDriverWait(driver, 30)  # increase from 15s if needed
```

---


---

## 🐛 Troubleshooting

**GeckoDriver not found**
- Ensure GeckoDriver is in `PATH` or the project directory.
- Download the correct OS version.

**Element not found**
- Verify the portal URL is correct.
- Update CSS selectors to match the portal.
- Increase explicit wait time.

**SSL certificate errors**
- Ensure the portal's HTTPS certificate is valid.
- For self-signed certs, add an exception or use a testing certificate.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/AmazingFeature`
3. Commit changes: `git commit -m "Add AmazingFeature"`
4. Push and open a Pull Request

Please keep credentials out of commits.

---

## 📄 License

This project is available under the **MIT License**. See `LICENSE` for details.

---
