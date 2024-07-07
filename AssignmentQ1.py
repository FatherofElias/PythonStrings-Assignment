# Question 1


# Task 1


reviews = ["This product is really good. I'm impressed with its quality.", 
         "The performance of this product is excellent. Highly recommended!",
         "I had a bad experience with this product. It didn't meet my expectations.", 
         "Poor quality product. Wouldn't recommend it to anyone.", 
         "The product was average. Nothing extraordinary about it."]

# Keywords to search for
keywords = ["good", "excellent", "bad", "poor", "average"]

def capitalize_keywords(review):
    for keyword in keywords:
        review = review.replace(keyword.lower(), keyword.upper())
        review = review.replace(keyword.capitalize(), keyword.upper())
    return review

# Print modified reviews
for review in reviews:
    modified_review = capitalize_keywords(review)
    print(modified_review)
