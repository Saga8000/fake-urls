# 🔐 LinkShield – Web-Based Fake URL Blocker System

## 📌 Project Overview

LinkShield is a **Web-Based Fake URL Blocker System** designed to protect users from accessing **fake, phishing, and malicious websites**. The system verifies user-entered URLs against a **blacklist of known malicious URLs** generated from a real phishing dataset.

If a URL is identified as malicious, access is blocked. If the URL is not found in the blacklist, the system informs the user that the website appears safe and provides an option to proceed.

This project is implemented **without using Machine Learning or rule-based techniques**, making it simple, efficient, and suitable for academic purposes.

---

## 🎯 Objectives

* To detect and block known fake or phishing URLs
* To provide a secure and user-friendly web interface
* To demonstrate blacklist-based URL filtering using real datasets
* To allow user-controlled navigation without automatic redirection

---

## 🧩 Existing System

In the existing system:

* Users rely on **manual judgment** to identify fake websites
* There is no simple web-based phishing URL checker for common users
* Most existing solutions require **complex ML models or browser extensions**
* Non-technical users find it difficult to verify website authenticity

### Limitations of Existing System

* No centralized blacklist-based URL checking
* High complexity and technical dependency
* Limited usability for normal users

---

## 🚀 Proposed System

The proposed system introduces a **Web-Based Fake URL Blocker** that:

* Uses a **JSON blacklist** generated from a real phishing dataset
* Blocks URLs labeled as malicious
* Allows safe URLs to proceed only after user confirmation
* Provides a modern, interactive, and secure user interface

### Key Features

* Dataset-driven fake URL detection
* No database required
* No machine learning or rule-based logic
* Manual “Proceed to Website” option for safe URLs
* Clean and professional UI with branding and favicon

---

## 🛠️ Tools and Technologies Used

### Programming Languages

* **Python** – Backend logic and dataset processing
* **HTML** – Web page structure
* **CSS** – Styling and responsive UI
* **JavaScript** – Loader animation and interactivity

### Frameworks & Libraries

* **Flask** – Lightweight Python web framework
* **Jinja2** – Template engine (used with Flask)

### Data Handling

* **CSV Dataset** – Phishing dataset (Kaggle)
* **JSON** – Blacklist storage format

### Development Tools

* **Visual Studio Code** – Code editor
* **Python Virtual Environment (venv)**

---

## 📂 Project Structure

```
fake url/
│
├── app.py
├── blacklist.json
├── convert_dataset.py
│
├── dataset/
│   └── phishing_dataset.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── style.css
    ├── logo.png
    └── favicon.ico
```

---

## 🔄 Methodology

### Step 1: Dataset Collection

A publicly available **phishing URL dataset** was collected containing both:

* Benign URLs
* Malicious URLs

### Step 2: Dataset Pre-processing

A Python script (`convert_dataset.py`) extracts URLs labeled as **malicious** and stores them in a JSON file (`blacklist.json`).

### Step 3: Blacklist-Based Checking

* User submits a URL
* The system checks the URL against the blacklist
* If found → Access blocked
* If not found → URL marked as safe

### Step 4: User Interface Handling

* Blocked URLs show a warning page
* Safe URLs display a “Proceed to Website” button
* No automatic redirection is performed

---

## ⚙️ System Workflow

1. User enters a URL
2. URL is compared with blacklist
3. If malicious → Access blocked
4. If safe → User decides whether to proceed

---

## 🧪 Testing

* Tested using fake URLs from the dataset → Successfully blocked
* Tested using genuine websites → Allowed with user confirmation
* UI tested for navigation, buttons, and responsiveness

---

## ⚠️ Limitations

* The system blocks only **known fake URLs**
* Newly created phishing URLs cannot be detected
* No real-time blacklist updates

---

## 🔮 Future Enhancements

* Integration with real-time phishing feeds
* Rule-based or machine learning detection
* Admin dashboard for blacklist updates
* Browser extension integration

---

## 📚 Conclusion

The LinkShield system successfully demonstrates a **simple, effective, and user-friendly** approach to blocking fake URLs using a blacklist method. By leveraging real datasets and avoiding complex algorithms, the project achieves reliability, clarity, and academic suitability.

---

## 👨‍🎓 Academic Declaration

This project is developed purely for **educational purposes** and does not claim to block all phishing websites in real-world environments.

---

## 🏁 Viva Reference Statement

> “The project uses a blacklist-based approach with a real phishing dataset to block known fake URLs while allowing user-controlled access to safe websites.”
