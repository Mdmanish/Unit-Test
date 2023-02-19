import csv
import matplotlib.pyplot as plt


def calculate(deliveries_data, matches_data):
    match_id_2015 = set()
    for lines in matches_data:
        if lines['season'] == '2015':
            match_id_2015.add(lines['id'])

    bowler_run, bowler_over = {}, {}
    prev = "prev bowler"
    for lines in deliveries_data:
        if lines['match_id'] in match_id_2015 and lines['is_super_over'] == '0':
            if bowler_run.get(lines['bowler']) == None:
                bowler_run[lines['bowler']] = int(lines['total_runs'])
                bowler_over[lines['bowler']] = 0
            else:
                bowler_run[lines['bowler']] += int(lines['total_runs'])
            if lines['bowler'] != prev:
                bowler_over[lines['bowler']] += 1
                prev = lines['bowler']

    top_10_eco_bowler_2015 = {}
    for bowler in bowler_run:
        top_10_eco_bowler_2015[bowler] = bowler_run[bowler] / \
            bowler_over[bowler]

    sorted_top_10_eco_bowler_2015 = sorted(
        top_10_eco_bowler_2015.items(), key=lambda x: x[1])
    bowler_name, runs = [], []
    for i in range(0, len(sorted_top_10_eco_bowler_2015)):
        bowler_name.append(sorted_top_10_eco_bowler_2015[i][0])
        runs.append(sorted_top_10_eco_bowler_2015[i][1])
        if i == 10:
            break
    return bowler_name, runs


def graph_plot(bowler_name, runs):
    plt.bar(bowler_name, runs)
    plt.xlabel("Bowler Name")
    plt.ylabel("Average runs")
    plt.title("Top 10 economical bowlers in the year 2015")
    #plt.xticks(rotation = 90)
    plt.show()


def main():
    file = open('deliveries.csv', mode='r')
    deliveries_data = csv.DictReader(file)
    file = open('matches.csv', mode='r')
    matches_data = csv.DictReader(file)

    bowler_name, runs = calculate(deliveries_data, matches_data)
    graph_plot(bowler_name, runs)


if __name__ == "__main__":
    main()
