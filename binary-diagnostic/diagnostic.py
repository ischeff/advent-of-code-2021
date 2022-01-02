def load_input(data):
    with open(data) as f:
        report = [int(i) for i in f]
        return report

if __name__ == "__main__":
    print(load_input("data.txt"))
