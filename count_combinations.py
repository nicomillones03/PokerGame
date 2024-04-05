from Poker import Hand, Deck


def count_flushes(shuffle_times=10000):
    flush_count = 0
    for _ in range(shuffle_times):
        deck = Deck()
        deck.shuffle()
        hand = Hand(deck)
        if hand.is_flush:
            flush_count += 1
    return flush_count


def count_pair(shuffle_times=10000):
    pair_count = 0
    for _ in range(shuffle_times):
        deck = Deck()
        deck.shuffle()
        hand = Hand(deck)
        if hand.is_pair:
            pair_count += 1
    return pair_count
