"""The marketing page the golden fixtures were frozen from.

The same tags, the same attributes, the same order as WingedSwift's
``GoldenFileTests``. Kept out of the test module so both the golden test and the
performance guard can build it.
"""

from __future__ import annotations

from winged import (
    H1,
    A,
    Body,
    Button,
    Caption,
    Code,
    Details,
    Document,
    Fieldset,
    Figcaption,
    Figure,
    Footer,
    Form,
    Head,
    Header,
    Img,
    Input,
    Label,
    Legend,
    Li,
    Link,
    Main,
    Nav,
    P,
    Pre,
    Section,
    Summary,
    Table,
    Tbody,
    Td,
    Th,
    Thead,
    Title,
    Tr,
    Ul,
)
from winged.seo import SeoBuilder


def marketing_page() -> Document:
    seo = SeoBuilder(
        title="RideKeeper",
        description="Motorcycle maintenance companion",
        image="https://ridekeeper.example/og.jpg",
        url="https://ridekeeper.example",
        keywords=["swift", "motorcycle"],
        author="Michel Lutz",
        twitter_site="@micheltlutz",
    )
    head = Head(
        seo.build(),
        Title("RideKeeper — track every service"),
        Link(href="/css/style.css", rel="stylesheet"),
    )
    body = Body(
        Header(
            Nav(
                A("RideKeeper", href="/", cls="logo"),
                Ul(
                    Li(A("Home", href="/")),
                    Li(A("Pricing & plans", href="/pricing")),
                ),
            )
        ),
        Main(
            Section(
                H1("Track every service"),
                P("Fuel, tyres & chain — all in one place."),
                A("Download", href="https://apps.example/app", cls="button"),
                id_="hero",
            ),
            Table(
                Caption("Plans"),
                Thead(Tr(Th("Plan"), Th("Price"))),
                Tbody(
                    Tr(Td("Free"), Td("R$ 0")),
                    Tr(Td("Pro"), Td("R$ 9,90/mês")),
                ),
            ),
            Details(
                Summary("Is my data private?"),
                P("Yes — everything syncs through your own iCloud account."),
                open=True,
            ),
            Form(
                Fieldset(
                    Legend("Newsletter"),
                    Label("E-mail", for_="email"),
                    Input(type_="email", name="email", required=True),
                    Button("Subscribe", type_="submit"),
                ),
                action="/subscribe",
            ),
            Pre(Code("let page = html { }")),
            Figure(
                Img("/img/app.png", "App screenshot"),
                Figcaption("The garage screen"),
            ),
        ),
        Footer(P("© 2026 RideKeeper — built with Swift & WingedSwift")),
    )
    return Document(head, body, lang="pt-BR")
