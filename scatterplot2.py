# %matplotlib inline   
# -- This line is required if you are running from notebook
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
# import numpy as np
filename = "resulting_data.csv"
dict_lines = {}
line_no = 0
x_retweets = []
y_netscore = []
with open(filename, 'r') as fref:
	for line in fref:
		#print(line.strip())
		line = line.strip()
		line_list = line.split(",")
		dict_lines[line_no] = line_list
		if line_no > 0:
			x_retweets.append(int(line_list[0]))
			y_netscore.append(int(line_list[4]))
		line_no += 1

#print(dict_lines)	
print('Used as x axis :', y_netscore)
print('Used as y axis :',x_retweets)	

#x = np.linspace(0, 10, 30)
#y = np.sin(x)

#colors = (0,0,0)
colors = None
area = 80

# Plot
plt.scatter(y_netscore, x_retweets, s=area, c=colors, alpha=0.5)
plt.title('Sentiment Analysis of Tweets', fontsize=20)
plt.xlabel('Net Sentiment Score', fontsize=15)
plt.ylabel('Number of Retweets', fontsize=15)
plt.show()
