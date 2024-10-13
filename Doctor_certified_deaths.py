import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('bmh')

data = pd.read_csv('Doctor_certified_deaths.csv')


df_melted = data.melt(id_vars=["Cause of Death"], 
                      value_vars=["June 2024", "June 2023", "June 2022", 
                                  "Jan-Jun 2024", "Jan-Jun 2023", "Jan-Jun 2022"], 
                      var_name="Period", 
                      value_name="Number of Deaths")


plt.figure(figsize=(14, 8))
sns.barplot(x="Cause of Death", y="Number of Deaths", hue="Period", data=df_melted, palette="muted")

plt.title("Doctor Certified Deaths by Cause (June and Jan-Jun, 2022-2024)", fontsize=16)
plt.xlabel("Cause of Death", fontsize=12)
plt.ylabel("Number of Deaths", fontsize=12)

plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig('doctor_certified_deaths_by_cause_periods.png')

plt.show()
