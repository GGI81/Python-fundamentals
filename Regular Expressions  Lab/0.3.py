import re

pattern = r"(?P<day>\d{2})(?P<separator>[-./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
text = input()

result = re.finditer(pattern, text)

for date in result:
    current_date = date.groupdict()
    print(f"Day: {current_date['day']}, Month: {current_date['month']}, Year: {current_date['year']}")