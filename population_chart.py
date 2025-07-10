import matplotlib.pyplot as plt
countries = ['India', 'China', 'USA', 'Indonesia', 'Brazil']
population = [1410, 1440, 331, 273, 213]
plt.figure(figsize=(10, 6))
plt.bar(countries, population, color='skyblue')
plt.title('Population by Country')
plt.xlabel('Country')
plt.ylabel('Population (millions)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('population_chart.png')  
plt.show()
