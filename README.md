# Automated Testing for iamdave.ai

## ✅ Project Overview
This project contains automated tests for the website https://www.iamdave.ai using Python:
- **UI Automation** with Selenium
- **Load Testing** using Locust (optional)

---

## ✅ How to Run the Tests

### 1️⃣ UI Automation Tests
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the UI tests:
    ```bash
    python tests/ui_tests.py
    ```

The script will:
- Open the website
- Validate the page title
- Verify the main heading
- Navigate to the Contact page
- Check if the footer logo is present

### 2️⃣ Load Testing (Optional)
1. Run Locust with:
    ```bash
    locust -f load_test.py --host https://www.iamdave.ai
    ```

2. Open the Locust UI in your browser:
    ```
    http://localhost:8089
    ```

3. Set the number of users (e.g., 5–10) and spawn rate, then click **Start swarming**.

---

## ✅ Dependencies

All dependencies are listed in `requirements.txt`:

