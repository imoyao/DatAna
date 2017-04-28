# -*- coding: utf-8 -*-
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib import mlab
# from matplotlib import rcParams
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
  
import settings
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
import matplotlib.font_manager as mfm
import sys
 
reload(sys)
sys.setdefaultencoding("utf-8")


n_groups = 5  
  
means_men = (20, 35, 30, 35, 27)  
means_women = (25, 32, 34, 20, 25)   
fig, ax = plt.subplots()  
index = np.arange(n_groups)  
bar_width = 0.35   
opacity = 0.4  
rects1 = plt.bar(index, means_men, bar_width,alpha=opacity, color='b',label=    'Men')  
rects2 = plt.bar(index + bar_width, means_women, bar_width,alpha=opacity,color='r',label='Women')  
plt.xlabel('Group')  
plt.ylabel('Scores')  
plt.title('Scores by group and gender')  
plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'E'))  
plt.ylim(0,40)  
plt.legend()  
  
plt.tight_layout()  
plt.show()  


