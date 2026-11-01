from python.spel_fabriek import Spel
from python.save import slaag_op

spel = Spel(debug=False)


def main():
    spel.spel_loop()
    slaag_op("src/txt/opslaag_tekst.txt",spel)


if __name__ == "__main__":
    main()