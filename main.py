import matplotlib.pyplot as plt
import pandas as pd

data = [{
    'name': 'Nick',
    'jan_ir': 124,
    'feb_ir': 129,
    'mar_ir': 165,
    },
    {
        ''


}]

raw_data ={'names':['Ned', 'Ashley', 'Jon'],
           'jan_ir':[123,147, 150],
            'feb_ir':[122,144, 139],
            'mar_ir':[121,141, 130]
           }

df = pd.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'march_ir'])
print(df)