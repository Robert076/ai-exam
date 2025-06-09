# 🌎 ai-exam

Learn the AI exam questions just like you learned the driver's exam questions. For my fellow brothers at uni.

Most logic is taken from Mircea Maierean's cn-exam repo. This was just adapted to our AI exam.

### 🚀 Run the script:

1. Change directory

```bash
cd src
```

2. Start it up

```bash
python3 main.py
```

---

### ❗️ Some tips

Regarding this question:

> Select the correct combination: <br>
> a) Output type: Discrete, Output Distribution: Multinoulli, Output Layer: Linear, Cost Function: Cross Entropy. <br>
> b) Output type: Binary, Output Distribution: Bernoulli, Output Layer: Sigmoid, Cost Function: Binary Cross Entropy. <br>
> c) Output type: Continuous, Output Distribution: Gaussian, Output Layer: Softmax, Cost Function: MSE. <br>
> d) None of the above.

Discrete should have Softmax instead of linear, Continuous should have Linear output layer. They are backwards that's why only b is correct. The other question similar to this has all 3 (a b c) correct.
