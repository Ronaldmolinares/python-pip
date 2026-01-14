import charts
import read_csv
import utils


def show_menu():
    print("\n" + "=" * 50)
    print("World Population Dataset")
    print("=" * 50)
    print("1. Buscar país y mostrar gráfico de barras")
    print("2. Ver porcentaje de población mundial (gráfico de pastel)")
    print("3. Ver población por continente (gráfico de pastel)")
    print("4. Ver población por continente especifico (gráfico de pastel)")
    print("5. Salir")
    print("=" * 50)


def search_country(df):
    country = input("\nIngrese el nombre del país: ")
    keys, values = utils.filter_country(country, df)

    try:
        if len(keys) > 0:
            print(f"\nDatos de {country.title()}:")
            print(f"Años: {list(keys)}")
            print(f"Población: {list(values)}")
            charts.generate_bar_chart(country.title(), keys, values)
        else:
            print(f"\nNo se encontró el país '{country}'")
    except Exception as e:
        print(f"Error: {e}, {type(e)}")


def show_world_population(df):
    print("\nGenerando gráfico de población mundial...")
    values, labels = utils.world_population_percentage(df)
    charts.generate_pie_chart(values, labels)


def show_continent_population(df):
    print("\nGenerando gráfico de población por continente...")
    continent, population = utils.continent_population_percentage(df)
    charts.generate_pie_chart(population, continent)


def population_by_continent(df):
    print("Continentes: Asia, Europe, Africa, Oceania, South America, North America")
    continent = input("Ingrese el nombre del continente: ")
    df_filtered = df[df["Continent"] == continent.title()]
    percentage_population, countries = utils.countries_with_population(df_filtered)
    charts.generate_pie_chart(percentage_population, countries, name=continent.title())


def run():
    df = read_csv.read_csv("data.csv")

    while True:
        show_menu()
        opcion = input("\nSeleccione una opción (1-5): ")

        if opcion == "1":
            try:
                search_country(df)
            except ValueError as e:
                print(f"Error: Pais no registrado en el data set\n{e} , {type(e)}")
        elif opcion == "2":
            show_world_population(df)
        elif opcion == "3":
            show_continent_population(df)
        elif opcion == "4":
            population_by_continent(df)
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione 1, 2, 3, 4 o 5.")


if __name__ == "__main__":
    run()