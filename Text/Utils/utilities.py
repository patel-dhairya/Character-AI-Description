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


def format_key_value(key: str, value) -> str:
    if isinstance(value, list):
        return f"\"{key}\":{double_quote_list(value)}"
    elif isinstance(value, str):
        return f"\"{key}\":\"{value}\""
    else:
        return "Error"
