import numpy as np

from scipy.special import erf

def inplace_elu(X: np.ndarray, alpha: float = 1.0) -> None:
    """Apply the ELU activation function element-wise to the input array.

    `ELU(x) = x: if x > 0, α(eˣ-1): if x <= 0`

    Parameters:
        X : Input array
        alpha: ELU coefficient (slope of the negative region).
    """
    mask = X < 0
    X[mask] = alpha * (np.exp(X[mask])-1)

def inplace_gelu(X: np.ndarray):
    """Apply the GELU activation function element-wise to the input array.

    `GELU(x) ≈ 0.5x(1 + erf(x / sqrt(2)))`

    where,
    - `erf(): returns the error function of a complex argument`

    Parameters:
        X: Input array.
    """
    X[:] *= 0.5 * (1 + erf(X / np.sqrt(2)))

def inplace_glu(X: np.ndarray, gate: np.ndarray) -> None:
    """Apply the GELU activation function element-wise to the input array.

    `GLU(x, g) = x ⊙ σ(g)`

    where,
    - `⊙: element-wise multiplication`
    - `x: input array` 
    - `g: gate array`
    - `σ: sigmoid activation function`

    Parameters:
        X: Input array.
        gate: Gate array.
    """
    X[:] *= 1 / (1 + np.exp(-gate))

def inplace_leaky_relu(X: np.ndarray, alpha: float = 1.0) -> None:
    """Apply the Leaky ReLU activation function element-wise to the input array.

    `Leaky ReLU(x) = x: if x >= 0, αx: if x < 0`

    Parameters:
        X: Input array.
        alpha: Leaky coefficient (slope of the negative region).
    """
    mask = X < 0
    X[mask] *= alpha

def inplace_relu(X: np.ndarray) -> None:
    """Apply the ReLU activation function element-wise to the input array.

    `ReLU(x) = x: if x > 0, 0: if x <= 0`

    Parameters:
        X: Input array.
    """
    mask = X < 0
    X[mask] = 0

def inplace_sigmoid(X: np.ndarray) -> None:
    """Apply the Sigmoid activation function element-wise to the input array.

    `Sigmoid(x) = 1 / (1 + e⁻ˣ)`

    Parameters:
        X: Input array.
    """
    X[:] = 1 / (1 + np.exp(-X))

def inplace_silu(X: np.ndarray) -> None:
    """Apply the SiLU activation function element-wise to the input array.

    `SiLU(x) = xσ(x)`

    where,
        - `σ: sigmoid activation function`

    Parameters:
        X: Input array.
    """
    X[:] *= 1 / (1 + np.exp(-X))

def inplace_softmax(X: np.ndarray) -> None:
    """Apply the Softmax activation function element-wise to the input array.

    `Softmax(x) = e^xᵢ / sum(e^xⱼ)`

    where,
        - `xᵢ: input value at index i`
        - `xⱼ: all values over all j indices`

    Parameters:
        X: Input array.
    """
    e_x = np.exp(X - np.max(X))
    X[:] /= np.sum(e_x)

def inplace_tanh(X: np.ndarray) -> None:
    """Apply the Tanh activation function element-wise to the input array.

    `Tanh(x) = (eˣ - e⁻ˣ) / (eˣ + e⁻ˣ)`

    Parameters:
        X: Input array.
    """
    X[:] = (np.exp(X)-np.exp(-X))/(np.exp(X)+np.exp(-X))