# Population Data Retrieval Script

This Python script utilizes the REST Countries API to retrieve and display population data for a specific country or the entire world. The script also includes a function to convert numerical population data into words.

## How to Use:

### Installation:

Ensure you have the `requests` library installed. If not, you can install it using `pip install requests`.

### Script Overview:

- The script defines a function `get_population_data(location)` that takes a country name or "global" as an argument.
- If "global" is provided, it fetches population data for all countries worldwide and displays the total population along with a word representation.
- If a specific country name is given, it retrieves and displays the population data for that country, along with a word representation.

### Number to Words Conversion:

- The script includes a function `number_to_words(num)` that converts numerical values into their word representation.
- This function uses an internal function `_convert_to_words(num)` to handle the conversion logic.

### How to Run:

- Run the script and input a country name or "global" when prompted.
- The script will then fetch and display the relevant population information.

## Dependencies:

- **requests**: Used for making HTTP requests to the REST Countries API.

## Note:

- Ensure an active internet connection for the script to fetch data from the REST Countries API.
- Handle user input carefully to avoid errors related to invalid country names.

Feel free to incorporate and modify this script based on your needs. For any issues, please refer to the error messages or seek documentation for assistance.
