"""Determinant subspace construction used by QSC-EOM.

`inite(n_electrons, n_spin_orbitals)` returns a list of determinants (occupation
lists) consisting of:
  - all spin-conserving single excitations relative to the HF reference
  - all spin-conserving double excitations relative to the HF reference

The ordering is kept compatible with the original implementation in this repo.
"""


def inite(n_electrons, n_spin_orbitals):
    """Return the single+double excitation determinant list for a closed-shell HF reference."""
    n_electrons = int(n_electrons)
    n_spin_orbitals = int(n_spin_orbitals)

    dets = []

    # Singles.
    for hole in range(n_electrons):
        virt_base = n_spin_orbitals - n_electrons
        while virt_base < n_spin_orbitals:
            det = []
            for occ in range(n_electrons):
                if occ == hole:
                    det.append(virt_base if (hole % 2) == 0 else virt_base + 1)
                    virt_base += 2
                else:
                    det.append(occ)
            dets.append(det)

    # Doubles.
    for hole1 in range(n_electrons):
        for hole2 in range(hole1 + 1, n_electrons):
            same_spin = (hole1 % 2) == (hole2 % 2)
            for virt1 in range(n_electrons, n_spin_orbitals, 2):
                for virt2 in range(n_electrons, n_spin_orbitals, 2):
                    # Disallow exciting two same-spin electrons into the same spin-orbital.
                    if same_spin and virt1 == virt2:
                        continue
                    # Avoid duplicates for same-spin pairs.
                    if same_spin and virt2 < virt1:
                        continue

                    det = []
                    for occ in range(n_electrons):
                        if occ == hole1:
                            det.append(virt1 if (hole1 % 2) == 0 else virt1 + 1)
                        elif occ == hole2:
                            det.append(virt2 if (hole2 % 2) == 0 else virt2 + 1)
                        else:
                            det.append(occ)
                    dets.append(det)

    return dets
