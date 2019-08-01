#import packages
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#load the file
className = input("type the name of the class")
file = input("type the filename of the {} scores: ".format(className))
scores = pd.read_csv(file)


#display data
print()
print("here is he raw data")
print(scores)


#in this section we will look at the calculus ab scores by year
#create subplot
figure1 = plt.subplot()

#create individual bar plot for every AP Calculus AB score
colors = ["red", "orange", "green", "blue", "purple"]
for i in [1, 2, 3, 4, 5]:
    figure1.bar(np.array(scores["Year"] - .45 + .15 * i), scores["Number of {}s".format(i)], .15, label=str(i), color=colors[i - 1])

#create labels
figure1.set_title("{} Scores by Year".format(className))
figure1.set_ylabel("Frequency")
figure1.set_xlabel("Year")
figure1.set_xticks(scores["Year"])
figure1.legend()

#show subplot
plt.show()


#now we will plot the average score per year and the percent 3 or higher per year, side by side
#create plot
plt.figure()

#create the percent 3 or higher subplot
plt.subplot(211)
plt.subplot(211).set_title("{} Statistics by Year".format(className))
plt.plot(scores["Year"], scores["Percent 3 or Higher"], color="green", marker='o')
plt.subplot(211).set_ylabel("Percent 3 or Higher")
plt.subplot(211).set_yticks([10 * i for i in range(11)])
plt.subplot(211).set_xlabel("Year")
plt.subplot(211).set_xticks(scores["Year"])

#create the average score subplot
plt.subplot(212)
plt.plot(scores["Year"], scores["Average Score"], marker='o')
plt.subplot(212).set_ylabel("Average Score")
plt.subplot(212).set_yticks([1, 2, 3, 4, 5])
plt.subplot(212).set_xlabel("Year")
plt.subplot(212).set_xticks(scores["Year"])

#show plot
plt.show()
