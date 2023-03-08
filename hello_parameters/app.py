from ferris_ef import context


username = context.params.get('sample_name')
print(f"Incoming Parameter: {username}")