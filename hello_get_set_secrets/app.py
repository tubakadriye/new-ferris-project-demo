from ferris_ef import context

print('hello dx')

print("------- Get Secret -------")
print(context.secrets.get("test_secret_1"))

print("------- Set Secret -------")
print(context.secrets.set(name = "test_secret_4", value = {"pfkey":"platform val"}, context = "platform"))
print(context.secrets.set("test_secret_4", {"prjkey":"project val"}, "project"))

print("------- Get Secret test_secret_4 -------")
print(context.secrets.get("test_secret_4"))


