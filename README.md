# Price Tracker

A simple Django application to track product prices across different stores and brands.

## Features

- **Product Management**: Track products, their brands, and packaging details.
- **Brand Management**: Organize products by brand.
- **Store Management**: Keep track of different stores (supermarkets, markets, etc.) and their locations.
- **Price Tracking**: Log and view price history for products across different stores.
- **Responsive UI**: Built using Django's generic views and templates.

## Project Structure

- `price/`: Project configuration (settings, URLs, ASGI/WSGI).
- `prices/`: Main application containing models, views, and templates.
  - `models.py`: Defines `Brand`, `Product`, `Store`, and `Price`.
  - `views.py`: Class-based views for listing, creating, updating, and deleting records.
  - `urls.py`: Application-specific URL routing.

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. (Optional) Create a superuser to access the Django admin:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Usage

Access the application at `http://127.0.0.1:8000/`.

- **Prices**: The homepage shows a list of recent prices. You can add new price entries here.
- **Products**: View and manage the catalog of products.
- **Brands**: Manage the list of brands.
- **Stores**: Manage the stores where you track prices.

## Development

To add new features or modify existing ones:
1. Update `prices/models.py` if you need to change the data structure.
2. Run `python manage.py makemigrations` and `python manage.py migrate` to apply model changes.
3. Update `prices/views.py` and `prices/urls.py` for new views and routes.
4. Modify templates in `prices/templates/` to update the UI.

## Docker & Kubernetes

### Docker

Build the image locally:
```bash
docker build -t price-tracker .
```

Run the container:
```bash
docker run -p 8000:8000 -e SECRET_KEY=your-secret-key price-tracker
```

### Kubernetes

Apply the manifests:
```bash
kubectl apply -f k8s/deployment.yml
```
*Note: Ensure you have created the `price-tracker-secret` with a `secret-key` before deploying.*
