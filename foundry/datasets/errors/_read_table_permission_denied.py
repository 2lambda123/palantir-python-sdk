from typing import Any, Dict

from foundry.errors._palantir_rpc_exception import PalantirRPCException


class ReadTablePermissionDenied(PalantirRPCException):
    """The provided token does not have permission to read the given dataset as
    a table."""

    def __init__(self, error_metadata: Dict[str, Any]) -> None:
        super().__init__(error_metadata)