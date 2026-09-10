"""Wallpapers: two flat SVG scenes per flavor, at 16:9, 16:10 and phone sizes.

"Stripes" is the site's supergraphic: five painted bands falling in from the top,
bending round one centre and running off to the right, over walnut paneling (cream
enamel panels in Enamel). "Seats" is the inside of the car: ad cards, windows with
tunnel lights streaking past, a stainless rail, and a bench of orange and gold
bucket seats between two stanchions.

Everything is flat vector with vertical-only texture, so the SVGs look the same in
every renderer (KDE's has no filters) and the PNG renders in assets/wallpapers stay
small. scripts/render-wallpapers.sh makes those PNGs.
"""

import random

import palette as p
from ports._lib import HEADER, Out, ui_colors

META = {
    "id": "wallpapers",
    "name": "Wallpapers",
    "category": "Desktop",
    "homepage": "https://github.com/oddurs/subway-seat/tree/main/assets/wallpapers",
    "enable": {
        "where": "a shell (GNOME or KDE Plasma)",
        "code": '# GNOME\ngsettings set org.gnome.desktop.background picture-uri "file://$HOME/Pictures/Subway Seat/{slug}-stripes-16x10.svg"\n'
        'gsettings set org.gnome.desktop.background picture-uri-dark "file://$HOME/Pictures/Subway Seat/{slug}-stripes-16x10.svg"\n'
        '# KDE Plasma\nplasma-apply-wallpaperimage "$HOME/Pictures/Subway Seat/{slug}-stripes-16x10.svg"',
        "lang": "sh",
    },
    "auto": {
        "where": "a shell (GNOME keeps a light and a dark picture)",
        "code": 'gsettings set org.gnome.desktop.background picture-uri "file://$HOME/Pictures/Subway Seat/subway-seat-enamel-stripes-16x10.svg"\n'
        'gsettings set org.gnome.desktop.background picture-uri-dark "file://$HOME/Pictures/Subway Seat/subway-seat-stripes-16x10.svg"',
        "lang": "sh",
    },
    "notes": "Two flat scenes in each flavor: the supergraphic stripes on walnut paneling, and a row of "
    "orange and gold bucket seats under the tunnel lights. SVGs at 16:9, 16:10 and phone size; PNGs at "
    "5K, 4K, 2560×1600 and 1290×2796 are in assets/wallpapers. macOS needs a PNG.",
}

HOW = (
    "set it in GNOME's Settings › Appearance or KDE's Desktop and Wallpaper; "
    "macOS can't show SVGs, so use the PNG from assets/wallpapers (right-click › Set Desktop Picture)"
)

# viewBox (the drawing's units) and the intrinsic size a viewer rasterizes at
SIZES = {
    "16x9": ((1920, 1080), (5120, 2880)),
    "16x10": ((1920, 1200), (3840, 2400)),
    "phone": ((1290, 2796), (1290, 2796)),
}


def num(v):
    """Compact, stable numbers for the SVG text."""
    return f"{v:.1f}".rstrip("0").rstrip(".") or "0"


def rect(x, y, w, h, fill, rx=0, op=None, extra=""):
    r = f' rx="{num(rx)}"' if rx else ""
    o = f' fill-opacity="{f"{op:.3f}".rstrip("0").rstrip(".")}"' if op is not None else ""
    return f'<rect x="{num(x)}" y="{num(y)}" width="{num(w)}" height="{num(h)}"{r} fill="{fill}"{o}{extra}/>'


def svg(W, H, size, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{size[0]}" height="{size[1]}">'
        f"<!-- {HEADER} -->\n<title>{title}</title>\n{body}</svg>\n"
    )


def light(f):
    """The lightest thing in the room: ivory on the dark flavors, a paper white on Enamel."""
    return f.text_hi if f.dark else ui_colors(f)["paper"]


def dark(f):
    return f.crust if f.dark else f.text


