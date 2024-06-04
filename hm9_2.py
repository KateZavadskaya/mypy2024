""" Task 2: count candles """


def solution(nw_candls, candle_leftover):

    """ Function count candles to burn  """

    tot_candles = nw_candls
    while nw_candls >= candle_leftover:
        tot_candles += nw_candls // candle_leftover
        nw_candls = nw_candls // candle_leftover + nw_candls % candle_leftover
    return tot_candles


print(solution(15, 5))

assert solution(5, 2) == 9, "Incorrect count"
assert solution(1, 2) == 1, "Incorrect count"
assert solution(15, 5) == 18, "Incorrect count"
assert solution(12, 2) == 23, "Incorrect count"
assert solution(6, 4) == 7, "Incorrect count"
assert solution(13, 5) == 16, "Incorrect count"
assert solution(2, 3) == 2, "Incorrect count"
