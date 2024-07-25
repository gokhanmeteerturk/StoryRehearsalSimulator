from __future__ import annotations

from typing import List
from datetime import datetime

import pytz
from tortoise import Model, fields, Tortoise
# noinspection PyPackageRequirements
from tortoise.exceptions import NoValuesFetched
from tortoise.contrib.pydantic import pydantic_model_creator

