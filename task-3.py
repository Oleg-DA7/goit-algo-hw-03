def print_tower_state(poles):
    print("\nСтан:", *[f"{p}:{sorted(poles[p], reverse=True)}" for p in 'ABC'], sep=' ')

def hanoi_towers(n, source='A', aux='B', dest='C', poles=None):
    if n <= 0:
        return
    hanoi_towers(n - 1, source, dest, aux, poles)
    poles[source].pop()
    poles[dest].append(n)
    print(f"Диск {n}: {source} -> {dest}")
    print_tower_state(poles)
    hanoi_towers(n - 1, aux, source, dest, poles)

def main():
    n = int(input("Дисків: "))
    if n <= 0:
        raise ValueError("Число має бути > 0")
    poles = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print("\nПочатковий стан:")
    print_tower_state(poles)
    print(f"\nКроки для {n} дисків (A -> C):")
    hanoi_towers(n, poles=poles)
 
if __name__ == "__main__":
    main()