for key in menu:                      # Keys only
    print(key)

for value in menu.values():           # Values only
    print(value)

for key, value in menu.items():       # Both at once
    print(f"{key}: {value}")