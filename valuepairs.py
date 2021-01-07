def value_pair(obj1, obj2, key):

    return [obj1[key], obj2[key]]


object1 = {"name": 'One', "location": 'Remote', "age": 1}
object2 = {"name": 'Two', "location": 'San Francisco'}

print(value_pair(object1, object2, 'location'))
