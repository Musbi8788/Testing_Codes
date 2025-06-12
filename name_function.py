def get_formatted_name(first, last, middle=""):
    """_summary_
    Generate a neatly formatted full name.

    Args:
        first (str): first name
        last (str): last name
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