def paneling(f, x0, y0, w, h, board, seed=1972):
    """Walnut paneling (straight grain and V-grooves), or cream enamel panels with seams.
    Everything is vertical, so every row of a render is the same and PNGs compress to almost nothing."""
    out = []
    if f.dark:
        rnd = random.Random(seed)
        x = x0
        while x < x0 + w:
            x += rnd.uniform(2, 14)
            grain = f.crust if rnd.random() < 0.75 else f.surface1
            out.append(rect(x, y0, rnd.uniform(0.4, 2.2), h, grain, op=rnd.uniform(0.04, 0.14)))
    k = 1
    while k * board < w:
        gx = x0 + k * board
        out.append(rect(gx - 1.5, y0, 3, h, dark(f), op=0.5 if f.dark else 0.1))
        out.append(rect(gx + 1.5, y0, 1, h, light(f), op=0.05 if f.dark else 0.9))
        k += 1
    return "".join(out)


# ── Stripes ────────────────────────────────────────────────────────────────
def bands(f):
    if f.dark:
        return [f.red, f.orange, f.yellow, f.green, f.text]
    return [f.red_hi, f.orange_hi, f.yellow_hi, f.green_hi, f.overlay2]


def stripes(f, W, H):
    s = H if W > H else 0.82 * W
    w, gap, r0 = 0.044 * s, 0.008 * s, 0.17 * s
    cx, cy = (0.42 * W, 0.40 * H) if W > H else (0.52 * W, 0.54 * H)
    board = 0.14 * s
    body = [rect(0, 0, W, H, f.base), paneling(f, 0, 0, W, H, board)]
    for i, color in enumerate(bands(f)):
        r = r0 + i * (w + gap) + w / 2
        body.append(
            f'<path d="M {num(cx - r)} -10 V {num(cy)} A {num(r)} {num(r)} 0 0 0 {num(cx)} {num(cy + r)} H {W + 10}" '
            f'fill="none" stroke="{color}" stroke-width="{num(w)}"/>'
        )
    # the paneling's grooves show through the paint
    k = 1
    while k * board < W:
        body.append(rect(k * board - 1.5, 0, 3, H, dark(f), op=0.07 if f.dark else 0.05))
        k += 1
    return "\n".join(body)


# ── Seats ──────────────────────────────────────────────────────────────────
def tunnel_lights(f, x0, y0, w, h, u, seed=46):
    """Lights streaking past in the dark, like a long exposure: random streaks in five lanes
    and a lane of evenly spaced lamps. Returns (x0, x1, y, thickness, color, glow) across the
    whole band, so the same lights run on behind every window."""
    rnd = random.Random(seed)
    warm = (f.yellow, f.orange, f.yellow_hi, f.orange_hi, light(f))
    out = []
    for lane, t in ((0.14, 1.6), (0.3, 2.6), (0.5, 3.4), (0.68, 2.2), (0.86, 4.2)):
        x = x0 - rnd.uniform(0, 400) * u
        while x < x0 + w:
            length = rnd.uniform(90, 620) * u
            out.append((x, x + length, y0 + lane * h, t * u, rnd.choice(warm), rnd.uniform(0.55, 1.0)))
            x += length + rnd.uniform(60, 520) * u
    x = x0 - 120 * u
    while x < x0 + w:  # the tunnel's own lamps
        out.append((x, x + 150 * u, y0 + 0.4 * h, 2.8 * u, light(f), 0.9))
        x += 330 * u
    return out


