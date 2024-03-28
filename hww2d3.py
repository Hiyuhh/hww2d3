import re
# 1. Python Regular Expressions Mastery
# Task 1: Code Correction

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-Z|a-z._-]{2,}" , text)
print(emails)

# 2. Python Regular Expressions Deep Dive
# Task 1: Email Extraction Enhancement

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = [email for email in re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text) if 'exclude.com' not in email] 
print(emails)

emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text) # I did two ways to solve the problem
print(emails)

# not sure which way is prefered, but I think the second one is more readable