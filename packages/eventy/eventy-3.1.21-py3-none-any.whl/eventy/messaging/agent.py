# Copyright (c) Qotto, 2021

from __future__ import annotations

from enum import Enum
from functools import wraps
from typing import Callable, Iterable, Optional

from eventy.record import Record, RecordType

__all__ = [
    'Guarantee',
    'Handler',
    'Agent',
    'handler',
    'handle_event',
    'handle_response',
    'handle_request',
]


class Guarantee(Enum):
    """
    Delivery guarantee for handlers
    """
    AT_LEAST_ONCE = 'AT_LEAST_ONCE'
    # alias
    ALO = 'AT_LEAST_ONCE'

    AT_MOST_ONCE = 'AT_MOST_ONCE'
    # alias
    AMO = 'AT_MOST_ONCE'

    EXACTLY_ONCE = 'EXACTLY_ONCE'
    # alias
    EOS = 'EXACTLY_ONCE'


class Handler:
    """
    Record handler
    """

    def __init__(
        self,
        service_name: Optional[str],
        record_type: RecordType,
        record_name: str,
        delivery_guarantee: Guarantee,
    ):
        self._service_name = service_name
        self._delivery_guarantee = delivery_guarantee
        self._record_type = record_type
        self._record_name = record_name

    @property
    def service_name(self) -> Optional[str]:
        return self._service_name

    @property
    def record_type(self) -> RecordType:
        return self._record_type

    @property
    def record_name(self) -> str:
        return self._record_name

    @property
    def delivery_guarantee(self) -> Guarantee:
        return self._delivery_guarantee

    def handle_record(self, record: Record) -> Iterable[Record]:
        raise NotImplementedError

    def __str__(self) -> str:
        record_info = f"{self._record_name} ({self._record_type})"
        if self._service_name is None:
            service_info = "current app service"
        else:
            service_info = self._service_name
        return f'<{self.__class__.__name__} for {record_info} from {service_info}>'


class Agent:
    """
    An agent can define methods to handle records
    """

    @property
    def handlers(self) -> Iterable[Handler]:
        for attribute_name in self.__dir__():
            attribute = getattr(self, attribute_name)
            if isinstance(attribute, _AgentHandler):
                agent_handler = attribute
                agent_handler.set_agent(self)
                yield agent_handler


class _FunctionHandler(Handler):
    """
    Record handler
    """

    def __init__(
        self,
        service_name: Optional[str],
        record_type: RecordType,
        record_name: str,
        delivery_guarantee: Guarantee,
        handle_function: Callable[[Record], Iterable[Record]],
    ) -> None:
        super().__init__(
            service_name=service_name,
            record_type=record_type,
            record_name=record_name,
            delivery_guarantee=delivery_guarantee,
        )
        self._handle_function = handle_function

    def handle_record(self, record: Record) -> Iterable[Record]:
        yielded_records = self._handle_function(record)
        if yielded_records:
            yield from yielded_records
        else:
            return []

    def __call__(self, record: Record) -> Iterable[Record]:
        """
        Override __call__ so the method can be called directly as if it was not decorated.
        """
        yield from self._handle_function(record)


class _AgentHandler(Handler):
    """
    Record handler for an Agent method
    """

    def __init__(
        self,
        service_name: Optional[str],
        record_type: RecordType,
        record_name: str,
        delivery_guarantee: Guarantee,
        handle_method: Callable[[Agent, Record], Iterable[Record]],
    ) -> None:
        super().__init__(
            service_name=service_name,
            record_type=record_type,
            record_name=record_name,
            delivery_guarantee=delivery_guarantee,
        )
        self._handle_method = handle_method
        self._handle_function: Optional[Callable[[Record], Iterable[Record]]] = None

    def set_agent(self, agent: Agent) -> None:
        method = self._handle_method

        @wraps(method)
        def function(record: Record) -> Iterable[Record]:
            yield from self._handle_method(agent, record)

        self._handle_function = function

    def handle_record(self, record: Record) -> Iterable[Record]:
        if self._handle_function is None:
            raise AttributeError(f"Agent need to be set before usage.")
        else:
            yielded_records = self._handle_function(record)
            if yielded_records:
                yield from yielded_records
            else:
                return []

    def __call__(self, agent_self: Agent, record: Record) -> Iterable[Record]:
        """
        Override __call__ so the method can also be called directly as if it was not decorated.
        """
        yielded_records = self._handle_method(agent_self, record)
        if yielded_records:
            yield from yielded_records
        else:
            return []


def handler(type: RecordType, service: Optional[str], name: str, guarantee: Guarantee):
    """
    Decorator to create handlers from functions or agent methods
    """

    def decorator(function_or_method):
        # Agent method
        if '.' in function_or_method.__qualname__:
            method = function_or_method
            return _AgentHandler(
                service_name=service,
                record_type=type,
                record_name=name,
                delivery_guarantee=guarantee,
                handle_method=method,
            )
        # Simple function
        else:
            function = function_or_method
            return _FunctionHandler(
                service_name=service,
                record_type=type,
                record_name=name,
                delivery_guarantee=guarantee,
                handle_function=function,
            )

    return decorator


def handle_event(service: str, name: str, guarantee: Guarantee = Guarantee.EXACTLY_ONCE):
    return handler(RecordType.EVENT, service, name, guarantee)


def handle_request(name: str, guarantee: Guarantee = Guarantee.EXACTLY_ONCE):
    return handler(RecordType.REQUEST, None, name, guarantee)


def handle_response(service: str, name: str, guarantee: Guarantee = Guarantee.EXACTLY_ONCE):
    return handler(RecordType.RESPONSE, service, name, guarantee)