def capsule(x0, x1, y, a, color, op, round_left, round_right):
    """A bar of half-height `a` from x0 to x1, with rounded or square ends."""
    left, right = (x0 + a, x1 - a)
    if right < left:
        left = right = (x0 + x1) / 2
    d = [f"M {num(left if round_left else x0)} {num(y - a)}", f"H {num(right if round_right else x1)}"]
    d.append(f"A {num(a)} {num(a)} 0 0 1 {num(right)} {num(y + a)}" if round_right else f"V {num(y + a)}")
    d.append(f"H {num(left if round_left else x0)}")
    d.append(f"A {num(a)} {num(a)} 0 0 1 {num(left)} {num(y - a)}" if round_left else f"V {num(y - a)}")
    return f'<path d="{" ".join(d)} Z" fill="{color}" fill-opacity="{f"{op:.3f}".rstrip("0").rstrip(".")}"/>'


def pane_view(f, pane, radius, glass, lights):
    """One window: the glass, the lights cut to its rounded outline, and a faint glare.
    The lights are cut here instead of with a clipPath, which KDE's SVG renderer ignores."""
    x, y, w, h = pane

    def inset(yy):  # how far the rounded corners pull the outline in at height yy
        d = max(y + radius - yy, yy - (y + h - radius), 0)
        return radius - (max(radius * radius - d * d, 0)) ** 0.5

    out = [rect(x, y, w, h, glass, rx=radius)]
    for sx0, sx1, sy, t, color, glow in lights:
        # a soft outer halo, an inner halo and the bright core
        for a, pad, op in ((3.5 * t, 4 * t, glow * 0.07), (1.5 * t, 1.5 * t, glow * 0.22), (t / 2, 0, glow)):
            if sy - a < y or sy + a > y + h:
                continue
            cut = max(inset(sy - a), inset(sy + a))
            lo, hi = max(sx0 - pad, x + cut), min(sx1 + pad, x + w - cut)
            if hi - lo > 0.5:
                out.append(capsule(lo, hi, sy, a, color, op, lo > x + cut, hi < x + w - cut))
    g = x + w * 0.2  # the glare's corners stay clear of the rounded ones
    out.append(
        f'<path d="M {num(g)} {num(y + h)} L {num(g + 0.45 * h)} {num(y)} H {num(g + 0.7 * h)} L {num(g + 0.25 * h)} {num(y + h)} Z" '
        f'fill="{light(f)}" fill-opacity="0.05"/>'
    )
    return "".join(out)


def seat(f, x, y, w, h, color, warmer):
    """One molded bucket seat seen from across the car: its shadow on the wall, the back
    with a lit rim, the scoop, and the pan's front lip. Shade leans toward the next warmer
    accent (gold toward orange, orange toward red), the way painted shadows do."""
    hi = f.mix(light(f), color, 0.16)
    rim = f.mix(light(f), color, 0.3)
    lo = f.mix(dark(f), p.blend(color, warmer, 0.5), 0.2)
    back = h * 0.74
    pan = y + back * 0.84
    return "".join(
        (
            rect(x + w * 0.05, y + h * 0.04, w, back, dark(f), rx=w * 0.3, op=0.3 if f.dark else 0.1),
            rect(x, y, w, back, rim, rx=w * 0.3),
            rect(x, y + h * 0.012, w, back - h * 0.012, color, rx=w * 0.3),
            rect(x + w * 0.14, y + back * 0.1, w * 0.72, back * 0.72, hi, rx=w * 0.22),
            rect(x - w * 0.035, pan, w * 1.07, y + h - pan, lo, rx=w * 0.12),
            rect(x - w * 0.035, pan, w * 1.07, h * 0.075, color, rx=w * 0.035),
        )
    )


