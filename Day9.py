#Dictionary - Key value pairs

# student_report = {"Name": "punit",
#                   "Branch":"CSE",
#                   "Semester": 8}
# print(student_report)

#Retrieving an item form the dictionary
# print(student_report["Name"])

#Adding an item to the dictionary
# student_report["Address"] = "Delhi"
# print(student_report)

#Creating an empty Dictionary
# empty_Dictionary = {}
# print(empty_Dictionary)

#Wipe out an Existing dictionary
# student_report = {}
# print(student_report)

#Append an Key value
# student_report["Name"] = "Punit Mann"
# print(student_report)

#Loop Through a Dictionary
# for key in student_report:
#     print(key)
#     print(student_report[key])
# for key, value in student_report.items():
#     print(key, ":", value)


#Grading Program
# student_scores = {
#     "harry": 81,
#     "ron": 78,
#     "hermaini": 99,
#     "draco": 62
# }

# student_grades = {}
# for student in student_scores:
#     score = student_scores[student]

#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# print(student_grades)


# Nesting dictionary inside dictionary
# fruits_vegies = {
#     "fruits" : {"without_peel" : ["Apple", "Cherry"], "with_peel":["Banana","Papaya"] } ,
#     "vegies" : ["Tomato", "Potato", "Onion"]
# }
# print(fruits_vegies["fruits"]["without_peel"])

# Nesting list inside dictionary
# fruits_vegies = [{
#          "without_peel" : ["Apple", "Cherry"],
#          "with_peel" : ["Banana","Papaya"] ,
#
# },
#     {"vegies" : ["Tomato", "Potato", "Onion"]}]
# print(fruits_vegies[0]["with_peel"])

#Dictionary in list

# travel_log = [
#     {"country": "japan",
#      "visits": 15,
#      "cities": ["moncho", "concho"]
#     },
# {   "country": "china",
#      "visits": 5,
#      "cities": ["chomo", "cocho"]
#     }
# ]
#
# def add_new_country(country_visited, no_of_times, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = no_of_times
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)
# add_new_country("India",10,["Delhi", "Himachal pradesh"])
# print(travel_log)


#Auction Program
# from replit import clear
# bids = {}
# bidding_finished = False
#
# def find_highest_bidder(bids):
#     highest_bidder = 0
#     winner = ""
#     for bidder in bids:
#         bid_amount = bids[bidder]
#         if bid_amount > highest_bidder:
#             highest_bidder = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with {highest_bidder}")
#
# while not bidding_finished:
#     name = input("What is your name:\n").lower()
#     amount = int(input("What is your bid:\n"))
#     bids[name] = amount
#     should_continue = input("Type yes to continue and no for exit").lower()
#     if should_continue == "no":
#         bidding_finished = True
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         clear()






