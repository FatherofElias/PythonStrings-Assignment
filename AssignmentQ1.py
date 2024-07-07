# Question 1


# Task 1
# Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". 
# We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.



# Solution

#List of reviews

import string

reviews = ["This product is really good. I'm impressed with its quality.", 
         "The performance of this product is excellent. Highly recommended!",
         "I had a bad experience with this product. It didn't meet my expectations.", 
         "Poor quality product. Wouldn't recommend it to anyone.", 
         "The product was average. Nothing extraordinary about it."]

# Keywords to search for inside of reviews
keywords = ["good", "excellent", "bad", "poor", "average"]

# using .upper alond with .lower and .capitalize to make sure that all keywords regardless
# of the first letter of them being capitial or lowercase are output in full uppercase.
def capitalize_keywords(review):
    for keyword in keywords:
        review = review.replace(keyword.lower(), keyword.upper())
        review = review.replace(keyword.capitalize(), keyword.upper())
    return review

# Printing modified reviews
for review in reviews:
    modified_review = capitalize_keywords(review)
    print(modified_review)


    #Task 2


# Positive, negative and neutral words
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing"]
neutral_words = ["average"]

# Function to tally the number of positive, negative and neutral words in each review
def sentiment_tally(reviews):
    tally = {'positive': 0, 'negative': 0, 'neutral': 0}
    for review in reviews:
        # Remove punctuation from the review
        review = review.translate(str.maketrans('', '', string.punctuation))
        for word in review.split():
            if word.lower() in positive_words:
                tally['positive'] += 1
            elif word.lower() in negative_words:
                tally['negative'] += 1
            elif word.lower() in neutral_words:
                tally['neutral'] += 1
    return tally

# Printing modified reviews
for review in reviews:
    modified_review = capitalize_keywords(review)
    print(modified_review)

# Printing sentiment tally
print(sentiment_tally(reviews))

