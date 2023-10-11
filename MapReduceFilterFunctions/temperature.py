# Hourly temperature data for a week in Kelvin
temp_list = [
    [
        281.72,
        281.72,
        281.71,
        281.70,
        281.69,
        281.69,
        281.68,
        281.67,
        281.66,
        281.66,
        281.65,
        281.64,
        281.63,
        281.63,
        281.62,
        282.71,
        285.05,
        287.97,
        290.61,
        292.06,
        293.68,
        295.32,
        295.18,
        296.11,
    ],
    [
        295.24,
        294.38,
        292.28,
        291.12,
        289.93,
        287.87,
        287.14,
        286.54,
        286.16,
        285.31,
        284.30,
        283.96,
        283.60,
        283.23,
        283.50,
        284.57,
        285.64,
        286.71,
        287.42,
        288.61,
        289.13,
        289.41,
        289.18,
        288.95,
    ],
    [
        288.79,
        287.47,
        286.01,
        284.85,
        283.91,
        283.31,
        283.07,
        283.15,
        282.51,
        281.98,
        281.49,
        281.14,
        280.59,
        279.65,
        279.15,
        279.72,
        282.40,
        284.72,
        286.03,
        287.19,
        288.68,
        289.56,
        290.05,
        289.98,
    ],
    [
        289.60,
        288.40,
        286.38,
        285.56,
        284.45,
        283.92,
        283.25,
        282.59,
        281.92,
        281.78,
        281.63,
        281.08,
        280.64,
        281.14,
        280.08,
        280.70,
        282.98,
        284.62,
        286.61,
        287.45,
        289.22,
        290.21,
        289.94,
        290.01,
    ],
    [
        289.85,
        288.82,
        287.60,
        285.82,
        284.58,
        284.12,
        283.63,
        282.98,
        282.68,
        282.38,
        281.77,
        281.47,
        281.06,
        280.55,
        280.65,
        281.00,
        283.49,
        286.17,
        287.58,
        289.49,
        292.11,
        292.85,
        292.69,
        292.85,
    ],
    [
        292.05,
        290.34,
        288.05,
        286.46,
        285.37,
        285.04,
        284.38,
        283.73,
        283.07,
        282.87,
        280.77,
        280.32,
        280.01,
        279.77,
        279.54,
        279.63,
        282.48,
        287.17,
        289.47,
        291.63,
        293.42,
        293.95,
        294.78,
        294.10,
    ],
    [
        293.62,
        291.88,
        290.03,
        288.43,
        287.15,
        286.78,
        286.32,
        285.17,
        283.78,
        282.96,
        282.93,
        281.96,
        282.02,
        281.26,
        280.25,
        281.01,
        283.15,
        286.49,
        289.87,
        291.42,
        292.46,
        293.35,
        294.32,
        294.85,
    ],
]
# Lambda + Map
print(temp_list[0])  # temp_list_Monday
Celcius = list(map(lambda temp: round(temp - 273.15, 2), temp_list[0]))
print(Celcius)
Fahrenhite = list(map(lambda far: round(((far * 1.8) + 32), 2), Celcius))
print(Fahrenhite)

# List comprehension
temp_list_Monday_C = [round(temp_K - 273.15, 2) for temp_K in temp_list[0]]
print(temp_list_Monday_C)

# For loop
temp_list_Monday_C = []
for temp_K in temp_list[0]:
    temp_list_Monday_C.append(round(temp_K - 273.15, 2))
print(temp_list_Monday_C)

# average temperature for each day of the week

# For loop : Way1
temp_list_week = []
weeklyavg = []
s = 0
print(len(temp_list))
for i in range(len(temp_list)):
    for temp_K in temp_list[i]:
        s = s + temp_K
    weeklyavg.append(round((s / 24), 2))
    s = 0
print(weeklyavg)

# For loop : Way2
avgtempbyday = []
for temp_c_by_day in temp_list:
    avgtempbyday.append(round(sum(temp_c_by_day) / len(temp_c_by_day), 2))
print(avgtempbyday)

# List comprehension
avgtempbyday1 = []
avgtempbyday1 = [
    round(sum(temp_c_by_day) / len(temp_c_by_day), 2) for temp_c_by_day in temp_list
]
print(avgtempbyday1)


# Lambda + Reduce
from functools import reduce

avgtempbyday2 = []
avgtempbyday2 = [
    round(reduce(lambda x, y: x + y, temp_c_by_day) / len(temp_c_by_day), 2)
    for temp_c_by_day in temp_list
]
print(avgtempbyday2)
