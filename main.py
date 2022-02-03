import engine

if __name__ == '__main__':
    alive_cells = engine.step(100, frozenset([2, 4, 5, 8, 9, 10, 108]))
    print(alive_cells)
    print(type(alive_cells))
