import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def swap(A, i, j):
    """Helper function to swap elements i and j of list A."""

    if i != j:
        A[i], A[j] = A[j], A[i]


def insertionsort(A):
    """In-place insertion sort."""

    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A


def quicksort(A, start, end):
    """In-place quicksort."""

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A

    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)


if __name__ == "__main__":

    N = int(input("Enter number of integers: "))
    method_msg = "Enter sorting method:\n(i)nsertion\n(q)uick\n"
    method = input(method_msg)

    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)

    if  method == "i":
        title = "Insertion sort"
        generator = insertionsort(A)
    elif method == "q":
        title = "Quicksort"
        generator = quicksort(A, 0, N - 1)

    fig, ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)), A, align="edge")

    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))

    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=1,
        repeat=False)
    plt.show()