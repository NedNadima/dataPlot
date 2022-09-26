import matplotlib.pyplot as plt

labels = "Python", "C++", "Ruby", "Java", "PHP", "Perl"
sizes = [33, 52, 12, 17, 62, 48]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.show()