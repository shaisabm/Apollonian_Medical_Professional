import json

# New JSON object to append
new_data = {
    "name": "Dr. John Doe",
    "bio": "A clinical psychologist with over 10 years of experience.",
    "category": "clinical psychologist"
}

# Read existing data from the file
with open('responses.json', 'r') as file:
    data = json.load(file)

# Append the new data
data.append(new_data)

# Write the updated data back to the file
with open('responses.json', 'w') as file:
    json.dump(data, file, indent=4)