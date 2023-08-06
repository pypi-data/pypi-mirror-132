from dominate.tags import a
from more_itertools import first

from iolanta.facet import Facet
from octadocs.iolanta import render, HTML


class ProvEntity(Facet):
    """Render a node with prov:value defined."""

    def render(self):
        """Render value and link to it."""
        rows = self.octiron.query(
            '''
            SELECT * WHERE {
                ?node
                    prov:value ?value ;
                    prov:wasDerivedFrom ?source .

                OPTIONAL {
                    ?node rdfs:comment ?comment .
                }
            }
            ''',
            node=self.iri,
        )

        try:
            row = first(rows)
        except ValueError:
            return '<prov:value> and <prov:wasDerivedFrom> were not found.'

        kwargs = {}
        if title := row.get('title'):
            kwargs.update(title=title)

        return a(
            render(
                node=row['value'],
                octiron=self.octiron,
            ),
            href=row['source'],
            target='_blank',
            **kwargs,
        )
