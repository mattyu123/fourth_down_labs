import nflreadpy as nfl
import polars as pl

## Define a polars data frame for all players 
all_players = nfl.load_player_stats()

## Test filter for one player 
josh_allen = all_players.filter(
  pl.col("player_display_name") == "Josh Allen"
)

## test filter for specific columns of josh allen
josh_allen_stats = josh_allen.select([
    "player_display_name",
    "position",
    "season",
    "week",
    "team",
    "opponent_team",
    "passing_yards",
    "passing_tds",
    "passing_interceptions"
])

print(josh_allen_stats)