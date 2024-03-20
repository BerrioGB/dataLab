import pandas as pd
import numpy as np
from datetime import datetime
# Course Categories Data
course_categories_data = {
 "category_id": [1, 2, 3, 4, 5],
 "category_name": ["Technology", "Business", "Art", "Science", "Health"]
}
# Course Levels Data
course_levels_data = {
 "level_id": [101, 102, 103],
 "level_name": ["Beginner", "Intermediate", "Advanced"]
}
# Courses Data
np.random.seed(0)
courses_data = {
 "course_id": np.arange(1, 101),
 "course_name": [f"Course{i}" for i in range(1, 101)],
 "category_id": np.random.choice([1, 2, 3, 4, 5], 100),
 "level_id": np.random.choice([101, 102, 103], 100),
 "start_date": [datetime(2021, np.random.randint(1, 13), np.random.randint(1, 29)) for _ in range(100)]
}
# Convert to DataFrame
course_categories_df = pd.DataFrame(course_categories_data)
course_levels_df = pd.DataFrame(course_levels_data)
courses_df = pd.DataFrame(courses_data)

#impresiones
course_categories_df = pd.DataFrame(course_categories_data)
print("Course Categories DataFrame:")
print(course_categories_df)

course_levels_df = pd.DataFrame(course_levels_data)
print("\nCourse Levels DataFrame:")
print(course_levels_df)

courses_df = pd.DataFrame(courses_data)
print("\nCourses DataFrame:")
print(courses_df)
