# coding=utf-8
# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2017
from typing import Any
from typing import Callable
from typing import Iterable
from typing import Set
from typing import Union

from enum import Enum

from streamsx.topology.schema import StreamSchema
from streamsx.topology.schema import CommonSchema
#from streamsx.topology.topology import Routing
#from streamsx.topology.topology import Stream
#from streamsx.topology.topology import View

class Routing(Enum): ...

class Topology(object):
    def __init__(self, name: str=None, namespace: str=None, files: Any=None) -> None: ...
    def source(self, func : Union[Callable[[], Any],Iterable[Any]], name: str =None) -> Stream: ...
    def name(self) -> str: ...
    def namespace(self) -> str: ...
    def subscribe(self, topic: str, schema: Union[StreamSchema,CommonSchema], name: str=None) -> Stream: ...
    def add_file_dependency(self, path: str, location: str) -> str: ...


class Stream(object):
    def name(self) -> str: ...
    def for_each(self, func: Any, name: str=None) -> Any: ...
    def sink(self, func: Callable[[Any], None], name: str=None) -> Any: ...
    def filter(self, func: Callable[[Any], bool], name: str=None) -> 'Stream': ...
    def view(self, buffer_time: float=10.0, sample_size: int=10000, name: str=None, description: str=None, start: bool=True) -> View: ...
    def map(self, func: Callable[[Any], Any], name: Any=None, schema: Any=None) -> 'Stream': ...
    def transform(self, func: Callable[[Any], Any], name: str=None) -> 'Stream': ...
    def flat_map(self, func: Any, name: str=None) -> 'Stream': ...
    def multi_transform(self, func: Any, name: str=None) -> 'Stream': ...
    def isolate(self) -> 'Stream': ...
    def low_latency(self) -> 'Stream': ...
    def end_low_latency(self) -> 'Stream': ...
    def parallel(self, width: Any, routing: Routing, func: Any=None, name: str=None) -> Any: ...
    def end_parallel(self) -> 'Stream': ...
    def last(self, size: int) -> Window: ...
    def union(self, streamSet: Set[Any]) -> 'Stream': ...
    def print(self, tag: Any=None, name: str=None) -> Any: ...
    def publish(self, topic: Any, schema: Any=None, name: str=None) -> Any: ...
    def autonomous(self) -> Any: ...
    def as_string(self, name: str=None) -> 'Stream': ...
    def as_json(self, force_object: Any=bool, name: str=None) -> Any: ...
    def resource_tags(self) -> Any: ...


class View(object):
    def initialize_rest(self) -> None: ...
    def stop_data_fetch(self) -> None: ...
    def start_data_fetch(self) -> Any: ...

class PendingStream(object):
    def __init__(self, topology: Topology) -> None: ...
    def complete(self, stream: Stream) -> None: ...
    def is_complete(self) -> bool: ...

class Window(object):
    def trigger(self, when: Any=1) -> Any: ...
    def aggregate(self, function: Any, name: Any=None, schema: Any=None) -> Any: ...


