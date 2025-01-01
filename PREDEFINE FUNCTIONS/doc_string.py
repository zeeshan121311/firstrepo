def greet(name: str) ->str:
    """
   Returns a greeting message.

    Parameters:
        name (str): The name to greet.
    
    Returns:
        str: A personalize greeting
    """
    return f"Hello, {name}!"
 
name = greet('Zeeshan')

print(name) 