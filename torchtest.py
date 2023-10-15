import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt

# Create a simple linear regression model
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        x = self.fc(x)
        return x

# Create a dataset based on a 2*x function
x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)
y = 2*x + torch.rand(x.size()) * 0.2

# Initialize the model, loss function and optimizer
model = Net()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.2)

# Train the model
for t in range(200):
    prediction = model(x)
    loss = criterion(prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Plot the original 2*x function and the function learned by the model
plt.figure(figsize=(10,4))
plt.scatter(x.data.numpy(), y.data.numpy(), label='Original data')
plt.scatter(x.data.numpy(), prediction.data.numpy(), label='Fitted line')
plt.legend()
plt.show()
