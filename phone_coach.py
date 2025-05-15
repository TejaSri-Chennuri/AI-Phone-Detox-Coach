import random

# Define the user profile for "The Night Owl Socializer"
profile_a = {
    "name": "The Night Owl Socializer",
    "typical_usage": "late at night (11 PM - 2 AM)",
    "dominant_apps": ["social media", "messaging"],
    "triggers": ["wind-down", "FOMO"],
    "desired_changes": ["reduce late-night scrolling", "improve sleep"],
    "suggestions": [
        "Consider setting a phone curfew an hour before bed.",
        "Try replacing late-night scrolling with reading a physical book or listening to an audiobook.",
        "Remember that better sleep can lead to more energy and focus tomorrow!",
        "Perhaps dim your screen significantly in the hour before you plan to sleep.",
    ]
}

# Define the user profile for "The Boredom Scroller"
profile_b = {
    "name": "The Boredom Scroller",
    "typical_usage": "frequent short bursts during the day",
    "dominant_apps": ["social media", "news", "casual games"],
    "triggers": ["boredom", "idle time"],
    "desired_changes": ["reduce impulsive checks", "find alternatives"],
    "suggestions": [
        "It's great you're taking breaks! When you feel that urge to scroll, perhaps try a quick stretch or a short walk instead?",
        "How about keeping a small notebook and pen handy to jot down thoughts when you're feeling idle?",
        "Maybe try a quick mindfulness exercise or just observe your surroundings for a minute.",
        "Consider having a go-to list of quick, enjoyable activities that don't involve your phone.",
    ]
}

# Define the user profile for "The Entertainment Bingewatcher"
profile_c = {
    "name": "The Entertainment Bingewatcher",
    "typical_usage": "longer sessions in evenings/weekends",
    "dominant_apps": ["streaming", "video platforms"],
    "triggers": ["relaxation", "escapism"],
    "desired_changes": ["limit viewing time", "more varied activities"],
    "suggestions": [
        "Enjoying your shows! Remember to take short breaks to rest your eyes and maybe do something else you enjoy too.",
        "Perhaps set a timer for your viewing sessions to help you stay mindful of the time.",
        "Consider planning a different enjoyable activity for after your viewing session.",
        "Maybe explore other forms of relaxation that don't involve screens, like listening to music or a podcast.",
    ]
}

# Define the user profile for "The Notification Addict"
profile_d = {
    "name": "The Notification Addict",
    "typical_usage": "frequent and reactive throughout the day",
    "dominant_apps": ["all"],
    "triggers": ["notifications", "FOMO"],
    "desired_changes": ["reduce checking", "improve focus"],
    "suggestions": [
        "You're staying connected! Maybe try setting specific times to check notifications and keep focused in between.",
        "Consider turning off non-essential notifications to reduce interruptions.",
        "Perhaps try putting your phone on 'Do Not Disturb' for focused work periods.",
        "Remember that responding immediately isn't always necessary. You can check in at your own pace.",
    ]
}

# List of all user profiles
user_profiles = [profile_a, profile_b, profile_c, profile_d]

def get_suggestion(profile):
    """
    Selects and returns a random positive reinforcement suggestion
    from the list of suggestions for the given user profile.
    """
    return random.choice(profile["suggestions"])

def main():
    """
    Main function to present a simple text-based phone detox coach.
    It allows the user to select a simulated profile and receive a suggestion.
    """
    print("Welcome to your Simple Phone Detox Coach!")
    print("Choose a profile to simulate:")
    for i, profile in enumerate(user_profiles):
        print(f"{i + 1}. {profile['name']}")

    while True:
        try:
            choice = int(input("Enter the number of your profile (or 0 to quit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(user_profiles):
                selected_profile = user_profiles[choice - 1]
                suggestion = get_suggestion(selected_profile)
                print(f"\nSuggestion for '{selected_profile['name']}':")
                print(suggestion)
                print("\n")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("Thank you for using the Simple Phone Detox Coach!")

if __name__ == "__main__":
    main()

# --- Outline of Next Steps for a Full Project ---
# 1. Real-time Data Acquisition:
#    - Android: Research and implement the UsageStatsManager API to access app usage data.
#    - iOS: Explore the ScreenTime and DeviceActivity frameworks (considering privacy limitations).
#    - Handle user permissions for data access.
#
# 2. Data Storage:
#    - Decide on data storage (local on device or a backend server).
#    - If backend: Choose a database (e.g., PostgreSQL, MongoDB) and set up data models.
#
# 3. Developing AI Models:
#    - Analyze historical usage data to identify patterns and triggers.
#    - Implement machine learning models for personalized suggestions (e.g., clustering, time series analysis).
#    - Train models to predict potential excessive use and optimize suggestion delivery.
#
# 4. Mobile App Development:
#    - Design the user interface (UI) and user experience (UX) of the mobile app.
#    - Choose a development framework (e.g., Flutter, React Native) or native development.
#    - Integrate the data acquisition, AI engine, and UI.
#
# 5. Ethical Considerations:
#    - Prioritize user data privacy and security.
#    - Obtain explicit user consent for data collection and usage.
#    - Be transparent about how the app works and its potential impact.
#
# 6. More Sophisticated Features:
#    - Implement features like progress tracking, goal setting, customizable suggestions, and integration with other well-being apps.