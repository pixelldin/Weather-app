
# Weather App

This Flask application allows users to check the current weather for a specified city using the OpenWeatherMap API.

## Description

The application has a single route (`/`) that handles both `GET` and `POST` requests. Users can input a city name to get the current weather conditions, including temperature and weather description.

### Functionality

1. **GET request**: Renders a form for users to enter a city name.
2. **POST request**: 
   - Retrieves the city name from the form.
   - Makes an API call to OpenWeatherMap to get the weather data.
   - Handles errors such as city not found or other API errors.
   - Renders the weather data on the same page.

### API Key

The application uses an API key from OpenWeatherMap, which is stored in an environment variable. The `dotenv` library is used to load the API key from a `.env` file.

### Templates

The application uses a template file `weather.html` to render the form and display the weather data or error messages.

## Usage

1. **Clone the repository**.
2. **Install dependencies**:
    ```sh
    pip install flask requests python-dotenv
    ```
3. **Create a `.env` file** in the root directory and add your OpenWeatherMap API key:
    ```
    API_KEY=your_api_key_here
    ```


## Dependencies

- Python 3.x
- Flask
- Requests
- python-dotenv

## License

This project is licensed under the MIT License - see the LICENSE file for details.

### Directory Structure

```
Weather App/
│
├── app.py
├── .env
├── templates/
│   └── weather.html
├── static/
│   └── styles.css
└── README.md
```
