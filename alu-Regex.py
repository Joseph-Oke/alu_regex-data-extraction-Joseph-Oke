import re

# 1. Email Extraction
def extract_email(text):
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return re.findall(email_regex, text)

# 2. URL Extraction
def extract_url(text):
    url_regex = r"(https?:\/\/[^\s]+)"
    return re.findall(url_regex, text)

# 3. Phone Number Extraction
def extract_phonenumber(text):
    phone_regex = r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})"
    return re.findall(phone_regex, text)

# 4. Time Extraction (12h & 24h)
def extract_time(text):
    time_regex = r"\b((1[0-2]|0?[1-9]):[0-5][0-9]\s?(AM|PM|am|pm)?|([01]?[0-9]|2[0-3]):[0-5][0-9])"
    matches = re.findall(time_regex, text)
    return [m[0] for m in matches]

# 5. HTML Tag Extraction
def extract_html_tags(text):
    html_regex = r"<[^>]+>"
    return re.findall(html_regex, text)

# Sample Text
sample_text = """
Email: j.oke@alustudent.com, enitanokejoseph@gmail.com
URL: https://www.example.com, https://www.apple.com
Phone: 09035795891, 08166220094,
Time: 14:30, 2:30 PM, 09:15 am
HTML: <p>Paragraph</p> <div class="container">Content</div> <img src="pic.jpg" alt="img">
"""

# Running the Extraction
print("Emails:", extract_email(sample_text))
print("URLs:", extract_url(sample_text))
print("Phone Numbers:", extract_phonenumber(sample_text))
print("Times:", extract_time(sample_text))
print("HTML Tags:", extract_html_tags(sample_text))
