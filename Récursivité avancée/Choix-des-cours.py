def choose(first, count, total_courses, choices_to_make, choices):
    if count == 0:
        print(*choices)
        return
    for course in range(first, total_courses - count + 2):
        choices[choices_to_make - count] = course
        choose(course + 1, count - 1, total_courses, choices_to_make, choices)

def main():
    total_courses, choices_to_make = map(int, input().split())
    if choices_to_make <= total_courses:
        choices = [None] * choices_to_make
        choose(1, choices_to_make, total_courses, choices_to_make, choices)

main()
