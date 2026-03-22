import cv2


def extract_message(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found")

    bits = []

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            for k in range(3):  # RGB channels
                bits.append(str(img[i][j][k] & 1))

    message = ""
    for i in range(0, len(bits), 8):
        byte = bits[i : i + 8]
        if len(byte) < 8:
            break

        char = chr(int("".join(byte), 2))

        if char == "\x00":
            break

        if "###END###" in message:
            message = message.split("###END###")[0]
            break

        message += char

    return message


msg = extract_message("data/compromised_manual.png")
print("Extracted message:", msg)
