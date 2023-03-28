# FastAPI Integration of Amazon Store

This is an e-commerce platform backend built with FastAPI and integrated with Amazon Store. The platform supports buying and selling products, leaving reviews, and saving products for later purchase. It uses Stripe for online payments, Redis for caching of shopping carts, OAuth2 for portal defined authentication, Mailgun for email systems, Firebase for OTP verification, and image cloud storage and messaging systems. Bcrypt is used for encryption and Neo4j for graphical representation of courier service providers.

## Features

- User registration as seller or buyer
- Buying and selling products
- Writing and viewing reviews
- Adding products to wishlist and shopping cart
- Multiple cards, addresses, and phone numbers per user
- Online payments with Stripe
- Caching of shopping cart with Redis
- OAuth2 authentication
- Email systems with Mailgun
- OTP verification with Firebase
- Image cloud storage and messaging systems
- Encryption with Bcrypt
- Graphical representation of courier service providers with Neo4j
- Pre-trained model for image to product search with Codelabs

## Database Design 
- ER diagram : 
- Normalised Relational Schema :
- Database and Project Analysis: https://docs.google.com/document/d/e/2PACX-1vQBefVC2wWksEsZvqFS04Hw_9kSxNgplvfubVVVJIQeXNR8-GkAYevTKQvJ67rd47ZrFCxpqrH-O3MJ/pub

## Installation

1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Run the application using `uvicorn main:app --reload`.

## Usage

After installation, the following endpoints will be available:

- `/register`: Allows a user to register as a seller or buyer.
- `/products`: Allows a user to add and view products.
- `/wishlist`: Allows a buyer to add and view products in their wishlist.
- `/cart`: Allows a buyer to add and view products in their shopping cart.
- `/cards`: Allows a user to add and view credit cards.
- `/addresses`: Allows a user to add and view addresses.
- `/phones`: Allows a user to add and view phone numbers.
- `/buy`: Allows a user to purchase a product.
- `/buy_cart`: Allows a buyer to purchase all products in their shopping cart.
- `/reviews`: Allows a buyer to write reviews for products.
- `/images/product`: Allows a seller to upload images for a product.
- `/images/review`: Allows a buyer to upload images for a review.

## Tech - Integration 
The following integrations are used in the project:

- Stripe API for online payments
- Redis for caching shopping cart
- OAuth2 for portal-defined authentication
- Mailgun for email notification
- Firebase for OTP verification
- Neo4j for graphical representation of courier service providers 

## Environment Variables
The following environment variables are required:

- `DATABASE_URL`: database URL
- `STRIPE_SECRET_KEY`: Stripe secret key
- `STRIPE_PUBLISHABLE_KEY`: Stripe publishable key
- `REDIS_URL`: Redis URL
- `JWT_SECRET`: JWT secret key
- `MAILGUN_DOMAIN`: Mailgun domain name
- `MAILGUN_API_KEY`: Mailgun API key
- `FIREBASE_PROJECT_ID`: Firebase project ID
- `FIREBASE_APP_ID`: Firebase app ID
- `FIREBASE_API_KEY`: Firebase API key
- `FIREBASE_AUTH_DOMAIN`: Firebase auth domain
- `NEO4J_URI`: Neo4j URI
- `NEO4J_USER`: Neo4j username
- `NEO4J_PASSWORD`: Neo4j password

## API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
