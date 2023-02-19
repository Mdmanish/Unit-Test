import csv
import matplotlib.pyplot as plt


def calculate(csv_data):
    match_played_every_year = {}
    for lines in csv_data:
        if match_played_every_year.get(lines['season']) == None:
            match_played_every_year[lines['season']] = 1
        else:
            match_played_every_year[lines['season']] += 1
    return match_played_every_year


def transfer(total_run_scored_by_each_team):
    year_names = list(total_run_scored_by_each_team.keys())
    match_played = list(total_run_scored_by_each_team.values())
    return year_names, match_played


def graph_plot(year_names, match_played):
    plt.bar(year_names, match_played)
    plt.xlabel("Years")
    plt.ylabel("Matches played")
    plt.title("5. Number of matches played per year for all the years in IPL.")
    plt.xticks(rotation=90)
    plt.show()


def main():
    file = open('matches.csv', mode='r')
    csv_data = csv.DictReader(file)

    match_played_every_year = calculate(csv_data)
    team_names, team_scores = transfer(match_played_every_year)
    graph_plot(team_names, team_scores)


if __name__ == "__main__":
    main()
