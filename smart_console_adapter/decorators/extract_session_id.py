import inspect
from functools import wraps

from fastapi import Request


def extract_session_id(func):
    """Decorator that extracts X-chkp-sid from request headers and sets it on the adapter."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        # Get function signature to find request and adapter parameters
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        # Find request and adapter in the bound arguments
        request = None
        adapter = None

        for _, param_value in bound_args.arguments.items():
            if isinstance(param_value, Request):
                request = param_value
            elif hasattr(param_value, "set_sid"):  # Check if it's an adapter
                adapter = param_value

        # Extract session ID from headers and set it on adapter
        if request and adapter:
            session_id = request.headers.get("X-chkp-sid")
            if session_id:
                adapter.set_sid(session_id)

        return await func(*args, **kwargs)

    return wrapper
