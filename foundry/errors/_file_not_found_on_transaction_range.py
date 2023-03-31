from typing import Any, Dict

from foundry.errors._palantir_rpc_exception import PalantirRPCException


class FileNotFoundOnTransactionRange(PalantirRPCException):
    """The requested file could not be found on the given transaction range, or
    the client token does not have access to it."""

    def __init__(self, error_metadata: Dict[str, Any]) -> None:
        super().__init__(error_metadata)
