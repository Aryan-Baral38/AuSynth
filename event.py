

events = {}
def event_handler(event_type : str, data):
    #log_event(event_type, data)
    if event_type == "keyPress":
        key_pressed(data)

    
    if event_type == "KeyRelease":
        key_released(data)

