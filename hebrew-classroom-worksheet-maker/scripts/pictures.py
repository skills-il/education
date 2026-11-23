#!/usr/bin/env python3
"""A small set of black line pictures that survive a photocopier.

Each picture lists its pointed Hebrew name, so a homograph cannot pass. The list cannot prove that
a child will name the drawing this way, so a person still looks at every picture.
"""

S = 'fill="none" stroke="#000" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'


def svg(body):
    return f'<svg viewBox="0 0 64 64" aria-hidden="true"><g {S}>{body}</g></svg>'


PICTURES = {
    "dreidel": {"names": ["סְבִיבוֹן"], "svg": svg(
        '<path d="M32 6v10"/><path d="M18 16h28v22L32 58 18 38z"/><path d="M18 27h28"/>'
        '<path d="M26 33c3-3 9-3 12 0"/>')},
    "candle": {"names": ["נֵר"], "svg": svg(
        '<path d="M24 26h16v30H24z"/><path d="M32 26v-5"/><path d="M32 6c5 6 5 11 0 15-5-4-5-9 0-15z"/>'
        '<path d="M16 58h32"/>')},
    "apple": {"names": ["תַּפּוּחַ"], "svg": svg(
        '<path d="M32 20c-6-5-20-3-20 13 0 12 8 25 15 25 2 0 3-1 5-1s3 1 5 1c7 0 15-13 15-25 0-16-14-18-20-13z"/>'
        '<path d="M32 20c0-6 2-10 6-13"/><path d="M36 13c5-4 10-3 13 0-4 4-9 4-13 0z"/>')},
    "fish": {"names": ["דָּג"], "svg": svg(
        '<path d="M6 32c8-13 28-15 40 0-12 15-32 13-40 0z"/><path d="M46 32l12-10v20z"/>'
        '<circle cx="18" cy="28" r="2"/><path d="M28 22c3 6 3 14 0 20"/>')},
    "house": {"names": ["בַּיִת"], "svg": svg(
        '<path d="M8 30L32 8l24 22"/><path d="M14 26v30h36V26"/><path d="M27 56V40h10v16"/>')},
    "sun": {"names": ["שֶׁמֶשׁ"], "svg": svg(
        '<circle cx="32" cy="32" r="12"/><path d="M32 6v9M32 49v9M6 32h9M49 32h9'
        'M14 14l6 6M44 44l6 6M50 14l-6 6M20 44l-6 6"/>')},
    "tree": {"names": ["עֵץ"], "svg": svg(
        '<path d="M32 6c-13 0-22 9-20 21-6 10 3 21 14 19h12c11 2 20-9 14-19 2-12-7-21-20-21z"/>'
        '<path d="M28 46v12h8V46"/>')},
    "book": {"names": ["סֵפֶר"], "svg": svg(
        '<path d="M32 16c-6-5-16-6-24-4v38c8-2 18-1 24 4 6-5 16-6 24-4V12c-8-2-18-1-24 4z"/>'
        '<path d="M32 16v38"/>')},
}
