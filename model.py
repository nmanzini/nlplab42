import torch.nn as nn
import torch.nn.functional as F
from torch.nn import Parameter
import torch

class BowModel(nn.Module):
    def __init__(self, emb_tensor):
        super(BowModel, self).__init__()
        n_embedding, dim = emb_tensor.size()
        self.embedding = nn.Embedding(n_embedding, dim, padding_idx=0)
        self.embedding.weight = Parameter(emb_tensor, requires_grad=False)
        self.out = nn.Linear(dim, 2)

    def forward(self, input):
        '''
        input is a [batch_size, sentence_length] tensor with a list of token IDs
        '''

        embedded = self.embedding(input)
        # Here we take into account only the first word of the sentence
        # You should change it, e.g. by taking the average of the words of the sentence

        bow = torch.mean(embedded, 1, keepdim=False)
        # bow = embedded[:, 0]
        return F.log_softmax(self.out(bow))

def unique(tensor1d):
    t, idx = np.unique(tensor1d.numpy(), return_inverse=True)
    return torch.from_numpy(t), torch.from_numpy(idx)  