def ad_card(f, x, y, w, h, kind, u):
    """The cards above the windows: a tiny supergraphic, a sun over lines, or a headline."""
    frame = f.surface1 if f.dark else f.crust
    face = f.surface0 if f.dark else ui_colors(f)["paper"]
    pad = 5 * u
    out = [rect(x, y, w, h, frame, rx=5 * u), rect(x + pad, y + pad, w - 2 * pad, h - 2 * pad, face, rx=3 * u)]
    ix, iy, iw, ih = x + 2.5 * pad, y + 2.5 * pad, w - 5 * pad, h - 5 * pad
    ink = f.overlay0 if f.dark else f.surface2
    if kind == 0:  # the stripes, small
        t = ih * 0.13
        cx, cy = ix + iw * 0.4, iy + ih * 0.1
        for i, color in enumerate(bands(f)):
            r = ih * 0.1 + i * t + t / 2
            out.append(
                f'<path d="M {num(cx - r)} {num(iy)} V {num(cy)} A {num(r)} {num(r)} 0 0 0 {num(cx)} {num(cy + r)} H {num(ix + iw)}" '
                f'fill="none" stroke="{color}" stroke-width="{num(t * 0.82)}"/>'
            )
    elif kind == 1:  # a sun over two lines of type
        out.append(
            f'<circle cx="{num(ix + ih * 0.5)}" cy="{num(iy + ih * 0.5)}" r="{num(ih * 0.45)}" fill="{f.orange}"/>'
        )
        out.append(rect(ix + ih * 1.3, iy + ih * 0.18, iw * 0.55, ih * 0.2, ink, rx=ih * 0.1))
        out.append(rect(ix + ih * 1.3, iy + ih * 0.58, iw * 0.35, ih * 0.2, ink, rx=ih * 0.1, op=0.6))
    else:  # a headline and a gold rule
        out.append(rect(ix, iy + ih * 0.08, iw * 0.7, ih * 0.26, ink, rx=ih * 0.13))
        out.append(rect(ix, iy + ih * 0.5, iw * 0.45, ih * 0.16, ink, rx=ih * 0.08, op=0.6))
        out.append(rect(ix, iy + ih * 0.84, iw, ih * 0.1, f.yellow))
    return "".join(out)


def stanchion(f, x, y0, y1, w):
    steel = f.overlay2 if f.dark else f.overlay0
    return "".join(
        (
            rect(x, y0, w, y1 - y0, steel),
            rect(x + w * 0.2, y0, w * 0.22, y1 - y0, light(f), op=0.55),
            rect(x + w * 0.7, y0, w * 0.3, y1 - y0, dark(f), op=0.28),
        )
    )


