import csv
import matplotlib.pyplot as plt


def calculate(csv_data):
    matches_won_per_team_per_year = {}
    for lines in csv_data:
        if matches_won_per_team_per_year.get(lines['winner']) == None:
            matches_won_per_team_per_year[lines['winner']] = {
                2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0, 2015: 0, 2016: 0, 2017: 0}
            matches_won_per_team_per_year[lines['winner']][int(
                lines['season'])] = 1
        else:
            matches_won_per_team_per_year[lines['winner']][int(
                lines['season'])] += 1

    return matches_won_per_team_per_year


def graph_plot(matches_won_per_team_per_year):
    team_names = list(matches_won_per_team_per_year.keys())
    years = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    clr = ["blue", "grey", "yellow", "green", "navy",
           "olive", "red", "pink", "purple", "black"]
    buttom_height = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 10):
        curr_year_won_count = []
        if i == 0:
            for team in matches_won_per_team_per_year:
                curr_year_won_count.append(
                    matches_won_per_team_per_year[team][years[i]])
            plt.bar(team_names, curr_year_won_count,
                    color=clr[i], label=years[i])
        else:
            for team in matches_won_per_team_per_year:
                curr_year_won_count.append(
                    matches_won_per_team_per_year[team][years[i]])
            plt.bar(team_names, curr_year_won_count, bottom=list(
                buttom_height), color=clr[i], label=years[i])

        # calculates buttom parameter (buttom_height).
        for j in range(0, 15):
            buttom_height[j] += int(curr_year_won_count[j])

    plt.xlabel("Teams")
    plt.ylabel("Match won every season.")
    plt.title("6. Stacked chart of matches won by team by season")
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()


def main():
    file = open('matches.csv', mode='r')
    csv_data = csv.DictReader(file)
    matches_won_per_team_per_year = calculate(csv_data)
    graph_plot(matches_won_per_team_per_year)


if __name__ == "__main__":
    main()
