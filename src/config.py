from dataclasses import dataclass


@dataclass
class Config:
    OD_SECRET = 'letmepass'
    OD_ENDPOINT_PREFIX = f"https://app.optimaldynamics.io/eng-interviews/q0/{OD_SECRET}"

config = Config()
