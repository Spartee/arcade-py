from unittest.mock import AsyncMock

import pytest

from arcadepy._client import AsyncArcade
from arcadepy.resources.auth import AsyncAuthResource
from arcadepy.types.shared.authorization_response import AuthorizationResponse


@pytest.mark.asyncio
async def test_wait_for_completion_calls_status_with_correct_args():
    client = AsyncArcade(api_key="test")
    auth = AsyncAuthResource(client)
    auth.status = AsyncMock(return_value=AuthorizationResponse(status="completed"))

    auth_response_or_id = "auth_id"
    scopes = ["scope1", "scope2"]

    await auth.wait_for_completion(auth_response_or_id, scopes)

    auth.status.assert_called_with(
        authorization_id="auth_id",
        scopes="scope1 scope2",
        wait=45,
    )
