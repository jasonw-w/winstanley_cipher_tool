import argparse
from toolbox.ceasar import caesar


CIPHER_REGISTRY = {
    "caesar": caesar,
}


def build_parser():
    parser = argparse.ArgumentParser(description="Cipher toolbox")
    parser.add_argument(
        "cipher",
        choices=sorted(CIPHER_REGISTRY.keys()),
        help="Cipher to use",
    )
    parser.add_argument("text", help="Text to encrypt or decrypt")
    parser.add_argument("shift", type=int, help="Shift amount")
    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt"],
        help="Choose whether to encrypt or decrypt",
    )
    return parser


def get_cipher(name):
    cipher_class = CIPHER_REGISTRY[name]
    return cipher_class()


def main():
    parser = build_parser()
    args = parser.parse_args()

    cipher = get_cipher(args.cipher)

    if args.mode == "encrypt":
        result = cipher.plain2cipher(args.text, args.shift)
    else:
        result = cipher.cipher2plain(args.text, args.shift)
    print(result)


if __name__ == "__main__":
    main()