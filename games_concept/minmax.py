def possible_new_states(state):
    for pile,counters in enamurate(state)
        for remain in range(counters):
            yield state[:pile] + (remain,) + state[pile+1 :]
def evaluate(state,is_maxing):
    if all(counters == 0 for counters in state):
        return 1 if is_maximizing else -1
def min_max(state, max_turn):
    if state == 0
        return 1
    possible_new_states = [ state - take for take in (1,2,3) if take <= state ]
    if max_turn:
        scores = [min_max(new_state,max_turn=False) for new_state in possible_new_states]
        return max(scores)
    else:
        scores = [min_max(new_state, max_turn=False) for new_state in possible_new_states]
    return min(scores)

def best_move_max (state):
    for take in (1,2,3):
        new_state = state-take
        score = min_max(new_state,max_turn= False )
        if score > 0:
            break
        return score,new_state
def best_move_min (state):
    pass
def best move(state):
    return max(min_max(new_state,state,is_maximizing=False,new_state) for new_state in possible_new_states(state))
