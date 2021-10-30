inspect.ismodule(batch) // check is argument is a module, returns a boolean
inspect.getmembers(batch) // get classes and methods of a module, takes in a predicate function as a second argument to filter results


inspect also has methods that can help in filtering members based on their types
e.g isclass(), isfunction

modules inported into another module has their classes and functions available in the namespace of the first module

inspect module contains tools for interrogating individual functions

this is done by retrieving a signature object of the function 
e.g
init_sig = inspect.signature(batch.Batch.__init__)

//returns <Signature (self, iterables=())>

from this signature object u can retrieve a set of parameters and query for their default values
 init_sig.parameters()

signature also stores information about python type annotations