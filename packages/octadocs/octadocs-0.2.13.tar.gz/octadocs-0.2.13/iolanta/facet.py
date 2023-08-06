from dataclasses import dataclass
from functools import cached_property
from typing import Optional

from octadocs.octiron import Octiron
from rdflib.term import Node, URIRef


@dataclass
class Facet:
    """Base facet class."""

    iri: Node
    octiron: Octiron
    environment: Optional[URIRef] = None

    @cached_property
    def uriref(self) -> URIRef:
        """Format as URIRef."""
        return URIRef(self.iri)

    def query(self, query_text: str, **kwargs):
        """SPARQL query."""
        return self.octiron.query(
            query_text=query_text,
            **kwargs
        )

    def render(self):
        """Render the facet."""
        raise NotImplementedError()

    def __str__(self):
        """Render."""
        return str(self.render())
