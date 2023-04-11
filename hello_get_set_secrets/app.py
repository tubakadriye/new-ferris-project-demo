from ferris_ef import context

print('hello dx')

print("------- Get Secret -------")
print(context.secrets.get("test_secret_1"))

print("------- Set Secret -------")
print(context.secrets.set(name = "test_secret_4", value = {"test_secret_4":"55"}, context = "platform"))
print(context.secrets.set("test_secret_5", {"test_secret_5":"17"}, "project"))

print("------- Get Secret test_secret_4 -------")
print(context.secrets.get("test_secret_4"))


print("------- Get Secret test_secret_5 -------")
print(context.secrets.get("test_secret_5"))

