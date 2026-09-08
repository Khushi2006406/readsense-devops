def recommend_book(mood, genre):
    if mood == "stressed" and genre == "motivational":
        return "The Alchemist"
    elif genre == "fiction":
        return "The Hobbit"
    else:
        return "Atomic Habits"


print("Welcome to ReadSense")

book = recommend_book("stressed", "motivational")
print("Recommended Book:", book)
