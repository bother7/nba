#
#
#
import glob
import datetime
import json
import bb_tools as bb

games_url_base = 'http://data.nba.com/5s/json/cms/noseason/scoreboard/%s/games.json'
do_sportvu = False

def main():
  season_id = '00215'

  print 'Finding date of last update...'
  try:
    last_boxscore_file = sorted(glob.glob('%s/json/box_%s*.json' % (bb.DATAHOME,season_id)))[-1]
    last_boxscore = json.load(open(last_boxscore_file,'r'))
    last_update = bb.dateify(last_boxscore[0]['GAME_DATE_EST']['0'].split('T')[0])
    start_day = last_update + datetime.timedelta(days=1)
  except: # if no data exists, use first day of season
    start_day = datetime.date(2015,10,27)
  end_day = datetime.date.today() - datetime.timedelta(days=1)
  
  print 'Getting list of games since last update...'
  bb.write_gamelist_by_date('%s/csv/gamelist_update.csv' % bb.DATAHOME, season_id, start_day, end_day)

  print 'Getting stats for each game...'
  bb.write_gamelist_json('%s/csv/gamelist_update.csv' % bb.DATAHOME)

if __name__ == '__main__': 
  main()