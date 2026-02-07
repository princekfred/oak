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
