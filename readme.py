# Generates a README from a JSON format
# <!-- https://github.com/alexandresanlim/Badges4-README.md-Profile -->
import json

f = open('data.json')
data = json.load(f)

print(data)