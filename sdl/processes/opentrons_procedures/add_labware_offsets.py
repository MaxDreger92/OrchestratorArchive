# generated by datamodel-codegen:
#   filename:  add_labware_offsets.json
#   timestamp: 2024-07-17T18:45:08+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel

from sdl.processes.opentrons_utils import Location, Vector, OpentronsBaseProcedure


class AddLabwareOffsetParams(BaseModel):
    definitionUri: str
    location: Location
    vector: Vector


class AddLabwareOffset(OpentronsBaseProcedure[AddLabwareOffsetParams]):
    url = '/runs/{run_id}/commands'
    commandType = "addLabwareOffsets"


