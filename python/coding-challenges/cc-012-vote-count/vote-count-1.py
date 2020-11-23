# Vote Count

from collections import Counter

votes = ["A", "A", "A", "B", "C", "A"]

votes_counter = Counter(votes)

majority_vote = votes_counter.most_common()

winner, max_votes = majority_vote[0]

print(majority_vote)

print(f"{winner} won with {max_votes} votes.")
