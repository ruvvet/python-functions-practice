def does_key_exist(obj, key):
    return True if key in obj.keys() else False


obj1 = {"company": 'General Assembly',
        "course": 'Software Engineering Immersive'}

print(does_key_exist(obj1, "course"))
