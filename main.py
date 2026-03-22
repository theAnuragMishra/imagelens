from stegano import lsb


def main():
    input_image = "data/scene.png"

    secret = "This image is compromised"

    output_image = lsb.hide(input_image, secret)

    output_image.save("compromised.png")


if __name__ == "__main__":
    main()
