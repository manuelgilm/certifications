import random
from typing import Dict 
from typing import Any

def get_random_prediction()->Dict[str, Any]:
    """
    Generate a random prediction for demonstration purposes.
    """
    classes = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    return {
        "prediction": random.choice(classes),
        "confidence": round(random.uniform(0.7, 1.0), 2)
    }