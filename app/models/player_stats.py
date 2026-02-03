from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PlayerStats(Base):
    __tablename__ = "player_stats"

    id = Column(Integer, primary_key=True, index=True)
    league = Column(String(100))
    season = Column(Integer)
    team = Column(String(100))
    player = Column(String(100))
    league_id = Column(Integer)
    season_id = Column(Integer)
    team_id = Column(Integer)
    player_id = Column(Integer)
    position = Column(String(10))
    matches = Column(Integer)
    minutes = Column(Integer)
    goals = Column(Integer)
    xg = Column(Numeric(10, 6))
    np_goals = Column(Integer)
    np_xg = Column(Numeric(10, 6))
    assists = Column(Integer)
    xa = Column(Numeric(10, 6))
    shots = Column(Integer)
    key_passes = Column(Integer)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    xg_chain = Column(Numeric(10, 6))
    xg_buildup = Column(Numeric(10, 6))