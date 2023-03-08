from ferris_ef import context



hostname = context.params.get('sample_hostname')
print(f"Incoming Parameter: {hostname}")