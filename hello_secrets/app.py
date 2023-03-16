from ferris_ef import get_secret, get_param

print(f"DB NAME: {get_secret('DB_NAME')}")
print(f"DB PASS: {get_secret('DB_PASS')}")

print(f"service Name: {get_param('service_name')}")