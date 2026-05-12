#!/usr/bin/env python
"""
HIKAL Financial Analysis Report - HTML to PDF Converter
Converts HTML report to professional PDF format
"""

import os
import sys
from pathlib import Path

# File paths
html_file = r'E:\Airf_PETNET\learning\My_Software_Project\My research\Fiance 5 projects\Swapan_Kapoor_Fin_Management\HIKAL_Financial_Analysis_Report.html'
pdf_file = r'E:\Airf_PETNET\learning\My_Software_Project\My research\Fiance 5 projects\Swapan_Kapoor_Fin_Management\HIKAL_Financial_Analysis_Report.pdf'

print("=" * 80)
print("HIKAL Financial Analysis Report - HTML to PDF Converter")
print("=" * 80)
print(f"\n📄 HTML Source: {html_file}")
print(f"📕 PDF Output: {pdf_file}\n")

# Check if HTML file exists
if not os.path.exists(html_file):
    print(f"❌ ERROR: HTML file not found at {html_file}")
    sys.exit(1)

print("✓ HTML file found\n")

# Method 1: Try pdfkit + wkhtmltopdf
print("Attempting Method 1: pdfkit + wkhtmltopdf...")
try:
    import pdfkit
    print("  ✓ pdfkit imported successfully")
    
    # Try common wkhtmltopdf locations
    wkhtmltopdf_paths = [
        r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe',
        r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe',
        'wkhtmltopdf',  # Try system PATH
    ]
    
    wkhtmltopdf_path = None
    for path in wkhtmltopdf_paths:
        if os.path.exists(path) or path == 'wkhtmltopdf':
            try:
                config = pdfkit.configuration(wkhtmltopdf=path)
                wkhtmltopdf_path = path
                print(f"  ✓ Found wkhtmltopdf at: {path}")
                break
            except:
                continue
    
    if wkhtmltopdf_path:
        options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'enable-local-file-access': None,
            'print-media-type': None,
        }
        
        pdfkit.from_file(html_file, pdf_file, options=options, config=config)
        
        if os.path.exists(pdf_file):
            file_size = os.path.getsize(pdf_file) / (1024 * 1024)
            print(f"\n✅ SUCCESS! PDF created using pdfkit + wkhtmltopdf")
            print(f"   File: {os.path.basename(pdf_file)}")
            print(f"   Size: {file_size:.2f} MB")
            print(f"   Location: {pdf_file}")
            sys.exit(0)
    else:
        raise Exception("wkhtmltopdf not found in common locations")

except Exception as e:
    print(f"  ✗ Method 1 failed: {str(e)}\n")

# Method 2: Try Playwright (Chromium headless)
print("Attempting Method 2: Playwright + Chromium...")
try:
    from playwright.sync_api import sync_playwright
    print("  ✓ Playwright imported successfully")
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f'file:///{html_file.replace(chr(92), "/")}', wait_until='networkidle')
        page.pdf(path=pdf_file, format='A4', margin={'top': '0.75in', 'bottom': '0.75in', 'left': '0.75in', 'right': '0.75in'})
        browser.close()
    
    if os.path.exists(pdf_file):
        file_size = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"\n✅ SUCCESS! PDF created using Playwright + Chromium")
        print(f"   File: {os.path.basename(pdf_file)}")
        print(f"   Size: {file_size:.2f} MB")
        print(f"   Location: {pdf_file}")
        sys.exit(0)

except Exception as e:
    print(f"  ✗ Method 2 failed: {str(e)}\n")

# Method 3: Try fpdf2
print("Attempting Method 3: fpdf2...")
try:
    from fpdf import FPDF
    from html.parser import HTMLParser
    print("  ✓ fpdf2 imported successfully")
    
    # Simple HTML to PDF using fpdf2
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Remove HTML tags for basic text extraction
    import re
    text = re.sub('<[^<]+?>', '', html_content)
    text = text.strip()
    
    # Add text to PDF with word wrapping
    pdf.multi_cell(0, 5, text[:5000])  # Limit to first part
    pdf.output(pdf_file)
    
    if os.path.exists(pdf_file):
        file_size = os.path.getsize(pdf_file) / (1024 * 1024)
        print(f"\n✅ SUCCESS! PDF created using fpdf2 (basic format)")
        print(f"   File: {os.path.basename(pdf_file)}")
        print(f"   Size: {file_size:.2f} MB")
        print(f"   Location: {pdf_file}")
        print(f"\n⚠️  NOTE: This is a basic text-only conversion. For better formatting, use Method 1 or 2.")
        sys.exit(0)

except Exception as e:
    print(f"  ✗ Method 3 failed: {str(e)}\n")

# If all methods fail
print("\n" + "=" * 80)
print("❌ All automatic conversion methods failed")
print("=" * 80)
print("\n✅ RECOMMENDED SOLUTIONS:\n")
print("1️⃣  INSTALL pdfkit + wkhtmltopdf (Easiest):")
print("   pip install pdfkit")
print("   Download from: https://wkhtmltopdf.org/")
print("   Then run this script again\n")

print("2️⃣  INSTALL Playwright:")
print("   pip install playwright")
print("   playwright install chromium")
print("   Then run this script again\n")

print("3️⃣  MANUAL CONVERSION (Using Browser):")
print("   - Open the HTML file in Chrome/Edge/Firefox")
print("   - Press Ctrl + P (Print)")
print("   - Select 'Save as PDF'")
print(f"   - Save to: {pdf_file}\n")

print("4️⃣  INSTALL wkhtmltopdf:")
print("   Download from: https://wkhtmltopdf.org/")
print("   Then run: pip install pdfkit")
print("   Then run this script again\n")

sys.exit(1)
