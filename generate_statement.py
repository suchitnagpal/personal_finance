from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import random
from datetime import datetime, timedelta

# Output file
pdf_path = "sample_chase_statement.pdf"

# Expanded category-to-merchant map
categories = {
    "Groceries": ["Whole Foods", "Trader Joe's", "Walmart", "Kroger", "Costco"],
    "Dining": ["Starbucks", "McDonald's", "Chipotle", "Panera Bread", "Domino's", "Subway", "Chick-fil-A"],
    "Transport": ["Uber", "Lyft", "Shell Gas", "ExxonMobil", "Chevron", "Toll Booth"],
    "Subscriptions": ["Netflix", "Spotify", "YouTube Premium", "Hulu", "Amazon Prime", "Apple Music"],
    "Shopping": ["Amazon", "Target", "Best Buy", "Apple Store", "eBay", "Etsy", "Shein"],
    "Healthcare": ["CVS Pharmacy", "Walgreens", "Health Clinic", "Dental Checkup", "Optometrist"],
    "Utilities": ["ConEdison", "Verizon", "T-Mobile", "Comcast", "AT&T Internet", "National Grid"],
    "Travel": ["Delta Airlines", "Hilton Hotels", "Airbnb", "Southwest Airlines", "Marriott", "Uber"],
    "Education": ["Coursera", "edX", "Udemy", "Skillshare"],
    "Entertainment": ["AMC Theaters", "Fandango", "Concert Ticket", "Theme Park"],
    "Others": ["Donation", "Gym Membership", "Parking Fee", "Post Office", "Dry Cleaners"]
}

# Generate transactions
start_date = datetime(2025, 7, 1)
transactions = []

for _ in range(100):
    txn_date = start_date + timedelta(days=random.randint(0, 30))
    category = random.choice(list(categories.keys()))
    merchant = random.choice(categories[category])
    amount = round(random.uniform(5, 400), 2)

    if random.random() < 0.08:
        # Simulate payment or refund
        merchant = "Payment Received"
        amount = -round(random.uniform(100, 1000), 2)

    transactions.append((txn_date.strftime("%m/%d/%Y"), merchant, category, amount))

# Sort by date
transactions.sort(key=lambda x: datetime.strptime(x[0], "%m/%d/%Y"))

# Create PDF
c = canvas.Canvas(pdf_path, pagesize=LETTER)
width, height = LETTER

# Header
c.setFont("Helvetica-Bold", 16)
c.drawString(40, height - 40, "Chase Credit Card Statement")

c.setFont("Helvetica", 10)
y = height - 60
header_info = [
    ("Account Holder", "Jane Doe"),
    ("Account Number", "**** 5678"),
    ("Statement Period", "07/01/2025 - 07/31/2025"),
    ("Statement Date", "08/01/2025"),
    ("Payment Due Date", "08/25/2025"),
    ("Credit Limit", "$10,000.00"),
    ("Available Credit", "$8,500.00")
]
for label, value in header_info:
    c.drawString(40, y, f"{label}: {value}")
    y -= 14

# Table headers
y -= 10
c.setFont("Helvetica-Bold", 10)
c.drawString(40, y, "Date")
c.drawString(110, y, "Description")
c.drawString(300, y, "Category")
c.drawRightString(550, y, "Amount")
c.line(40, y - 2, 550, y - 2)
y -= 16

# Transactions
c.setFont("Helvetica", 9)
for date, desc, cat, amt in transactions:
    if y < 60:
        c.showPage()
        y = height - 60
        c.setFont("Helvetica-Bold", 10)
        c.drawString(40, y, "Date")
        c.drawString(110, y, "Description")
        c.drawString(300, y, "Category")
        c.drawRightString(550, y, "Amount")
        c.line(40, y - 2, 550, y - 2)
        y -= 16
        c.setFont("Helvetica", 9)
    c.drawString(40, y, date)
    c.drawString(110, y, desc[:35])
    c.drawString(300, y, cat)
    amt_str = f"-${abs(amt):,.2f}" if amt < 0 else f"${amt:,.2f}"
    c.drawRightString(550, y, amt_str)
    y -= 14

c.save()
print(f"✅ PDF saved as {pdf_path}")
