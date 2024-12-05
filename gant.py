import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Predefined tasks with start, end dates, and optional colors
tasks = [
{"task": "Definuj požadavky", "start": "2025-01-01", "end": "2025-01-15", "color": "blue"},
{"task": "Najdi organizátory", "start": "2025-01-16", "end": "2025-01-31", "color": "green"},
{"task": "Vyber vhodné zaměstnance", "start": "2025-02-01", "end": "2025-02-14", "color": "orange"},
{"task": "Připrav prezentaci pro investory", "start": "2025-02-15", "end": "2025-02-28", "color": "teal"},
{"task": "Definuj pozice", "start": "2025-02-28", "end": "2025-03-10", "color": "pink"},
{"task": "Odprezentuj prezentaci", "start": "2025-03-11", "end": "2025-03-15", "color": "magenta"},
{"task": "Vyber poskytovatele", "start": "2025-03-16", "end": "2025-03-31", "color": "yellow"},
{"task": "Pořiď systém", "start": "2025-04-01", "end": "2025-04-10", "color": "red"},
{"task": "Vyber typ infrastruktury", "start": "2025-04-11", "end": "2025-04-20", "color": "cyan"},
{"task": "Nakup servery", "start": "2025-04-21", "end": "2025-04-30", "color": "brown"},
{"task": "Zaregistruj doménu", "start": "2025-05-01", "end": "2025-05-07", "color": "lime"},
{"task": "Vyber servery", "start": "2025-05-08", "end": "2025-05-15", "color": "purple"},
{"task": "Nasaď servery", "start": "2025-05-16", "end": "2025-05-30", "color": "pink"},
{"task": "Integrace s informačním systémem", "start": "2025-06-01", "end": "2025-06-15", "color": "blue"},
{"task": "Navrhni úpravy systému", "start": "2025-06-16", "end": "2025-06-30", "color": "orange"},
{"task": "Uprav systém", "start": "2025-07-01", "end": "2025-07-10", "color": "teal"},
{"task": "Založ prostředí", "start": "2025-07-11", "end": "2025-07-20", "color": "magenta"},
{"task": "Vyber finální podobu systému", "start": "2025-07-21", "end": "2025-07-31"},
{"task": "Založení účtů na sociálních sítích", "start": "2025-08-01", "end": "2025-08-10", "color": "cyan"},
{"task": "Vytváření obsahu", "start": "2025-08-11", "end": "2025-08-31", "color": "green"},
{"task": "Publikuj na sociální sítě", "start": "2025-09-01", "end": "2025-09-15", "color": "red"},
{"task": "Publikace reklam", "start": "2025-09-16", "end": "2025-10-01", "color": "lime"},
{"task": "Sepiš smlouvy", "start": "2025-10-02", "end": "2025-10-10", "color": "yellow"},
{"task": "Podepiš smlouvy", "start": "2025-10-11", "end": "2025-10-20", "color": "blue"},
{"task": "Návrh smlouvy", "start": "2025-10-21", "end": "2025-10-31", "color": "pink"},
{"task": "Připrav a finalizuj smlouvu", "start": "2025-11-01", "end": "2025-11-10", "color": "brown"},
{"task": "Najdi vhodný prostor", "start": "2025-11-11", "end": "2025-11-20", "color": "purple"},
{"task": "Vybavit kancelář", "start": "2025-11-21", "end": "2025-11-30", "color": "orange"},
{"task": "Zaškolení uživatelů", "start": "2025-12-01", "end": "2025-12-15", "color": "teal"},
{"task": "Vytvoř komunikační kanály", "start": "2025-12-16", "end": "2025-12-31", "color": "magenta"},
{"task": "Vytvoř webové stránky", "start": "2026-01-01", "end": "2026-01-31", "color": "cyan"},
{"task": "Vytvoření reklam", "start": "2026-02-01", "end": "2026-02-15", "color": "pink"},
{"task": "Namigruj data", "start": "2026-02-16", "end": "2026-02-28", "color": "red"},
{"task": "Podepsání smlouvy (investoři)", "start": "2026-03-01", "end": "2026-03-15", "color": "lime"}
]

# Function to dynamically add tasks with optional custom colors
def add_task(task_name, start_date, end_date, color=None):
    tasks.append({"task": task_name, "start": start_date, "end": end_date, "color": color})

# Example of adding a task with a custom color
# add_task("Spuštění projektu", "2025-06-28", "2025-06-28", "blue")

# Convert dates and create a Gantt chart
fig, ax = plt.subplots(figsize=(10, 8))
yticks = []
ylabels = []

for i, task in enumerate(tasks):
    start = datetime.strptime(task["start"], "%Y-%m-%d")
    end = datetime.strptime(task["end"], "%Y-%m-%d")
    color = task.get("color", plt.cm.tab20.colors[i % 20])  # Default color if none provided
    ax.barh(i, (end - start).days, left=mdates.date2num(start), color=color)
    yticks.append(i)
    ylabels.append(task["task"])

# Format the chart
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))
ax.xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.xlabel("Datum")
plt.ylabel("Úkoly")
plt.title("Plán projektu - Ganttův diagram")
plt.tight_layout()

# Show the chart
plt.show()
