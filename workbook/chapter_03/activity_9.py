def format_customer(name, surname, location=None):
    full_name = f'{name} {surname}'
    if location:
        return f'{full_name} ({location})'
    else:
        return f'{full_name}'

print(format_customer('John', 'Smith', location="California"))
print(format_customer('Maria', 'Shmidt'))