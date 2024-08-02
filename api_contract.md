Thanks for providing the files. Here's the API contract with sample data based on the provided blueprint, manager, and repository files.

### API Endpoints and Sample Data

---

#### 1. **Get Order Status**

- **Endpoint**: `/orders/status`
- **Method**: `GET`
- **Query Parameters**:
  - `status`: (Optional) Status of the order (`pending`, `in progress`, `ready`, `delivered`).
  - `orderId`: (Optional) ID of the order.
  
- **Sample Request**:
  ```http
  GET /orders/status?status=pending
  ```
  ```http
  GET /orders/status?orderId=123
  ```
  
- **Sample Response** (Status-based):
  ```json
  {
    "orders": [
      {
        "id": 1,
        "user_id": 101,
        "status": "pending",
        "total_cost": 50.0,
        "payment_done": true,
        "created_timestamp": "2024-08-01T12:00:00Z",
        "updated_timestamp": "2024-08-01T12:00:00Z"
      },
      ...
    ]
  }
  ```
  
- **Sample Response** (Order ID-based):
  ```json
  {
    "orders": [
      {
        "id": 123,
        "user_id": 101,
        "status": "in progress",
        "total_cost": 75.0,
        "payment_done": true,
        "created_timestamp": "2024-08-01T12:00:00Z",
        "updated_timestamp": "2024-08-01T13:00:00Z"
      }
    ]
  }
  ```
  
- **Error Responses**:
  - Invalid status parameter:
    ```json
    {
      "error": "Invalid status parameter. Must be one of: pending, in progress, ready, delivered."
    }
    ```
  - Order not found:
    ```json
    {
      "error": "Order not found for the orderId 123"
    }
    ```
  - Missing query parameter:
    ```json
    {
      "error": "Missing query parameter."
    }
    ```

---

#### 2. **Update Order Status**

- **Endpoint**: `/orders/status`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "orderId": 123,
    "status": "ready"
  }
  ```
  
- **Sample Response**:
  ```json
  {
    "message": "Order status updated."
  }
  ```
  
- **Error Responses**:
  - Missing status or order ID parameter:
    ```json
    {
      "error": "Missing 'status' query parameter."
    }
    ```
    ```json
    {
      "error": "Missing 'order_id' query parameter."
    }
    ```
  - Invalid status parameter:
    ```json
    {
      "error": "Invalid status parameter. Must be one of: pending, in progress, ready, delivered."
    }
    ```

---

#### 3. **Get Order History**

- **Endpoint**: `/orders/history`
- **Method**: `GET`
- **Query Parameters**:
  - `customerId`: (Required) ID of the customer.
  
- **Sample Request**:
  ```http
  GET /orders/history?customerId=101
  ```
  
- **Sample Response**:
  ```json
  {
    "customerId": 101,
    "orders": [
      {
        "id": 1,
        "user_id": 101,
        "status": "delivered",
        "total_cost": 50.0,
        "payment_done": true,
        "created_timestamp": "2024-08-01T12:00:00Z",
        "updated_timestamp": "2024-08-01T14:00:00Z"
      },
      ...
    ]
  }
  ```

- **Error Response**:
  ```json
  {
    "error": "Missing 'customerId' query parameter."
  }
  ```

---

#### 4. **Get KDS Orders**

- **Endpoint**: `/kds/orders`
- **Method**: `GET`
  
- **Sample Request**:
  ```http
  GET /kds/orders
  ```
  
- **Sample Response**:
  ```json
  {
    "orders": [
      {
        "id": 1,
        "user_id": 101,
        "status": "in progress",
        "total_cost": 50.0,
        "payment_done": true,
        "created_timestamp": "2024-08-01T12:00:00Z",
        "updated_timestamp": "2024-08-01T12:00:00Z"
      },
      ...
    ]
  }
  ```

- **Error Response**:
  ```json
  {
    "error": "Internal server error message."
  }
  ```

---
