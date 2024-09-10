# Google Form Auto-Filler Script

This project automates the process of filling out a Google Form using information from a CSV file. It utilizes Selenium WebDriver for browser automation and Pandas to manage the CSV data.

## Features

- Automatically fills out form fields including Full Name, Preferred Method of Communication, Skills, Employment Status, and Meeting Date.
- Interacts with radio buttons, checkboxes, dropdown menus, and text input fields.
- Scrolls through the form and submits it using Selenium's ActionChains.
- Handles dynamic elements with `WebDriverWait` to ensure page elements load before interaction.

## Prerequisites

To run this project, you'll need:

- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

You can install the required Python packages by running:

```bash
pip install selenium pandas
```

## Setup Instructions
1. Download and install Google Chrome if you haven't already.
2. Download the ChromeDriver that matches your version of Google Chrome from here.
3. Add ChromeDriver to your system's PATH, or specify its location in the script.

## Running the Script
1. Ensure all dependencies are installed.
```
  git clone https://github.com/cyberfantics/google-form
  cd google-form
```
2. Run the script with Python:
   ```
   python main.py
   ```
- The script will open Chrome, navigate to the Google Form, and fill in the details for each row in the CSV file.

## Developer Information

**Developer:** Syed Mansoor ul Hassan Bukhari  
**GitHub:** [CyberFantics](https://github.com/CyberFantics)  
**LinkedIn:** [Mansoor Bukhari](https://www.linkedin.com/in/mansoor-bukhari-77549a264/)  
**Email:** [digital.creator380@gmail.com](mailto:digital.creator380@gmail.com)
