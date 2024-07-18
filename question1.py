# Task 1

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@exclide, user5@newdomain.com"
emails = re.findall(r"(?!\b[A-Za-z0-9._%+-]+@exclude\.com)\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)
