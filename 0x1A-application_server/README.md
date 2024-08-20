
Application Server (AirBnB Clone - Web Application Deployment)
This project focuses on deploying and configuring a web application using Flask, Gunicorn, and Nginx. The goal is to set up a fully functional web server capable of hosting a Flask-based AirBnB clone.

Project Overview
This project is divided into several tasks that progressively build on each other. It starts with setting up a Flask application, then integrates Gunicorn for handling HTTP requests, and finally configures Nginx as a reverse proxy to serve the application on both local and public IP addresses.

Technologies Used
Python 3.8+
Flask - A micro web framework used for routing and handling requests.
Gunicorn - A Python WSGI HTTP server for serving the Flask application.
Nginx - A web server used for serving static files and reverse proxying requests to Gunicorn.
UFW (Uncomplicated Firewall) - A firewall configuration tool for managing firewall rules.
Tasks

1. Setup a Flask Application
Clone the AirBnB clone repository (version 2) to your server.
Configure a Flask route /airbnb-onepage/ to return "Hello HBNB!".
The application should listen on port 5000 and be available at <http://0.0.0.0:5000/airbnb-onepage/>.
2. Serve the Flask Application Using Gunicorn
Serve the content of the Flask application using Gunicorn.
Run Gunicorn and bind it to 0.0.0.0:5000 with the Flask application object as the entry point.
3. Configure Nginx as a Reverse Proxy
Configure Nginx to serve the Flask application both locally and on its public IP.
The route /airbnb-onepage/ should be proxied to Gunicorn running on port 5000.
Ensure that Nginx is listening on port 80 and is accessible via your public IP address.
4. Deploy a Dynamic Route with Nginx and Gunicorn
Add a new service in the Flask application for handling dynamic routes.
Nginx should proxy requests to /airbnb-dynamic/number_odd_or_even/<int:n> to Gunicorn running on port 5001.
The dynamic route determines if the number is odd or even and displays the result on a webpage.
5. Deploy a RESTful API with Gunicorn and Nginx
Clone the AirBnB clone repository (version 3) to your server.
Setup Nginx to route /api/ requests to Gunicorn listening on port 5002.
Bind Gunicorn to handle requests for api/v1/app.py.
