import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# Definir transformações de pré-processamento
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # Normalização dos valores RGB
])

# Baixar e carregar o conjunto de dados CIFAR-10
trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)

# Definir a arquitetura da rede neural
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.features = torchvision.models.vgg16(pretrained=True).features
        self.classifier = nn.Sequential(
            nn.Linear(512 * 7 * 7, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(True),
            nn.Dropout(),
            nn.Linear(4096, 10)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

net = Net()

# Definir função de perda e otimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# Treinar a rede neural
for epoch in range(5):  # Executar 5 épocas de treinamento
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data

        optimizer.zero_grad()

        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if i % 2000 == 1999:
            print(f'Epoch: {epoch + 1}, Batch: {i + 1}, Loss: {running_loss / 2000}')
            running_loss = 0.0

print('Treinamento concluído')

# Salvar o modelo treinado
PATH = './cifar_net.pth'
torch.save(net.state_dict(), PATH)
