import os
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import wb
import torch
import torch.nn
import torch.optim

gdp = web.DataReader('ticker=RGDPUS','econdb')
print(gdp)
#prints to console the list of RGDP values (in millions of dollars)
#up until 2020-01-01



# df = gdp.unstack().T
# df.index = df.index.droplevel(0).astype(int)

# print(df)

dat = wb.download(indicator='NY.GDP.MKTP.CD',
        country=['US'], start=1979, end=2019)

df = dat.unstack().T
df.index = df.index.droplevel(0).astype(int)
print(df)

#Building the recurrent neural network
class Net(torch.nn.Module):
    
    def __init__(self, input_size, hidden_size):
        super(Net, self).__init__()
        self.rnn = torch.nn.LSTM(input_size, hidden_size)
        self.fc = torch.nn.Linear(hidden_size, 1)
        
    def forward(
        self, x):
        x = x[:, :, None]
        x, _ = self.rnn(x)
        x = self.fc(x)
        x = x[:, :, 0]
        return x

net = Net(input_size=1, hidden_size=5)
#print(net)

#training
#normalization of the network
df_scaled = df / df.loc[1999]

#training dataset and test dataset
years = df.index
train_seq_len = sum((years >= 1979) & (years < 1999))
test_seq_len = sum(years >= 1999)

#print ('Length of training set = {}, Length of test set = {}'.format(
#        train_seq_len, test_seq_len))

inputs = torch.tensor(df_scaled.iloc[:-1].values, dtype=torch.float32)
labels = torch.tensor(df_scaled.iloc[1:].values, dtype=torch.float32)
#print(inputs)
#print(labels)

# Training the network
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(),lr=0.01,momentum=0.9)
for step in range(10001):
    if step:
        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()
    
    preds = net(inputs)
    train_preds = preds[:train_seq_len]
    train_labels = labels[:train_seq_len]
    train_loss = criterion(train_preds, train_labels)
    
    test_preds = preds[-test_seq_len]
    test_labels = labels[-test_seq_len]
    test_loss = criterion(test_preds, test_labels)
    
    if step % 500 == 0:
        print ('{}times iteration: loss (training set) = {}, loss (test set) = {}'.format(
                step, train_loss, test_loss))
print('Optimizer:SGD')
preds = net(inputs)
df_pred_scaled = pd.DataFrame(preds.detach().numpy(),
        index=years[1:], columns=df.columns)
df_pred = df_pred_scaled * df.loc[2000]
df_pred.loc[2001:]                