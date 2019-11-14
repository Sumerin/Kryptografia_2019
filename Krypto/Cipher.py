import queue, locale

def railFence_encipher(message, h):
    layers = {}
    for i in range(h):
        layers[i] = []
    layer = 0
    is_down = True
    for char in message:

        layers[layer].append(char)

        if is_down:
            layer += 1
        else:
            layer -= 1

        if layer == h-1:
            is_down = False
        elif layer == 0:
            is_down = True

    encoded = ""
    for i in range(h):
        encoded += "".join(layers[i])
    return encoded


def railFence_decipher(message, h):
    layers_count = {}

    for i in range(h):
        layers_count[i] = 0

    layer = 0
    is_down = True
    for _ in message:
        layers_count[layer] += 1
        if is_down:
            layer += 1
        else:
            layer -= 1

        if layer == h-1:
            is_down = False
        elif layer == 0:
            is_down = True

    layers = {}
    idx = 0
    for i in range(h):
        count = layers_count[i]
        layers[i] = queue.Queue()
        for char in message[idx:(idx + count)]:
            layers[i].put(char)
        idx += count
    layer = 0
    is_down = True
    result = []
    for _ in message:
        char = layers[layer].get()
        result.append(char)

        if is_down:
            layer += 1
        else:
            layer -= 1

        if layer == h-1:
            is_down = False
        elif layer == 0:
            is_down = True

    decoded = "".join(result)
    return decoded


def matrix_cipher(message, w):
    matrix = ["" for w in range(w)]
    position = 0
    result = []
    r = len(message) % (w * w)
    if r != 0:
        message += ''.join("=" for _ in range((w * w) - r))

    while position < len(message):
        for row in range(w):
            start = position
            end = position + w
            matrix[row] = message[start:end]
            position = end
        for col in range(w):
            for row in range(w):
                result.append(matrix[row][col])

    return "".join(result)


def column_key_change(key):
    n = len(key)
    locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")
    sorted_key = sorted(key, key=locale.strxfrm)
    result = {}
    key_dict = {i: key[i] for i in range(n)}
    for i in range(n):
        char = sorted_key[i]
        for (k, v) in key_dict.items():
            if v == char:
                result[i] = k
                del key_dict[k]
                break

    return result, n


def column_encipher(message, key):

    pi, n = column_key_change(key)
    return column_encipher_pi_n(message, pi, n)


def column_encipher_pi_n(message, pi, n):

    matrix = []
    for _ in range(n):
        matrix.append([])

    for i in range(len(message)):
        char = message[i]
        idx = i % n
        matrix[idx].append(char)

    result = []
    for i in range(n):
        idx = pi[i]
        column_value = "".join(matrix[idx])
        result.append(column_value)

    return "".join(result)


def column_decipher(message, key):

    pi, n = column_key_change(key)
    return column_decipher_pi_n(message, pi, n)


def column_decipher_pi_n(message, pi, n):

    col_count = int(len(message)/n)
    col_with_extra_element = len(message) % n

    matrix = []
    for _ in range(n):
        matrix.append([])

    pos = 0
    for i in range(n):
        start = pos
        end = pos + col_count
        matrix_idx = pi[i]
        if matrix_idx < col_with_extra_element:
            end += 1
        matrix[matrix_idx] = message[start:end]
        pos = end

    result = []
    for row in range(col_count):
        for col in range(n):
            result.append(matrix[col][row])

    for col in range(col_with_extra_element):
        result.append(matrix[col][col_count])

    return "".join(result)


