# Sort packages function

Sort function that classifies packages based on width, height, length, and mass parameters.
Packages are first sorted using the following criteria:
- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm3 or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

The package is then classified as:
- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

## How to run:
```
uv run sort.py <width>, <height>, <length>, <mass>
```

## Running the tests:
```
uv run pytest -svvv
```
