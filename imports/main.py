from Objects.animals import Dog

if __name__ == "__main__":
    max = Dog("Max", 40, 16)
    print(max.dump_json())
