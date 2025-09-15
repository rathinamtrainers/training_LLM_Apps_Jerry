from google.adk.agents import Agent


def get_weather(city: str) -> dict:
    """
    Retrieves the current weather report for the specified city.

    :param city: The name of the city for which to retrieve the weather report
    :return: dict: status and result or error message.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": "New York is experiencing clear weather with a temperature of 22 degrees Celsius."
        }
    else:
        return {
            "status": "error",
            "message": f"Weather data not available for the city {city}."
        }

def get_current_time(city: str) -> dict:
    """
    Returns the current time in the specified city.

    :param city: The name of the city for which current time has to be retrieved.
    :return: dict: Status and result or error message.
    """
    if city.lower() == "new york":
        return {
            "status": "success",
            "time": "10:30 AM"
        }
    else:
        return {
            "status": "error",
            "message": f"Time data not available for the city {city}."
        }

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.5-flash",
    description="Agent to answer questions about the time and weather in a city.",
    instruction="""You are a helpful agent who can answer user questions about the time and weather in a city.
    Don't answer questions that are not related to the time and weather in a city.""",
    tools=[get_weather, get_current_time]
)