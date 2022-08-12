import re

# print("Hello, World!")

with open("assets/existing-contacts.txt") as f:
    file_text = f.read()

# attribution in README.md
pattern = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

em_patt = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

phone_nums = re.findall(pattern, file_text)
emails = re.findall(em_patt, file_text)

report = f"Found {len(phone_nums)} phone numbers."
print(report)

email_report = f"Found {len(emails)} email addresses."
print(email_report)

with open("assets/existing-contacts.txt", 'a') as e:
    e.write(str(phone_nums))
    e.write(str(emails))