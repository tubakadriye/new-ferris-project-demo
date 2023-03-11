from ferris_ef import context

my_last_state = context.state.get() # returns a state previously set
some_value = my_last_state.get('key')
context.state.put('Key','Value')