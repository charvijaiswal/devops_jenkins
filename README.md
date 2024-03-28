# Online Shopping API

This API provides endpoints for managing products and user shopping carts.

## Endpoints

### Get All Products
- **URL:** `http://127.0.0.1:5000/products`
- **Method:** GET

### Get Product By Id
- **URL:** `http://127.0.0.1:5000/products/1`
- **Method:** GET

### Add a Product
- **URL:** `http://127.0.0.1:5000/products`
- **Method:** POST
- **Sample Body Data For Postman:**
    ```json
    {
        "id": 5,
        "name": "Mac Book Pro",
        "price": 45.55,
        "description": "Amazing laptop with awesome security"
    }
    ```

### Get Cart Details
- **URL:** `http://127.0.0.1:5000/cart?user_id=1234`
- **Method:** GET

### Add Products To Cart
- **URL:** `http://127.0.0.1:5000/cart/add`
- **Method:** POST
- **Sample Body Data For Postman:**
    ```json
    {
        "user_id": "user123",
        "product_id": 2,
        "quantity": 3
    }
    ```

### Delete Product From Cart
- **URL:** `http://127.0.0.1:5000/cart/delete`
- **Method:** POST
- **Sample Body Data For Postman:**
    ```json
    {
        "user_id": "user123",
        "product_id": 2
    }
    ```

## Usage Notes
- For POST requests to add a product or add to cart, ensure the body data is provided in JSON format as shown in the sample data.
- Replace `127.0.0.1:5000` with the appropriate hostname and port if the API is hosted elsewhere.
