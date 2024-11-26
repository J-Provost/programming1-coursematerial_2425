def pad_right(xs, length, padding):
    if len(xs) < length:
        xs.extend([padding] * (length - len(xs)))
