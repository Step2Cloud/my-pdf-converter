Markdown
# 📄 High-Fidelity PDF to Word Converter

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg.svg)](https://my-pdf-converter-ab5stqhdzbzm4sqxgby2cy.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A privacy-focused, cloud-native web application that converts PDF documents into editable Microsoft Word (.docx) files while maintaining layout integrity.

---

## 🚀 Overview

Most "free" online converters compromise user data by storing files on remote servers. This utility, built by **Step2Cloud Inc.**, utilizes a serverless architecture with **zero-persistence data handling**. Your files are processed in a volatile memory environment and deleted immediately after conversion.

### Key Features:
- **High Fidelity:** Reconstructs complex document schemas (tables, margins, and font styles) using `pdf2docx`.
- **Privacy First:** No database or persistent storage is used. Files exist only during the execution of the conversion script.
- **Modern UI:** Responsive, dark-mode interface built with **Streamlit**.
- **Cloud Native:** Optimized for deployment on Streamlit Cloud or Hugging Face Spaces.

---

## 🛠️ Technical Stack

* **Language:** Python 3.9+
* **UI Framework:** [Streamlit](https://streamlit.io/)
* **Conversion Engine:** [pdf2docx](https://dothinking.github.io/pdf2docx/)
* **Deployment:** GitHub Actions + Streamlit Cloud

---

## 📥 Installation & Local Usage

If you wish to run this tool locally:
Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py
🌐 Deployment
This project is configured for one-click deployment to Streamlit Cloud. Ensure your repository contains:

app.py: The core application logic.

requirements.txt: Necessary Python dependencies.

Website: [Step2Cloud Inc.](https://step2cloud.ca/)
