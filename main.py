class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right


def insert(root, point, depth=0):
    if root is None:
        return Node(point)

    axis = depth % len(point)
    if point[axis] < root.point[axis]:
        root.left = insert(root.left, point, depth + 1)
    else:
        root.right = insert(root.right, point, depth + 1)

    return root


def range_search(root, low, high, depth=0, result=[]):
    if root is None:
        return

    axis = depth % len(low)

    if low[axis] <= root.point[axis] <= high[axis]:
        result.append(root.point)

    if low[axis] < root.point[axis]:
        range_search(root.left, low, high, depth + 1, result)

    if high[axis] > root.point[axis]:
        range_search(root.right, low, high, depth + 1, result)


def main():
    root = None
    points = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]

    for point in points:
        root = insert(root, point)

    while True:
        try:
            low = [float(x) for x in input("Enter lower bound coordinates (comma-separated): ").split(",")]
            high = [float(x) for x in input("Enter upper bound coordinates (comma-separated): ").split(",")]

            result = []
            range_search(root, low, high, result=result)

            if result:
                print("Points within the specified range:")
                for point in result:
                    print(point)
            else:
                print("No points found within the specified range.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        repeat = input("Do you want to perform another range search? (y/n): ").lower()
        if repeat != 'y':
            break


if __name__ == '__main__':
    main()
