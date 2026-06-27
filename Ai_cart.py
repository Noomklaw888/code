import math
import random

# =====================================================================
# 1. CORE ENGINE (Value Object)
# =====================================================================
class Value:
    def __init__(self, data, _children=()):
        self.data = data
        self.grad = 0.0                 # The glowing arrow score
        self._backward = lambda: None   # Local math shortcut placeholder
        self._prev = set(_children)     # The parent tracker

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other))
        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other))
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    # SUBTRACTION TRICK: Adding a negative number
    def __sub__(self, other):
        return self + (other * -1)

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,))
        def _backward():
            self.grad += (1.0 - t**2) * out.grad
        out._backward = _backward
        return out
    
    def backward(self):
        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)
        
        self.grad = 1.0
        for node in reversed(topo):
            node._backward()

# =====================================================================
# 2. NEURAL NETWORK LAYERS (The Neuron Cake)
# =====================================================================
class Neuron:
    def __init__(self, nin):
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(random.uniform(-1,1))
        
    def __call__(self, x):
        # Calculate: (w1*x1 + w2*x2) + bias
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        out = act.tanh()
        return out
        
    def parameters(self):
        return self.w + [self.b]

class Layer:
    def __init__(self, nin, nout):
        self.neurons = [Neuron(nin) for _ in range(nout)]
        
    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        return outs[0] if len(outs) == 1 else outs
        
    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]

class MLP:
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1]) for i in range(len(nouts))]
        
    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
        
    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

# =====================================================================
# 3. INTERACTIVE GAME & SIMULATION
# =====================================================================
# Initialize our network with 2 inputs (Distance, Speed)
n = MLP(2, [4, 4, 1])

playing = True
print("This is a program that simulates an AI golf cart that automatically stops.")
input("Press Enter to start...")

while playing:
    wipe = input("Wipe AI memory?(y, other)").lower
    if wipe == 'y':
        n = MLP(2, [4,4,1])
    train = input("Want to skip training? (y to skip, or press Enter to train): ").lower()
    if train != "y":
        print("\n--- Training Started ---")
        
        # 2-element inputs: [Distance, Speed]
        xs = [
            [2.0, 3.0],
            [3.0, -1.0],
            [5.5, 10.0],
            [8.0, 1.0],
            [100.0, 10.0]
        ]
        ys = [1.0, -1.0, 1.0, -1.0, -1.0] # Targets (1.0 means Brake)

        # The Grand Learning Loop
        for step in range(100):
            # Forward Pass: Make a guess on all rows
            ypred = [n(x) for x in xs]
            
            # Squaring mistakes manually using multiplication (avoiding pow method)
            loss = Value(0.0)
            for ygt, yout in zip(ys, ypred):
                diff = yout - ygt
                loss = loss + (diff * diff)
             
            # Reset old arrows to zero before counting new ones
            for p in n.parameters():
                p.grad = 0.0
                
            # Backward Pass: Trace backward from the mistake
            loss.backward()
            
            # Optimization: Nudge every slider a tiny bit
            learning_rate = 0.05
            for p in n.parameters():
                p.data -= learning_rate * p.grad
                
            if (step + 1) % 20 == 0:
                print(f"Step {step+1:2d} | Mistake Score: {loss.data:.4f}")

        print("\nFinal Training Predictions:")
        for target, guess in zip(ys, ypred):
            print(f"Target: {target:2.1f} | AI Guess: {guess.data: .4f}")
        print("We're done training the cart!\n")

    # Safe User Inputs
    while True:
        s = input("Enter the speed of the golf cart (e.g., 2): ")
        try:
            s = float(s)
            break  
        except ValueError:
            print("That's not a valid number. Try again.")

    while True:
        x = input("Enter the starting distance to the wall (e.g., 15): ")
        try:
            x = float(x)
            break  
        except ValueError:
            print("That's not a valid number. Try again.")

    print(f"\nSpeed: {s} FPS")
    
    # Run frame-by-frame live simulation
    for i in range(int(x) + 1):
        current_distance = x - (i * s)
        
        if current_distance <= 0:
            print("Distance: 0 ft")
            print("CRASH!!! You hit the wall!")
            print("That was not a smart AI... Maybe retrain it.")
            input("Press Enter to continue...")
            break
        
        #these 2 lines here are the actual query    
        new_scenario = [float(current_distance), float(s)]
        prediction = n(new_scenario)
        
        print(f"Distance: {current_distance:.1f} ft | AI Prediction: {prediction.data:.4f}")

        if prediction.data > 0.5:       
            if current_distance > 5:
                print("The cart stopped too early")
            else:
                print("Brake activated! The cart stopped safely!")
            break
        else:
            print("Let's keep rolling!")
            
    pa = input('\nType "x" to quit, or press Enter to play again: ').lower().strip()
    if pa == "x":
        playing = False
        print("Byeeeeeeee!!!")
        break
