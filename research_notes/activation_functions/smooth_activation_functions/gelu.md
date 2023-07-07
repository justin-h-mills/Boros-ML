# **Gaussian Error Linear Units (GELU)**

<br>

The GELU is a commonly used activation function in deep learning models. It introduces smooth and differentiable nonlinearity by leveraging the standard Gaussian cumulative distribution function (CDF).

The GELU activation function applies the standard Gaussian CDF to the input, resulting in a smooth behavior that goes beyond simply gating inputs by their sign, as in ReLUs.

While various mathematical expressions, such as the sigmoid or hyperbolic tangent functions, can approximate the GELU function, modern deep learning frameworks like PyTorch often provide exact and efficient implementations, eliminating the need for such approximations.

GELU has gained popularity and is widely used in state-of-the-art models such as GPT-3, BERT, and Transformers. Its smooth nonlinearity and differentiability make it suitable for deep learning tasks, enabling effective gradient-based optimization during training.

In summary, the GELU activation function, based on the standard Gaussian CDF, offers a smooth nonlinearity for deep learning models. It is extensively utilized in cutting-edge models like GPT-3, BERT, and Transformers due to its ability to capture complex patterns effectively and its efficient implementation in modern deep learning frameworks.

<br>

## **Definition**

<br>

### **Exact Definition of GELU**

The exact definition of the GELU function involves the use of the error function (erf) and is given by:

$$GELU(x) = xP(X \le x)= x\Phi(x) = x \cdot \frac{1}{2} [1+erf(\frac{x}{\sqrt{2}})]$$

$$GELU\grave{(}x) \approx \frac{\alpha x}{\sqrt{2\pi}}e^{-\frac{(\alpha x)^2}{2}}+\Phi(\alpha x)$$

In this definition, $\Phi(x)$ represents the standard Gaussian cumulative distribution function, and $X \sim N(0, 1)$ refers to the cumulative distribution function of the standard normal distribution. The inclusion of the error function helps introduce the desired smooth and differentiable nonlinearity.

<br>

### **Approximations of GELU**

1. Polynomial Approximation:

$$GELU(x) \approx 0.5x(1+tanh(\sqrt{\frac{2}{\pi}}))(x+0.044715x^3)$$

$$GELU\grave{(}x) \approx 0.5(1+tanh(\sqrt{\frac{2}{\pi}}(x+0.044715x^3))+0.5x\cdot sech^2(\sqrt{\frac{2}{\pi}}(x+0.044715x^3))\cdot \sqrt{\frac{2}{\pi}}(1+3\cdot 0.044715x^2))$$

2. Sigmoid-based Approximation:

$$GELU(x) \approx x\sigma(1.702x)$$

$$GELU\grave{(}x) \approx \sigma(1.702x) + 1.702x \cdot \sigma(1.702x)(1-\sigma(1.702x))$$

These approximations offer a faster computation of the GELU function compared to the exact definition involving the error function. However, it's important to note that they may introduce a slight reduction in accuracy.

<br>

## **Properties**

- **Smooth and Continuous Nonlinearity:** GELU provides a smooth and continuous nonlinearity, making it advantageous in scenarios where the model needs to capture complex patterns or make fine-grained predictions.
- **Differentiable Everywhere:** GELU is differentiable everywhere, enabling the use of gradient-based optimization algorithms like backpropagation. This facilitates efficient learning and convergence.
- **Exact and Efficient Implementation:** Modern deep learning frameworks often offer an exact and efficient implementation of the GELU function, eliminating the need for approximations and ensuring computational efficiency.
- **Effective in Transformer Architectures:** GELU has demonstrated effectiveness in transformer architectures like GPT-3 and BERT. Its smoothness and nonlinearity make it well-suited for modeling complex relationships and capturing dependencies in sequential and attention-based models.

<br>

## **Advantages**

* Provides a smooth and continuous nonlinearity, which can capture complex patterns effectively.
* Allows for the use of gradient-based optimization algorithms like backpropagation, enabling efficient learning and convergence.
* Many modern deep learning frameworks provide an exact and efficient implementation of GELU, ensuring accurate and fast computations.
* Shown effectiveness in transformer architectures, demonstrating its suitability for modeling complex relationships and capturing dependencies.

<br>

## **Limitations**

* Does not have a clear interpretation in terms of probabilities or thresholding, which can make it harder to interpret and understand the behavior of the model.
* Predefined mathematical form, potentially lacking the flexibility offered by activations with learnable parameters or customized adjustments based on data characteristics or task requirements.
* Availability and performance of the exact GELU implementation may vary across different deep learning frameworks, potentially introducing compatibility issues or variations in performance.

<br>

### **Note:**

It's important to note that the advantages and limitations of using a particular activation function may vary depending on the specific context and problem at hand. Experimentation and evaluation on a case-by-case basis are recommended to determine the most suitable activation function for a given neural network.

<br>

---

<br>

## References

- [GELU on Papers with Code](https://paperswithcode.com/method/gelu)
- [(Research Paper) Gaussian Error Linear Units (GELUs)](https://arxiv.org/pdf/1606.08415v5.pdf)
- [(Research Paper) GELU Activation Function in Deep Learning: A Comprehensive Mathematical Analysis and Performance](https://www.researchgate.net/publication/370949533_GELU_Activation_Function_in_Deep_Learning_A_Comprehensive_Mathematical_Analysis_and_Performance)

<br>

---

The references provided above offer more in-depth information on the GELU activation function and related research. Feel free to explore these resources for further insights and a deeper understanding of the topic.