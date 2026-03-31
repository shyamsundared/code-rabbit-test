# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverses the characters in a string.
    
    Returns:
        reversed_text (str): The input string with characters in reverse order.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the whitespace-delimited words in a sentence.
    
    Parameters:
        sentence (str): Input text whose words will be counted.
    
    Returns:
        int: Number of tokens produced by splitting `sentence` on whitespace.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a Celsius temperature to Fahrenheit.
    
    Parameters:
        celsius (int | float): Temperature in degrees Celsius.
    
    Returns:
        float: Equivalent temperature in degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32
