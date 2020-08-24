"""Base RPC Provider."""
from typing import Any

from solanarpc.rpc_types import RPCResponse, RPCMethod


class BaseProvider:
    """Base class for RPC providers to implement."""

    def make_request(self, method: RPCMethod, *params: Any) -> RPCResponse:
        """Make a request ot the rpc endpoint."""
        raise NotImplementedError("Providers must implement this method")

    def is_connected(self) -> bool:
        """Health check."""
        raise NotImplementedError("Providers must implement this method")