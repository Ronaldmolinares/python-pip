def filter_country(busqueda: str, data):
    try:
        for country in data:
            if country["Country/Territory"] == busqueda.title():
                resultado = {
                    "2022 Population": int(country["2022 Population"]),
                    "2020 Population": int(country["2020 Population"]),
                    "2015 Population": int(country["2015 Population"]),
                    "2010 Population": int(country["2010 Population"]),
                    "2000 Population": int(country["2000 Population"]),
                    "1990 Population": int(country["1990 Population"]),
                    "1980 Population": int(country["1980 Population"]),
                }

        return resultado.keys(), resultado.values()
    except UnboundLocalError:
        return "Error: pais no encontrado."


def world_population_percentage(data):
    labels = []
    values = []
    for country in data:
        values.append(country["World Population Percentage"])
        labels.append(country["Country/Territory"])

    return values, labels


def countries_with_population(data):
    paises = list(map(lambda country: country["Country/Territory"], data))
    porcentaje_poblacion = list(
        map(lambda country: country["World Population Percentage"], data)
    )
    return porcentaje_poblacion, paises


def continent_population_percentage(data):
    dict_continent = {
        "Asia": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "Asia"
        ),
        "Europe": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "Europe"
        ),
        "Africa": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "Africa"
        ),
        "Oceania": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "Oceania"
        ),
        "South America": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "South America"
        ),
        "North America": sum(
            float(country["World Population Percentage"])
            for country in data
            if country["Continent"] == "North America"
        ),
    }

    return dict_continent.keys(), dict_continent.values()

