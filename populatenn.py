import nnData as nn
from datetime import datetime

for i in range(112, (datetime.today() - datetime(2019, 12, 31)).days + 1):
    nn.pred_to_file2(i, extra_days=50, minimum=100)