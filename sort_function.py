from typing import Literal


def sort(width: float, height: float, length: float, mass: float) -> Literal['standard', 'special', 'rejected']:
    """
    Sort function that takes width, height, length, and mass parameters of a package and
    returns its classification.

    Args:
        width: width value in cm
        height: height value in cm
        length: length value in cm
        mass: mass value in kg

    Returns:
        The classification of the package as 'standard', 'special', or 'rejected'

    Raises:
        ValueError: If inputs are not valid numbers or if any value is less than or equal to 0
    """

    # Validate all values are numeric
    try:
        float(width)
        float(height)
        float(length)
        float(mass)
    except ValueError:
        raise ValueError("All values must be numeric")

    if any(value <= 0 for value in (width, height, length, mass)):
        raise ValueError("All values must be greater than 0")

    # Calculate volume
    volume = width * height * length

    # Determine if package is bulky
    bulky = volume >= 1000000 or any(dim >= 150 for dim in (width, height, length))

    # Determine if package is heavy
    heavy = mass >= 20

    # Classify package
    if bulky and heavy:
        return 'rejected'
    elif bulky or heavy:
        return 'special'
    else:
        return 'standard'
