from pydantic import BaseSettings
import os

class appconfigs(BaseSettings):
	env: str = os.environ['ENV']

