import pandas as pd
import random
import faker

# Initialize faker for generating random data
fake = faker.Faker()

# Existing data pattern
user_ids = ['U001', 'U002', 'U003', 'U004']
platforms = ['Instagram', 'YouTube', 'Facebook', 'Twitter', 'TikTok']
activities = ['scrolling', 'video_watching', 'tweeting', 'commenting', 'reels_watching', 'video_browsing', 'chatting']

# Initialize lists to store data
data = []

# Function to create large data
for i in range(1000):  # Increase this number for larger dataset
    user_id = random.choice(user_ids)
    platform = random.choice(platforms)
    timestamp = fake.date_time_this_year()
    activity_type = random.choice(activities)
    duration = random.randint(10, 60)  # duration between 10 and 60 minutes
    data.append([user_id, platform, timestamp, activity_type, duration])

# Create a DataFrame
df = pd.DataFrame(data, columns=['user_id', 'platform', 'timestamp', 'activity_type', 'duration_minutes'])

# Save to CSV
df.to_csv('large_digital_addiction_data.csv', index=False)

print("Large dataset created and saved as 'large_digital_addiction_data.csv'")
