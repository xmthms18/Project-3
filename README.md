# Project-3

## Project Description
 A Weather app that provides users with current weather information for their chosen location. Users can input their preferred location and instantly receive accurate weather updates. 

## Api

## ERDs
We will design the following entities:

User: Stores user authentication and preferences.
Location: Stores user-selected locations for weather updates.
WeatherData: Stores the retrieved weather information for each location.

## Restful Routing Chart
'/': Home page displaying user's saved locations and weather updates.
/add_location: Form to add a new location for weather updates.
/location/{location_id}: Detailed weather information for a specific location.
/profile: User profile page to manage settings and preferences.

## Wireframes of Use views

* 1.HomePage -

* 2.Add Location -

* 3.Location Detail -

* 4.User Profile Page -



## User Stories
As a user, I want to view the current weather for my selected locations.
As a user, I want to add new locations to track their weather.
As a user, I want to see detailed weather information for each location.
As a user, I want to manage my profile settings and preferences.

## MVP Goals
Create a Django project with necessary configurations.
Implement user authentication and registration.
Develop a home page to display user's saved locations and basic weather information.
Integrate the OpenWeather API to fetch weather data based on user-selected locations.
Design a form to add new locations for weather updates.
Build a location detail page to show comprehensive weather data.

## Stretch Goals
Provide data visualization, such as graphs, to display historical weather trends.
Implement user settings for temperature units (Celsius/Fahrenheit) and time formats.
Incorporate real-time weather map using external libraries or APIs.
Create a responsive design for mobile devices.
