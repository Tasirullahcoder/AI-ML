# PROBLEM 1  GIVEN A JSON DATA,WHICH WE HAVE TO CLEAN IT AND STRUCTURE IT IN A WAY THAT IS EASY TO ANALYZE.
# 1 DATA IS INCONSISTENT,MIXED TYPES RATING
# 2 MISSING DATA AGE
# 3 DUPLICATE DATA USERS


import json

# Load the data
def load_data(fileName):
    with open(fileName, "r") as f:
        data = json.load(f) # json.load(f) reads the JSON content and converts it into Python objects.
        return data


result = load_data("store_Data.json")


# Clean and structure the data
def cleanData(result):
    # we create a dictionary to map text ratings to numeric values
    text_to_num = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }

    clean_data = [] # create an empty list to store the cleaned data
    unique_users = set() # create a set to keep track of unique user names

    for user in result: 

        # 1. Clean rating
        raw_rating = str(user.get("rating", "")).strip().lower() # we retrieve the rating, convert it to a string, strip remove whitespace, and convert it to lowercase for consistency.

        if raw_rating in text_to_num: # we check if word rating is in the text_to_num  is a key, we convert it to its corresponding numeric value.
            raw_rating = text_to_num[raw_rating] # then we replace the word rating with its numeric value.
        else:
            raw_rating = float(raw_rating) # if the rating is not a word, we try to convert it to a float. If it fails, we set it to 0.

        user["rating"] = raw_rating # we update the user dictionary with the cleaned rating.

        # 2. Handle missing age
        raw_age = user.get("age") # we retrieve the age from the user dictionary. If it's missing, we set it to 0. Otherwise, we convert it to an integer.

        if raw_age is None:# if the age is missing, we set it to 0.
            user["age"] = 0
        else:
            user["age"] = int(raw_age) # we convert the age to an integer and update the user dictionary.

        # 3. Remove duplicate users
        name = user.get("name", "").strip().lower()

        if name not in unique_users: # we check if the name is already in the unique_users set. If it's not, we add it to the set and append the user to the clean_data list.
            unique_users.add(name)
            clean_data.append(user)

    # 4. Return cleaned data
    return clean_data


cleaned_result = cleanData(result)

# print(cleaned_result)

###########################################################################

# PROBLEM 2 GETTING MEANINGFUL INSIGHTS FROM THE CLEANED DATA
# 1 WHAT IS THE AVERAGE RATING OF THE PRODUCT?
# 2 WHAT IS % OF USERS WHO GAVE POOR RATING?(RATING < 3)?

def get_insights(cleaned_result):

    # 1. Average rating
    total_rating = 0

    for user in cleaned_result:
        total_rating += float(user["rating"])

    average = total_rating / len(cleaned_result) if cleaned_result else 0
    print(f"Average rating = {average}")

    # 2. Percentage of poor ratings
    poor_rating = 0

    for user in cleaned_result:
        if user["rating"] < 3:
            poor_rating += 1

    percentage = (poor_rating / len(cleaned_result)) * 100 if cleaned_result else 0

    print("Users with poor ratings:", poor_rating)
    print("Total users:", len(cleaned_result))
    print(f"Poor rating percentage = {percentage}%")

get_insights(cleaned_result)
    

# #########################################

# 3 PROBLEM BUILD A PRODUCT BASE RECOMMENDATION FEATURE (RULE BASED NOT ML)
# FOR EXAMPLE IPHONE OR SAMSUNG MOBILES PRODUCTS RECOMMENDATION
# IF USER RATING >=4, RECOMMAND SAME BRAND PRODUCTS
# IF USER RATING <4 RECOMMAND DIFFERENT BRAND PRODUCTS

def get_recommendation(cleaned_result):
    # OUTSIDE LOOP: Create an empty list only once to store all users' recommendations.
    # It must be outside the loop so previous recommendations are not lost or reset.
    recommandation=[] 
    for user in cleaned_result:
        # INSIDE LOOP: Create a new empty dictionary for each user.
        # Every user needs a separate dictionary to store their recommendation.
        curr_recomm={} 
        curr_recomm["name"]=user["name"]
        if user["rating"] >= 4:
            curr_recomm["brand"]="apple"
        else:
            curr_recomm["brand"]="samsung"
        recommandation.append(curr_recomm)
    return recommandation

recommand_products=get_recommendation(cleaned_result)
print(recommand_products)