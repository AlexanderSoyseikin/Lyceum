def take_large_banknotes(banknotes):
    for i in range(len(banknotes)):
        result = []
        if banknotes[i] > 10:
            result.append(banknotes[str(i)])
        if len(banknotes) != 0:
            return result
        return []