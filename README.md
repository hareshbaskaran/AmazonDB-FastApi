#Amazon Store API with FastAPI
This is an e-commerce platform backend built with FastAPI and integrated with Amazon Store. The platform supports buying and selling products, leaving reviews, and saving products for later purchase. It uses Stripe for online payments, Redis for caching of shopping carts, OAuth2 for portal defined authentication, Mailgun for email systems, Firebase for OTP verification, and image cloud storage and messaging systems. Bcrypt is used for encryption and Neo4j for graphical representation of courier service providers.

Features
User registration as seller or buyer
Buying and selling products
Writing and viewing reviews
Adding products to wishlist and shopping cart
Multiple cards, addresses, and phone numbers per user
Online payments with Stripe
Caching of shopping cart with Redis
OAuth2 authentication
Email systems with Mailgun
OTP verification with Firebase
Image cloud storage and messaging systems
Encryption with Bcrypt
Graphical representation of courier service providers with Neo4j
Pre-trained model for image to product search with Codelabs
Setup and Installation
Clone the repository
Install the dependencies with pip install -r requirements.txt
Create a .env file with environment variables for database connection, Stripe, Redis, OAuth2, Mailgun, Firebase, Neo4j, and Codelabs API keys and credentials
Run the application with uvicorn main:app --reload
API Documentation
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
Database Design
ER Diagram
Normalized Relational Schema
Contributors
