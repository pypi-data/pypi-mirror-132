from abc import ABC
from dataclasses import dataclass, field
from typing import Iterable, Optional, TextIO

from iolanta.models import ContextAliases, LDContext, LDDocument, Quad
from rdflib import URIRef
from urlpath import URL


@dataclass(frozen=True)
class Parser(ABC):
    """
    Parser reads data from a file-like object and interprets them.

    For interpretation, it is also supplied with a context.
    """

    blank_node_prefix: str = ''

    def as_jsonld_document(self, raw_data: TextIO) -> LDDocument:
        """Generate a JSON-LD document."""
        raise NotImplementedError()

    def as_quad_stream(
        self,
        raw_data: TextIO,
        iri: Optional[URIRef],
        context: LDContext,
    ) -> Iterable[Quad]:
        raise NotImplementedError()

