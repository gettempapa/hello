people = [
    {"name": "fred", "country": "USA"},
    {"name": "sally", "country": "UK"},
    {"name": "cornelius", "country": "Norway"}
]

print(sorted(people, reverse=True, key=lambda people: people["country"]))