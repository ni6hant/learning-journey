# Write your solution here
import urllib.request, json

def retrieve_all():
    active_course = []
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = json.loads(my_request.read())
    for item in data:
        if item['enabled']:
            active_course.append((item['fullName'],item['name'],item['year'],sum(item['exercises'])))
    return active_course

def retrieve_course(course_name:str):
    my_request = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    data = json.loads(my_request.read())

if __name__ == "__main__":
    retrieve_course("docker2019")