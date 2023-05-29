def double_quote_list(ls: list) -> str:
    """Return formatted list which prints each element with double quote when
    printing list rather than single quote.

    Args:
        ls (list): List to print

    Returns:
        str: String representing list elements with each element in double quote
    """
    formatted_list = ",".join([f'"{item}"' for item in ls])
    return f"[{formatted_list}]"
