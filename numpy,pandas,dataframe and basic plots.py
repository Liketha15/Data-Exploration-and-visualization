# Part 1: NumPy Arrays
import numpy as np
# Creating arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Array operations
print(&quot;Original Array:&quot;, arr1)
print(&quot;Array + 5:&quot;, arr1 + 5)
print(&quot;Sliced Array:&quot;, arr1[1:4])
print(&quot;Reshaped 2D Array:\n&quot;, arr2.reshape(3, 2))
# Part 2: Pandas DataFrame
import pandas as pd
# Creating DataFrame
data = {
&#39;Name&#39;: [&#39;Alice&#39;, &#39;Bob&#39;, &#39;Charlie&#39;],
&#39;Age&#39;: [25, 30, 35],
&#39;Score&#39;: [85, 90, 88]
}
df = pd.DataFrame(data)
print(&quot;\nDataFrame:&quot;)
print(df)
print(&quot;\nDataFrame Info:&quot;)
print(df.info())
print(&quot;\nStatistics:&quot;)
print(df.describe())
# Part 3: Matplotlib Plots
import matplotlib.pyplot as plt
# Line Plot
plt.figure()
plt.plot(df[&#39;Name&#39;], df[&#39;Score&#39;], marker=&#39;o&#39;)
plt.title(&#39;Scores of Students&#39;)
plt.xlabel(&#39;Name&#39;)
plt.ylabel(&#39;Score&#39;)
plt.grid(True)
plt.show()
# Bar Plot
plt.figure()
plt.bar(df[&#39;Name&#39;], df[&#39;Age&#39;], color=&#39;orange&#39;)
plt.title(&#39;Age of Students&#39;)
plt.xlabel(&#39;Name&#39;)
plt.ylabel(&#39;Age&#39;)
plt.show()

# Pie Chart
plt.figure()
plt.pie(df[&#39;Score&#39;], labels=df[&#39;Name&#39;], autopct=&#39;%1.1f%%&#39;, startangle=90)
plt.title(&#39;Score Distribution&#39;)
plt.show()
