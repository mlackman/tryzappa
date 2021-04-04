from __future__ import annotations
from typing import Sequence
import dataclasses


@dataclasses.dataclass
class Response:
    principalId: str
    policyDocument: PolicyDocument


@dataclasses.dataclass
class PolicyDocument:
    Statement: Sequence[Statement]
    Version: str = '2012-10-17'


@dataclasses.dataclass
class Statement:
    Action: str
    Effect: str
    Resource: str


def lambda_handler(event, context):
    principalId = 'user'  # lookup this from somewhere
    response = Response(
        principalId,
        PolicyDocument(
            [Statement('execute-api:Invoke', 'Allow', event['methodArn'])]
        )
    )
    return dataclasses.asdict(response)