def seats(f, W, H):
    portrait = H > W
    u = W / 1290 if portrait else H / 1080  # one pixel of the 1080p (or phone) reference
    steel = f.overlay1 if f.dark else f.overlay0
    glass = p.blend(f.crust, "#000000", 0.5) if f.dark else f.text_hi
    body = [rect(0, 0, W, H, f.base)]

    # rows, top to bottom
    if portrait:
        cove, ad_y, ad_h = 0.1 * H, 0.03 * H, 0.05 * H
        win_y, win_h = 0.15 * H, 0.27 * H
        seat_y, floor_y = 0.535 * H, 0.84 * H
        n_seats, seat_w, seat_gap = 2, 0.38 * W, 0.012 * W
        n_win, win_w, win_gap = 1, 0.82 * W, 0.0
        ad_w, ad_gap = 0.4 * W, 0.04 * W
    else:
        cove, ad_y, ad_h = 0.15 * H, 0.035 * H, 0.08 * H
        win_y, win_h = 0.2 * H, 0.27 * H
        seat_y, floor_y = 0.56 * H, 0.86 * H
        n_seats, seat_w, seat_gap = 7, 0.1 * W, 0.006 * W
        n_win, win_w, win_gap = 4, 0.215 * W, 0.05 * W
        ad_w, ad_gap = 0.15 * W, 0.016 * W
    seat_h = floor_y - seat_y - 0.045 * H
    bench = n_seats * seat_w + (n_seats - 1) * seat_gap
    bx = (W - bench) / 2

    body.append(paneling(f, 0, cove, W, floor_y - cove, 150 * u))

    # ceiling cove: the ad cards and the long light under them
    body.append(rect(0, 0, W, cove, f.mantle))
    n_ads = int((W + ad_gap) // (ad_w + ad_gap)) + 1
    ax = (W - (n_ads * ad_w + (n_ads - 1) * ad_gap)) / 2
    for i in range(n_ads):
        body.append(ad_card(f, ax + i * (ad_w + ad_gap), ad_y, ad_w, ad_h, (i + 1) % 3, u))
    body.append(rect(0, cove - 9 * u, W, 5 * u, light(f), op=0.5 if f.dark else 0.9))
    body.append(rect(0, cove - 4 * u, W, 4 * u, dark(f), op=0.5 if f.dark else 0.12))

    # windows onto the tunnel
    wx = (W - (n_win * win_w + (n_win - 1) * win_gap)) / 2
    panes = [(wx + i * (win_w + win_gap), win_y, win_w, win_h) for i in range(n_win)]
    radius = 0.2 * win_h
    # the lights are drawn to the window's scale, so a phone's tall pane gets thicker streaks
    lights = tunnel_lights(f, 0, win_y, W, win_h, win_h / 292)
    body += [pane_view(f, pane, radius, glass, lights) for pane in panes]
    for x, y, w, h in panes:
        body.append(rect(x, y, w, h, "none", rx=radius, extra=f' stroke="{steel}" stroke-width="{num(8 * u)}"'))

    # stainless rail under the windows
    rail_y = win_y + win_h + 0.035 * H
    body.append(rect(0, rail_y, W, 14 * u, steel))
    body.append(rect(0, rail_y + 3 * u, W, 3 * u, light(f), op=0.4 if f.dark else 0.8))
    body.append(rect(0, rail_y + 14 * u, W, 6 * u, dark(f), op=0.3 if f.dark else 0.1))

    # the bench: its shadow, the heater grille, the seats
    under = seat_y + seat_h * 0.8
    body.append(rect(bx - 0.02 * W, under, bench + 0.04 * W, floor_y - under, dark(f), op=0.5 if f.dark else 0.14))
    slots = int(bench // (26 * u))
    for i in range(slots):
        body.append(
            rect(
                bx + (i + 0.3) * bench / slots,
                floor_y - 0.035 * H,
                bench / slots * 0.4,
                0.02 * H,
                dark(f),
                op=0.45 if f.dark else 0.16,
                rx=2 * u,
            )
        )
    pairs = (
        ((f.orange, f.red), (f.yellow, f.orange)) if f.dark else ((f.orange_hi, f.red_hi), (f.yellow_hi, f.orange_hi))
    )
    for i in range(n_seats):
        body.append(seat(f, bx + i * (seat_w + seat_gap), seat_y, seat_w, seat_h, *pairs[i % 2]))

    # floor, with a few seams running away from us
    body.append(rect(0, floor_y, W, H - floor_y, f.mantle if f.dark else f.crust))
    body.append(rect(0, floor_y, W, 5 * u, steel))
    y, step = floor_y + 0.03 * H, 0.025 * H
    while y < H:
        body.append(rect(0, y, W, 2 * u, dark(f), op=0.25 if f.dark else 0.07))
        y += step
        step *= 1.45

    # stanchions at each end of the bench
    pole = 18 * u
    for x in (bx - 0.035 * W - pole, bx + bench + 0.035 * W):
        body.append(stanchion(f, x, 0, floor_y + 0.02 * H, pole))
    return "\n".join(body)


DESIGNS = {"stripes": stripes, "seats": seats}


def build(flavors):
    outs = []
    for f in flavors:
        for design, draw in DESIGNS.items():
            for key, ((W, H), size) in SIZES.items():
                name = f"{f.slug}-{design}-{key}.svg"
                outs.append(
                    Out(
                        name,
                        svg(W, H, size, draw(f, W, H), f"{f.name}: {design}"),
                        flavor=f.id,
                        dest=f"~/Pictures/Subway Seat/{name}",
                        lang="xml",
                        how=HOW,
                    )
                )
    return outs
