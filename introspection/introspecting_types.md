Functions for introspecting type of an object
 - type()
 - issubclass(a, b) 
    - determines if a is a subclass of b
    - a can be a class or a tuple of classes
 - isinstance(obj, class)
    - determines if obj is an instance of class
    - obj can be an object of any type

avoid type checks if possible, if needed prefer isinstance or issubclass over type

Tools for introspecting attributes of an object
    - dir() returns the list of attribute(including method names) names for an instance
    - getattr(object, 'attribute string')
    - callable - checks if an attribute is callable as a method
    - hasattr(object, 'attr_name') - checks if an attribute exists
    


Introspecting relationships between types

Introspecting relationships between objects and types

Fundermentals of python type system