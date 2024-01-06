# Sample Portfolio Project

This is a sample portfolio project that demonstrates the basic structure of a web application using Flask. The project includes various views such as home, about, contact, portfolio, and a simple search functionality.

## Getting Started

### Prerequisites

- Python 
- HTML
- CSS
- Flask 

### Project Structure
• app.py: Main application file with Flask setup and routing.
• views.py: Blueprint file containing route definitions.
• templates/: HTML templates for different views.
• static/: Contains CSS styles (style.css) and image assets.

## Usage
Run the Flask application:
    ```python app.py```

## Views
• Home: Accessible at the root ("/") with optional query parameters for country and source.
• About: Information about the project and the developer.
• Contact: Simple contact page.
• Portfolio: Displays a list of sample projects with brief descriptions.
• 404: Custom error page for page not found.

## Routes
• /about-us: Redirects to the about page.
• /portfolio/<project>: Displays details of a specific project.
• /portfolio/json: Returns JSON data about sample projects.
• /s: Search endpoint that takes a keyword as a query parameter.

## Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.