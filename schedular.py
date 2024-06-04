import schedule
import time
from instagram_automation import post_on_instagram
from linkedin_automation_automation import post_on_linkedin
# Import other automation functions as needed

def schedule_posts():
    schedule.every().day.at("10:00").do(post_on_instagram, caption="Hello Instagram!", image_path="uploads/download (1).jpg")
    schedule.every().day.at("10:00").do(post_on_linkedin, caption="Hello Linkedin!", image_path="uploads/download (1).jpg")
    # schedule.every().day.at("10:00").do(post_on_facebook, caption="Hello Facebook!", image_path="/path/to/image.jpg")
    # Add more schedules for other platforms

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_posts()
