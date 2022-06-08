import math
import random

def get_sample_size(n):
    return int(n/math.e)

# candidate[] represents talents of n candidates.
def get_best_candidate(candidate, n):
    hiring_cost = 100
    cost = 0

    sample_size = get_sample_size(n)
  
    # Finding best candidate in sample size
    best = 0; 
    for i in range(1, int(sample_size)):
        cost += hiring_cost
        if candidate[i] > candidate[best]:
            best = i
  
    # Finding the first best candidate that is better than best in sample.
    for i in range(sample_size, n):
        if candidate[i] >= candidate[best]:
            cost += hiring_cost
            best = i
            break
  
    if best >= sample_size:
        print("\nBest candidate found is", best + 1, "with score", candidate[best], "and cost:", cost)
    else:
        print("Best candidate not found")

def generate_score_card(n):
    score_cards = []
    for i in range(n):
        res = random.randint(1, 10)
        score_cards.append(res)
    return score_cards


if __name__ == "__main__":
    n = int(input("Number of candidates:\n"))
    
    score_cards = generate_score_card(n)
    

    print("Worst case:")
    get_best_candidate(score_cards, n)

    print("Randomize:")
    random.shuffle(score_cards)
    get_best_candidate(score_cards, n)