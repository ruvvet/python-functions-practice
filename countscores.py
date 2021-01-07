def count_scores(scores):
    final_scores = {}
    for score in scores:
        if score['name'] in final_scores.keys():
            final_scores[score['name']] += score['score']
        else:
            final_scores[score['name']] = score['score']

    return (final_scores)


scores = [
    {"name": "Pete", "score": 2},
    {"name": "Dexter", "score": 2},
    {"name": "Mike", "score": 2},
    {"name": "Dexter", "score": 2},
    {"name": "Mike", "score": 2},
    {"name": "Pete", "score": 2},
    {"name": "Dexter", "score": 2}
]


print(count_scores(scores))
