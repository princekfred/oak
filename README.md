# oak

Small PennyLane VQE example.

## Setup

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python run.py
```

`Vqe.gs_exact` will prefer the `lightning.qubit` device and fall back to `default.qubit` if Lightning isn't available.

## Exact (non‑Trotterized) UCCSD (small systems)

`vqeex.gs_exact` constructs the *combined* UCCSD generator and applies `exp(-iG)`
via dense matrix exponentiation (not scalable, but removes Trotter error):

```bash
python run_exact.py
```

To run the QSC-EOM excited-state routine on top of the exact ansatz:

```bash
python run_exact.py qsceom
```

If you don't have PySCF installed, use the built-in differentiable Hartree-Fock backend:

```bash
python run_exact.py qsceom dhf
```
