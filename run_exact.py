import vqeex


def main():
    try:
        from pennylane import numpy as pnp
    except ModuleNotFoundError:
        pnp = None

    r = 1.88973
    symbols = ["H", "H", "H", "H"]
    coords = [
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 3.0 * r],
        [0.0, 0.0, 6.0 * r],
        [0.0, 0.0, 9.0 * r],
    ]
    geometry = (
        pnp.array(coords, dtype=float, requires_grad=False) if pnp is not None else coords
    )

    active_electrons = 4
    active_orbitals = 4
    charge = 0

    params = vqeex.gs_exact(
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

