import requests
from collections import defaultdict

repos = requests.get(f"https://api.github.com/users/yawsf1/repos").json()

language_totals = defaultdict(int)

for repo in repos:
    langs = requests.get(repo["languages_url"]).json()
    for lang, count in langs.items():
        language_totals[lang] += count

total_bytes = sum(language_totals.values())
for lang, count in language_totals.items():
    percent = (count / total_bytes) * 100
    print(f"{lang}: {percent:.2f}%")
