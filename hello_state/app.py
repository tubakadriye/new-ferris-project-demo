from ferris_cli import context

my_state = context.state.get() # returns a state previously set
some_value = my_last_state.get('key')
context.state.put('Key','Value')