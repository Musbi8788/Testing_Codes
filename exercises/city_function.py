def city_country(city_name, country_name, population=""):
    """City and Country name:


    Args:
        city_name (_type_): A city name
        country_name (_type_): A country name
    """
    if population:
        formatted_name = f"{city_name}, {country_name} - {population}"
    else:
        formatted_name = f"{city_name}, {country_name}"
    return formatted_name.title()
