#!/usr/bin/env python3
"""a Python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        List of students sorted by average score in descending order.
    """
    students = list_all(mongo_collection)
    for student in students:
        total_score = sum(topic['score'] for topic in student['topics'])
        average_score = total_score / len(student['topics'])
        student['averageScore'] = average_score

    sorted_students = sorted(
            students, key=lambda x: x['averageScore'], reverse=True
            )
    return sorted_students
