import csv
import matplotlib.pyplot as plt


def calculate(deliveries_data, matches_data):
    match_id_2016 = set()
    for lines in matches_data:
        if lines['season'] == '2016':
            match_id_2016.add(lines['id'])

    extra_run_per_team_2016 = {}
    for lines in deliveries_data:
        if lines['match_id'] in match_id_2016:
            if extra_run_per_team_2016.get(lines['bowling_team']) == None:
                extra_run_per_team_2016[lines['bowling_team']] = int(
                    lines['extra_runs'])
            else:
                extra_run_per_team_2016[lines['bowling_team']
                                        ] += int(lines['extra_runs'])
    return extra_run_per_team_2016


def transfer(extra_run_per_team_2016):
    team_names = list(extra_run_per_team_2016.keys())
    team_scores = list(extra_run_per_team_2016.values())
    return team_names, team_scores


def graph_plot(team_names, team_scores):
    plt.bar(team_names, team_scores)
    plt.xlabel("Team Name")
    plt.ylabel("Extra runs")
    plt.title("Extra runs conceded per team in the year 2016")
    plt.xticks(rotation=90)
    plt.show()


def main():
    file = open('deliveries.csv', mode='r')
    deliveries_data = csv.DictReader(file)
    file = open('matches.csv', mode='r')
    matches_data = csv.DictReader(file)

    extra_run_per_team_2016 = calculate(deliveries_data, matches_data)
    team_names, team_scores = transfer(extra_run_per_team_2016)
    graph_plot(team_names, team_scores)


if __name__ == "__main__":
    main()
