import queue

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
