command = input()

exam_results = {}

while command != "exam finished":
    tokens = command.split("-")
    if len(tokens) == 3:
        (username, language, points) = tokens
        points = int(points)
        if language not in exam_results:
            exam_results[language] = {}
        # for language_user in exam_results[language]:
        if username not in exam_results[language]:
            exam_results[language].update({username: [points]})
        else:
            if exam_results[language][username] == None:
                exam_results[language].update({username: [points]})
                break
            exam_results[language][username].append(points)
    else:
        username = tokens[0]
        for (language, value) in exam_results.items():
            for (user, p) in value.items():
                if username == user:
                    exam_results[language][user] = None
    command = input()

exam_results_by_users = {key: max(value) for (k, v) in exam_results.items() for (key, value) in v.items() if value != None}
exam_results_by_users_sorted = dict(sorted(exam_results_by_users.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
for (key, value) in exam_results_by_users_sorted.items():
    print(f"{key} | {value}")


language_counter = {}
for (key, value) in exam_results.items():
    count = 0
    for (k, v) in value.items():
        if v != None:
            count += len(v)
        else:
            count += 1

    language_counter[key] = count
language_counter_sorted = dict(sorted(language_counter.items(), key=lambda x: (-x[1], x[0])))
print("Submissions:")
for k, v in language_counter_sorted.items():
    print(f"{k} - {v}")
