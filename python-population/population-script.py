import requests

def get_population_data(location):
    # Using REST Countries API
    base_url = "https://restcountries.com/v3.1/name/"
    
    if location.lower() == "global":
        global_data = requests.get("https://restcountries.com/v3.1/all").json()
        total_population = sum(country.get('population', 0) if isinstance(country, dict) else country for country in global_data)
        
        # Displaying the result
        print("\nWorldwide Population Information:")
        print(f"Total Population: {format(total_population, ',')}")
        print(f"Total Population (In Words): {number_to_words(total_population)}")
    else:
        response = requests.get(base_url + location)
        
        if response.status_code == 200:
            country_data = response.json()[0]
            population_data = country_data.get('population', 0)

            # Displaying the result
            print(f"\nPopulation Information for {location}:")
            print(f"Total Population: {format(population_data, ',')}")
            
            # Displaying population information in words
            print("\nPopulation Information (In Words):")
            print(f"Total Population: {number_to_words(population_data)}")
        else:
            print(f"Failed to retrieve data for {location}. Make sure the country name is valid.")

# Function to convert numbers to words
def number_to_words(num):
    return _convert_to_words(num)

# Internal function to convert numbers to words
def _convert_to_words(num):
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if 1 <= num < 10:
        return f"{units[num]}"
    elif 10 < num < 20:
        return f"{teens[num - 10]}"
    elif 20 <= num < 100:
        return f"{tens[num // 10]} {units[num % 10] if num % 10 != 0 else ''}"
    elif 100 <= num < 1000:
        return f"{units[num // 100]} Hundred {_convert_to_words(num % 100)}"
    elif 1000 <= num < 1_000_000:
        return f"{_convert_to_words(num // 1000)} Thousand {_convert_to_words(num % 1000)}"
    elif 1_000_000 <= num < 1_000_000_000:
        return f"{_convert_to_words(num // 1_000_000)} Million {_convert_to_words(num % 1_000_000)}"
    elif 1_000_000_000 <= num < 1_000_000_000_000:
        return f"{_convert_to_words(num // 1_000_000_000)} Billion {_convert_to_words(num % 1_000_000_000)}"
    elif num >= 1_000_000_000_000:
        return f"{_convert_to_words(num // 1_000_000_000_000)} Trillion {_convert_to_words(num % 1_000_000_000_000)}"
    else:
        return "Zero"

# Requesting user input for the country or "global"
location_input = input("Enter a country name or type 'global' for worldwide population: ")
get_population_data(location_input)
