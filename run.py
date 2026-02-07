import Vqe


def main():
    r = 1.88973
    symbols = ["H", "H", "H", "H"]
    geometry = [
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 3.0 * r],
        [0.0, 0.0, 6.0 * r],
        [0.0, 0.0, 9.0 * r],
    ]

    active_electrons = 4
    active_orbitals = 4
    charge = 0
   
    params = Vqe.gs_exact(
        symbols,
        geometry,
        active_electrons,
        active_orbitals,
        charge,
        max_iter=100,
    )
    print("\nReturned parameter vector length:", len(params))


if __name__ == "__main__":
    main()
