import requests
from bs4 import BeautifulSoup
import time
import csv

# List of manually stored URLs for each major
major_urls = [
    "https://catalog.clemson.edu/preview_program.php?catoid=43&poid=11978&returnto=1504",
    "https://catalog.clemson.edu/preview_program.php?catoid=43&poid=11979&returnto=1504",
    # Add more URLs here
]

# Function to scrape course information from a major page
def scrape_courses(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find program requirements section
    program_section = soup.find("div", class_="program-requirements")
    
    if not program_section:
        print(f"No program requirements found for {url}")
        return []

    courses = []
    
    # Find each year/semester block
    year_blocks = program_section.find_all("h3")
    for block in year_blocks:
        # Capture the year or semester title (e.g., "Freshman Year")
        year_or_semester = block.get_text(strip=True)
        
        # Find all the course listings under this section
        next_element = block.find_next("ul")  # Assuming courses are in <ul> under each header
        if next_element:
            course_items = next_element.find_all("li")
            for item in course_items:
                course_text = item.get_text(strip=True)
                # Parse course information (code, title, credits)
                parts = course_text.split(" - ")
                if len(parts) >= 2:
                    course_code = parts[0].strip()
                    course_title = parts[1].strip()
                    credits = parts[2] if len(parts) > 2 else "No Credits Info"
                    
                    courses.append({
                        "Year/Semester": year_or_semester,
                        "Course Code": course_code,
                        "Course Title": course_title,
                        "Credits": credits
                    })
    
    return courses

# Loop through each major URL and scrape courses
all_courses = []
for url in major_urls:
    courses = scrape_courses(url)
    all_courses.extend(courses)
    time.sleep(1)  # Be respectful to the server

# Save courses to CSV
with open("courses_data.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Year/Semester", "Course Code", "Course Title", "Credits"])
    writer.writeheader()
    writer.writerows(all_courses)

print(f"Scraped data for {len(all_courses)} courses. Saved to 'courses_data.csv'.")