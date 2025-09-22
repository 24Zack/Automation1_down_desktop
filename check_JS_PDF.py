import PyPDF2

def check_pdf_for_javascript(pdf_path):
    found_js = False
    suspicious_entries = []

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Look for JavaScript in /Names or /OpenAction or /AA entries
        catalog = reader.trailer["/Root"]

        if "/Names" in catalog and "/JavaScript" in catalog["/Names"]:
            found_js = True
            suspicious_entries.append("JavaScript in /Names")

        if "/OpenAction" in catalog:
            action = catalog["/OpenAction"]
            if isinstance(action, dict) and action.get("/S") == "/JavaScript":
                found_js = True
                suspicious_entries.append("JavaScript in /OpenAction")

        if "/AA" in catalog:
            aa_dict = catalog["/AA"]
            if any(k for k in aa_dict if aa_dict[k].get("/S") == "/JavaScript"):
                found_js = True
                suspicious_entries.append("JavaScript in /AA")

        # Check all pages
        for i, page in enumerate(reader.pages):
            if "/AA" in page:
                aa_dict = page["/AA"]
                if any(k for k in aa_dict if aa_dict[k].get("/S") == "/JavaScript"):
                    found_js = True
                    suspicious_entries.append(f"JavaScript in /AA on page {i + 1}")

    if found_js:
        print("⚠️ JavaScript found in the PDF:")
        for entry in suspicious_entries:
            print(f"  - {entry}")
    else:
        print("✅ No JavaScript detected in the PDF.")

# Example usage
import os
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", "Civilized-to-Death.pdf")
check_pdf_for_javascript(downloads_path)