#!/usr/bin/env python3

import os
import sys
import json
import pprint

import jinja2

OUTDIR = 'dcss-scoreboard-html'

if __name__ == '__main__':
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('html_templates'))

    data = json.loads(open('scoring_data.json').read())

    print("Writing HTML to %s" % OUTDIR)
    os.makedirs(OUTDIR)

    with open(os.path.join(OUTDIR, 'index.html'), 'w') as f:
        template = env.get_template('index.html')
        f.write(template.render())

    with open(os.path.join(OUTDIR, 'highscores.html'), 'w') as f:
        template = env.get_template('highscores.html')
        f.write(template.render(highscores=data['global_stats']))

    player_html_path = os.path.join(OUTDIR, 'players')
    os.makedirs(player_html_path)
    with open(os.path.join(OUTDIR, 'players.html'), 'w') as f:
        template = env.get_template('players.html')
        f.write(template.render(players=data['players'].keys()))

    for player, stats in data['players'].items():
        outfile = os.path.join(player_html_path, player + '.html')
        with open(outfile, 'w') as f:
            template = env.get_template('player.html')
            f.write(template.render(player=player, stats=stats))
