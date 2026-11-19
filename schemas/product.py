PRODUCT_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "description", "price", "in_stock"],
    "properties": {
        "id": {"type": "string", "minLength": 1},
        "name": {"type": "string", "minLength": 1},
        "description": {"type": "string"},
        "price": {"type": "number", "minimum": 0},
        "in_stock": {"type": "boolean"},
    }
}