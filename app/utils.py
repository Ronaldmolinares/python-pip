import pandas as pd


def filter_country(busqueda: str, df):
    """
    Filtra un país específico y retorna sus datos de población por año.
    """
    try:
        country_data = df[df["Country/Territory"] == busqueda.title()]
        
        if country_data.empty:
            return [], []
        
        population_columns = [
            "2022 Population", "2020 Population", "2015 Population",
            "2010 Population", "2000 Population", "1990 Population",
            "1980 Population"
        ]
        
        years = [col.split()[0] for col in population_columns]
        values = country_data[population_columns].values[0].astype(int)
        
        return years, values
    except Exception as e:
        return [], []


def world_population_percentage(df):
    """
    Retorna los valores y labels de porcentaje de población mundial por país.
    """
    values = df["World Population Percentage"].tolist()
    labels = df["Country/Territory"].tolist()
    
    return values, labels


def countries_with_population(df):
    """
    Retorna el porcentaje de población y nombres de países de un DataFrame filtrado.
    """
    porcentaje_poblacion = df["World Population Percentage"].tolist()
    paises = df["Country/Territory"].tolist()
    
    return porcentaje_poblacion, paises


def continent_population_percentage(df):
    """
    Calcula el porcentaje de población mundial por continente.
    """
    continent_data = df.groupby("Continent")["World Population Percentage"].sum()
    
    return continent_data.index.tolist(), continent_data.values.tolist()

