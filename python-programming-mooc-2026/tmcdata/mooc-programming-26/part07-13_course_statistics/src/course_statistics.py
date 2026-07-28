# Write your solution here
import json
import urllib.request


def retrieve_all():
    active_course = []
    my_request = urllib.request.urlopen(
        "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    )
    data = json.loads(my_request.read())
    for item in data:
        if item["enabled"]:
            active_course.append(
                (item["fullName"], item["name"], item["year"], sum(item["exercises"]))
            )
    return active_course


def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen(
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    )
    data = json.loads(my_request.read())
    course_details = {}

    course_details["weeks"] = len(data)
    course_details["students"] = max(item["students"] for item in data.values())
    course_details["hours"] = sum(item["hour_total"] for item in data.values())
    course_details["hours_average"] = (
        course_details["hours"] // course_details["students"]
    )
    course_details["exercises"] = sum(item["exercise_total"] for item in data.values())
    course_details["exercises_average"] = (
        course_details["exercises"] // course_details["students"]
    )
    return course_details


if __name__ == "__main__":
    print(retrieve_course("docker2019"))
