from ferris_ef import context

context.config.get("my_configuration_dictionary")["alias"]

print('hello dx')

print("------- Get Service Config -------")
print(context.config.get("my_configuration_dictionary")["alias"])