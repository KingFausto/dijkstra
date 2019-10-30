from graph import Graph


def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    for i, row in enumerate(data[1:], start=1):
        row = row.replace('  ', ' ')
        data[i] = list(map(int, row.split()))

    start, end = data[1]
    matrix = data[2:]

    graph = Graph(matrix)
    dijkstra = graph.dijkstra(start, end)
    print(dijkstra)

if __name__ == "__main__":
    main()
