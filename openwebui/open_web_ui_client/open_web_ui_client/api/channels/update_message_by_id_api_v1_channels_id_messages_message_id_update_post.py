from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.message_form import MessageForm
from ...models.message_model import MessageModel
from ...types import Response


def _get_kwargs(
    id: str,
    message_id: str,
    *,
    body: MessageForm,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/api/v1/channels/{id}/messages/{message_id}/update",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, Union["MessageModel", None]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union["MessageModel", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = MessageModel.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageModel", None], data)

        response_200 = _parse_response_200(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, Union["MessageModel", None]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    message_id: str,
    *,
    client: AuthenticatedClient,
    body: MessageForm,
) -> Response[Union[HTTPValidationError, Union["MessageModel", None]]]:
    """Update Message By Id

    Args:
        id (str):
        message_id (str):
        body (MessageForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['MessageModel', None]]]
    """

    kwargs = _get_kwargs(
        id=id,
        message_id=message_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    message_id: str,
    *,
    client: AuthenticatedClient,
    body: MessageForm,
) -> Optional[Union[HTTPValidationError, Union["MessageModel", None]]]:
    """Update Message By Id

    Args:
        id (str):
        message_id (str):
        body (MessageForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['MessageModel', None]]
    """

    return sync_detailed(
        id=id,
        message_id=message_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    message_id: str,
    *,
    client: AuthenticatedClient,
    body: MessageForm,
) -> Response[Union[HTTPValidationError, Union["MessageModel", None]]]:
    """Update Message By Id

    Args:
        id (str):
        message_id (str):
        body (MessageForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, Union['MessageModel', None]]]
    """

    kwargs = _get_kwargs(
        id=id,
        message_id=message_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    message_id: str,
    *,
    client: AuthenticatedClient,
    body: MessageForm,
) -> Optional[Union[HTTPValidationError, Union["MessageModel", None]]]:
    """Update Message By Id

    Args:
        id (str):
        message_id (str):
        body (MessageForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, Union['MessageModel', None]]
    """

    return (
        await asyncio_detailed(
            id=id,
            message_id=message_id,
            client=client,
            body=body,
        )
    ).parsed
