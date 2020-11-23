# Vote Count

votes = ["A", "A", "A", "B", "C", "A"]

votes_dic = {}

for candidate in votes:
    if candidate in votes_dic:
        votes_dic[candidate] += 1
    else:
        votes_dic[candidate] = 1

    candidate_sorted = sorted(votes_dic.items(
    ), key=lambda candidate: candidate[1], reverse=True)

    winner, max_votes = candidate_sorted[0]

print(candidate_sorted)

print(f"{winner} won with {max_votes} votes.")
