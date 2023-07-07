# **Exponential Linear Unit (ELU)**

<br>

The Exponential Linear Unit (ELU) is an activation function used in neural networks. Unlike Rectified Linear Units (ReLUs), ELUs can have negative values, which helps push the average activation of units closer to zero, similar to the effect of batch normalization. However, ELUs achieve this with lower computational complexity. This shift towards zero speeds up learning by aligning the normal gradient with the unit's natural gradient, thanks to a reduced bias shift effect.

While other activation functions like Leaky ReLUs (LReLUs) and Parametric ReLUs (PReLUs) also allow negative values, they do not guarantee a robust deactivation state in the presence of noise. On the other hand, ELUs saturate to a negative value for smaller inputs, reducing the variation and information propagated forward through the network. This saturation helps mitigate the negative effects of noise on the network's performance.

<br>

## **Definition**

The exponential linear unit ELU with $0 < \alpha$ is defined as:

$$ELU(x)=\left\{ \begin{array}{cl} x & : \ x \gt 0 \\ \alpha (e^{x}-1) & : \ x \le 0 \end{array} \right.$$

$$ELU\grave{(}x)=\left\{ \begin{array}{cl} 1 & : \ x \gt 0 \\ ELU(x) + \alpha & : \ x \le 0 \end{array} \right.$$

Here, $\alpha$ controls the saturation value for negative net inputs.

<br>

## **Properties**

- **Improved Learning Speed:** ELUs accelerate learning, especially in deep neural networks, due to their smoothness and saturation properties.
- **Robustness To Noise:** ELUs have a noise-robust deactivation state, enabling them to handle noisy inputs without significantly impacting network performance.
- **Preservation Of Information:** ELUs saturate to negative values for smaller inputs, reducing variation and preventing over-amplification of certain inputs, potentially improving the network's representation power.
- **Closer Mean Activation To Zero:** By allowing negative values, ELUs shift the mean unit activations closer to zero, similar to batch normalization but with lower computational complexity.

<br>

## **Advantages**

- Improved learning speed, especially in deep neural networks.
- Robustness to noise, maintaining performance with noisy inputs.
- Preservation of information and reduced variation in smaller inputs.
- Closer mean activation to zero without requiring batch normalization.

<br>

## **Limitations**

- Slightly higher computational complexity compared to simpler activation functions like ReLU.
- Non-monotonic behavior, which can introduce challenges during optimization and training.
- Limited interpretability due to negative values and non-linear nature.
- Susceptibility to gradient vanishing or exploding issues, particularly in very deep networks.

<br>

### **Note:**

It's important to note that the advantages and limitations of using a particular activation function may vary depending on the specific context and problem at hand. Experimentation and evaluation on a case-by-case basis are recommended to determine the most suitable activation function for a given neural network.

<br>

---

<br>

## References

- [ELU on Papers with Code](https://paperswithcode.com/method/elu)
- [Research Paper: Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs)](https://arxiv.org/pdf/1511.07289v5.pdf)

<br>

---

The references provided above offer more in-depth information on the ELU activation function and related research. Feel free to explore these resources for further insights and a deeper understanding of the topic.