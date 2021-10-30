def num_vowels(text:str) -> int:
    return sum(1 if c.lower() in 'aeiou' else 0 for c in text)


import inspect
sig = inspect.signature(num_vowels)
sig.parameters['text']