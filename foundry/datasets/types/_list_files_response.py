from typing import TYPE_CHECKING, Any, Iterable, Optional

from foundry.core.api import PalantirSession

if TYPE_CHECKING:
    from typing import Mapping

    from foundry.datasets.types._file import File


class ListFilesResponse:
    """A page of Files and an optional page token that can be used to retrieve
    the next page."""

    def __init__(
        self, data: Iterable["File"], next_page_token: Optional[str] = None, session: Optional[PalantirSession] = None
    ) -> None:
        self._session = session
        self._next_page_token = next_page_token
        self._data = data

    @property
    def next_page_token(self) -> Optional[str]:
        return self._next_page_token

    @property
    def data(self) -> Iterable["File"]:
        return self._data

    def __eq__(self, other: Any) -> bool:
        return self is other or (
            type(self) == type(other)
            and self._next_page_token == other._next_page_token
            and (self._data == other._data)
        )

    def __repr__(self) -> str:
        return f"ListFilesResponse(next_page_token={self.next_page_token}, data={self.data})"

    def _asdict(self) -> "Mapping[str, Any]":
        return {
            "nextPageToken": self._next_page_token if self._next_page_token else None,
            "data": [field._asdict() for field in self._data],
        }