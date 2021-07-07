import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data], ["Math_score"], show_hist = False)
fig.show()

population_mean = statistics.mean(data)
population_stdev = statistics.stdev(data)

print(f"population_mean: {population_mean}")
print(f"population_stdev: {population_stdev}")

def random_set_of_data():
    tempList = []
    for i in range(0, 100):
        random_number = random.randint(0, len(data)-1)
        value = data[random_number]
        tempList.append(value)
    mean = statistics.mean(tempList)
    return mean
meanList = []
for i in range(0, 1000):
    random_mean = random_set_of_data()
    meanList.append(random_mean)
sampling_mean = statistics.mean(meanList)
sampling_stdev = statistics.stdev(meanList)

print(f"sampling_mean: {sampling_mean}")
print(f"sampling_stdev: {sampling_stdev}")

first_standard_deviation_start, first_standard_deviation_end = sampling_mean - sampling_stdev, sampling_mean + sampling_stdev
second_standard_deviation_start, second_standard_deviation_end = sampling_mean - (2*sampling_stdev), sampling_mean + (2*sampling_stdev) 
third_standard_deviation_start, third_standard_deviation_end = sampling_mean - (3*sampling_stdev), sampling_mean + (3*sampling_stdev)

fig2 = ff.create_distplot([meanList], ["studentMarks"], show_hist = False)
fig2.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name = "mean"))
fig2.add_trace(go.Scatter(x = [first_standard_deviation_start, first_standard_deviation_start], y = [0, 0.2], mode = "lines", name = "first_standard_deviation_start"))
fig2.add_trace(go.Scatter(x = [first_standard_deviation_end, first_standard_deviation_end], y = [0, 0.2], mode = "lines", name = "first_standard_deviation_end"))
fig2.add_trace(go.Scatter(x = [second_standard_deviation_start, second_standard_deviation_start], y = [0, 0.2], mode = "lines", name = "second_standard_deviation_start"))
fig2.add_trace(go.Scatter(x = [second_standard_deviation_end, second_standard_deviation_end], y = [0, 0.2], mode = "lines", name = "second_standard_deviation_end"))
fig2.add_trace(go.Scatter(x = [third_standard_deviation_start, third_standard_deviation_start], y = [0, 0.2], mode = "lines", name = "third_standard_deviation_start"))
fig2.add_trace(go.Scatter(x = [third_standard_deviation_end, third_standard_deviation_end], y = [0, 0.2], mode = "lines", name = "third_standard_deviation_end"))
fig2.show()

df1 = pd.read_csv("data1.csv")
data1 = df["Math_score"].tolist()

mean_data1 = statistics.mean(data1)

print(f"mean_data1: {mean_data1}")

fig3 = ff.create_distplot([meanList], ["Math_score"], show_hist = False)
fig3.add_trace(go.Scatter(x = [mean_data1, mean_data1], y = [0, 0.2], mode = "lines", name = "mean_data1"))
fig3.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name = "mean"))
fig3.add_trace(go.Scatter(x = [first_standard_deviation_end, first_standard_deviation_end], y = [0, 0.2], mode = "lines", name = "first_standard_deviation_end"))
fig3.show()

df2 = pd.read_csv("data2.csv")
data2 = df["Math_score"].tolist()

mean_data2 = statistics.mean(data2)

print(f"mean_data2: {mean_data2}")

fig3 = ff.create_distplot([meanList], ["Math_score"], show_hist = False)
fig3.add_trace(go.Scatter(x = [mean_data2, mean_data2], y = [0, 0.2], mode = "lines", name = "mean_data2"))
fig3.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name = "mean"))
fig3.add_trace(go.Scatter(x = [first_standard_deviation_end, first_standard_deviation_end], y = [0, 0.2], mode = "lines", name = "first_standard_deviation_end"))
fig3.show()

df3 = pd.read_csv("data3.csv")
data3 = df["Math_score"].tolist()

mean_data3 = statistics.mean(data3)

print(f"mean_data3: {mean_data3}")

fig3 = ff.create_distplot([meanList], ["Math_score"], show_hist = False)
fig3.add_trace(go.Scatter(x = [mean_data3, mean_data3], y = [0, 0.2], mode = "lines", name = "mean_data3"))
fig3.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 0.2], mode = "lines", name = "mean"))
fig3.add_trace(go.Scatter(x = [first_standard_deviation_end, first_standard_deviation_end], y = [0, 0.2], mode = "lines", name = "first_standard_deviation_end"))
fig3.show()


