# Send logs simulating real traffic

```zsh

curl -X POST "http://localhost:8000/log" \
     -H "Content-Type: application/json" \
     -d '{"message": "User login", "endpoint": "/api/login", "status_code": 200}'

curl -X POST "http://localhost:8000/log" \
     -H "Content-Type: application/json" \
     -d '{"message": "Get products", "endpoint": "/api/products", "status_code": 200}'

curl -X POST "http://localhost:8000/log" \
     -H "Content-Type: application/json" \
     -d '{"message": "User login failed", "endpoint": "/api/login", "status_code": 401}'

curl -X POST "http://localhost:8000/log" \
     -H "Content-Type: application/json" \
     -d '{"message": "Server error", "endpoint": "/api/orders", "status_code": 500}'

```
