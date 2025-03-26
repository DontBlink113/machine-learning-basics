import pandas as pd
import matplotlib.pyplot as plt 

# read data, seperate independent and dependent variables
df = pd.read_csv("linear_regression_data.csv")
xValues = df["studytime"]
yValues = df['score']

#Set initial parameters 

initial_m = -5.0 #initial slope of line
initial_b = 100.0 #initial y-intercept of line
m = initial_m
b = initial_b
L = 0.01 #training rate 
iterations = 1000


#update m and b based on error function
for i in range(iterations):
    
    #Calculate direction of greatest ascent for m
    sumOfError = 0.0
    for j in range(len(xValues)):
        sumOfError += xValues[j] * (yValues[j] - (m * xValues[j] + b))
        
        if(i % 100 == 0):
            print(xValues[j])
            print(yValues[j])
            print(m)
            print(b)
    m_greatestAscent = -2 * (sumOfError / len(xValues))


    #Calculate direction of greatest ascent for b
    sumOfError = 0
    for j in range(len(xValues)):
        sumOfError += (yValues[j] - (m * xValues[j] + b))
    b_greatestAscent = -2 * (sumOfError / len(xValues))

    m = m - L * m_greatestAscent
    b = b - L * b_greatestAscent
    
print(m, b)

#Display previous line of best fit
oldYValues = []
for i in range(len(xValues)):
    oldYValues.append(initial_m * xValues[i] + initial_b)

plt.scatter(df.studytime, df.score)
plt.plot(xValues, oldYValues, label=f"line of best fit", color='red')
plt.show()

#Display new line of best fit
newYValues = []
for i in range(len(xValues)):
    newYValues.append(m * xValues[i] + b)

plt.scatter(df.studytime, df.score)
plt.plot(xValues, newYValues, label=f"line of best fit", color='red')
plt.show()


