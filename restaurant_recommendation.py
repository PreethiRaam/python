import random

# Data structure to store information about restaurants and cuisines
restaurants = {
    "Italian": ["Pasta Palace", "Pizza Haven", "Mama Mia's"],
    "Mexican": ["Taco Town", "Burrito Bistro", "Salsa Shack"],
    "Japanese": ["Sushi House", "Ramen Express", "Tempura Kingdom"],
    "Indian": ["Sultan Biriyani","Ananda Bhavan","Jigarthanda cafe"]
}

# Additional information about the restaurants (ratings and proximity)
restaurant_info = {
    "Pasta Palace": {"rating": 4.5, "proximity": 3},
    "Pizza Haven": {"rating": 4.2, "proximity": 2},
    "Mama Mia's": {"rating": 4.8, "proximity": 4},
    "Taco Town": {"rating": 4.0, "proximity": 3},
    "Burrito Bistro": {"rating": 4.3, "proximity": 2},
    "Salsa Shack": {"rating": 4.7, "proximity": 4},
    "Sushi House": {"rating": 4.6, "proximity": 3},
    "Ramen Express": {"rating": 4.4, "proximity": 2},
    "Tempura Kingdom": {"rating": 4.1, "proximity": 4},
    "Sultan Biriyani":{"rating":4.2, "proximity":3},
    "Ananda Bhavan":{"rating":3.8, "proximity":3},
    "Jigarthanda cafe":{"rating":4.5, "proximity":4}
}

def recommend_restaurants(user_input):
    user_input = user_input.capitalize()

    if user_input in restaurants:
        # Sort restaurants based on rating and proximity
        recommended_restaurants = sorted(restaurants[user_input], key=lambda x: (restaurant_info[x]["rating"], -restaurant_info[x]["proximity"]), reverse=True)
        
        return recommended_restaurants
    else:
        raise ValueError("Invalid or unavailable type of food")

# Example usage
try:
    user_input = input("Enter a type of food: ")
    recommendations = recommend_restaurants(user_input)
    print(f"Recommended restaurants for {user_input}: {recommendations}")
except ValueError as e:
    print(e)
