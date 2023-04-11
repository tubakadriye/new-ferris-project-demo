from ferris_ef import context

print("------- Get Service Info -------")
print(context.package.name)
print(context.package.id)

print("------- Get Service State -------")
print( context.state.get())


print("------- Update Service State -------")
context.state.put("Name", "set_service")
context.state.put("Trigger Event", {"reference_id": "19"})


print("------- Get Service State -------")
last_state = context.state.get()
print("last_state", last_state)

name = last_state.get('Name')
print("Name", name)
