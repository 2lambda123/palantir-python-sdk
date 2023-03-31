from typing import Any, Dict

from foundry.errors._palantir_rpc_exception import PalantirRPCException


class AbortTransactionPermissionDenied(PalantirRPCException):
    """The provided token does not have permission to abort the given
    treansaction on the given dataset."""

    def __init__(self, error_metadata: Dict[str, Any]) -> None:
        super().__init__(error_metadata)