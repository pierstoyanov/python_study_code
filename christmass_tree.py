def christmass_tree(height: int, t=3, tree=None):
    if height == 0:
        return '\n'.join(tree)

    if not tree:
        tree = []
        tree.append(f"\x1b[2;33;40m{' ' * (height)}*{' ' * (height)}\x1b[0m")

    tree.append(f"\x1b[2;32;40m{' ' * int(height - 1)}{'#' * t}{' ' * int(height - 1)}\x1b[0m")
    return christmass_tree(height - 1, t + 2, tree)


if __name__ == '__main__':
    print(christmass_tree(5))
