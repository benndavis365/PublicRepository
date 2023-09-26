favorite_languages = {
  "betty" : "python",
  "johnny" : "html",
  "grace" : "javascript",
  "betty lu" : "c",
  "maple" : "ruby",
}

friends = ["maple", "betty lu", "ralph", "ronny"]

for name in friends:
  if name in favorite_languages.keys():
    print(f"\n{name.title()}, thank you for taking the poll.")
  elif name not in favorite_languages.keys():
    print(f"\n{name.title()}, please take the poll.")