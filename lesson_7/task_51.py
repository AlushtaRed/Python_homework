values = [0, 2, 10, 6]

def same_by(characteristic, objects):
    if len(set(map(characteristic, objects))) in (0, 1):
        return True
    return False

print(same_by(lambda x: x % 2, values))
print(same_by(lambda x: x % 2, []))
print(same_by(lambda x: x > 2, values))