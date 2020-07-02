# def import_circle_to_csv(path: str):
#     import csv
#     with open(path) as csv_file:
#         csv_reader = csv.reader(csv_file)
#         headers = next(csv_reader)

#         circles = list()
#         for row in csv_reader:
#             attrs = dict(((headers[i], value) for i, value in enumerate(row)))
#             circles.append(Circle(**attrs))

#     Circle.objects.bulk_create(circles)

#     for circle in circles:
#         print(f'circle saved success: {circle}')


def import_circle_to_csv(path: str):
    import csv
    with open(path) as csv_file:
        circles = [Circle(**attrs) for attrs in csv.DictReader(csv_file)]

    Circle.objects.bulk_create(circles)
    for circle in circles:
        print(f'circle saved success: {circle}')
