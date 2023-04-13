from ferris_ef import context

print('hello dx')

print("------- Get Service Info -------")
print(context.package.name)
print(context.package.id)

# code from hello_state

my_last_state = context.state.get() # returns a state previously set

print("my last state", my_last_state)
some_value = my_last_state.get('Key')
context.state.put('New Key','New Value')
print("some value", some_value)
my_current_state = context.state.get()
print("my_current_state", my_current_state)