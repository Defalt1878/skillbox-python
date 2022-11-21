import requests
import json

print('Задача 3. Во все тяжкие')


def get_max_deaths_episode(deaths_data, episodes_data):
    for death in deaths_data:
        episode = [
            episode for episode in episodes_data
            if int(episode['season']) == death['season'] and int(episode['episode']) == death['episode']
        ][0]
        episode['death_count'] = episode.get('death_count', 0) + death['number_of_deaths']
        episode.setdefault('deaths', []).append(death['death'])

    return max(episodes_data, key=lambda ep: ep.get('death_count', 0))


deaths_req = requests.get('https://www.breakingbadapi.com/api/deaths')
episodes_req = requests.get('https://www.breakingbadapi.com/api/episodes?series=Breaking+Bad')

max_deaths_episode = get_max_deaths_episode(json.loads(deaths_req.text), json.loads(episodes_req.text))

result_data = {
    "episode_id": max_deaths_episode['episode_id'],
    "season": int(max_deaths_episode['season']),
    "episode": int(max_deaths_episode['episode']),
    "death_count": max_deaths_episode['death_count'],
    "deaths": max_deaths_episode['deaths']
}

print(result_data)

with open('max_death_episode.json', 'w') as f:
    json.dump(result_data, f, indent=4)
