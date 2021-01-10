# Designer PDF Viewer
import string


def designerPdfViewer(h, word):
    count = 0
    maxx = 0
    for s in word:
        maxx = max(maxx, h[string.ascii_letters.index(s)])
        count += 1

    return maxx * count


h = list(map(int, "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7".split()))
word = 'zaba'
print(designerPdfViewer(h, word))
