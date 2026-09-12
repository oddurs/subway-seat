"use client";

import * as stylex from "@stylexjs/stylex";
import { useMemo, useState } from "react";
import { blend, contrast, fromLch, toLch } from "@/lib/oklab";
import {
  type ColorName,
  type FlavorId,
  accents,
  families,
  flavors,
  ground,
  roles,
  textRoles,
} from "@/lib/palette";
import { space } from "@/theme/space.stylex";
import { font } from "@/theme/type.stylex";

/**
 * A darkroom for the palette.
 *
 * Everything is a knob over OKLCH, because that is what the palette is solved
 * in: lightness, chroma and hue move independently, so "same colour, more of
 * it" and "same weight, different hue" are each one slider rather than a guess
 * in hex. The grain of the controls follows the grain of the system — one hue
 * and one chroma for the whole ground, a chroma for each of the two accent
 * bands, then per-role trims on top, the way you'd grade globally first and
 * touch individual colours last.
 *
 * The floors are live. Every value the repo's tests assert is recomputed on
 * each move and shown red the moment it breaks, so a palette can't be tuned
 * into something the build would reject.
 */

/** The four accents used as large fills; they have to hold an even band. */
const STRIPE: ColorName[] = ["red", "orange", "yellow", "green"];

type Trim = { dL: number; dC: number; dh: number };
const ZERO: Trim = { dL: 0, dC: 0, dh: 0 };

type Knobs = {
  groundHue: number;
  groundChroma: number;
  groundLift: number;
  stripeChroma: number;
  supportChroma: number;
  trims: Record<string, Trim>;
};

function baseKnobs(id: FlavorId): Knobs {
  const f = flavors.find((x) => x.id === id);
  if (!f) throw new Error(id);
  return {
    groundHue: toLch(f.colors.base).h,
    groundChroma: 1,
    groundLift: 0,
    stripeChroma: 1,
    supportChroma: 1,
    trims: {},
  };
}

/** Rebuild all 26 roles from the flavor's own values plus the knobs. */
function derive(id: FlavorId, k: Knobs): Record<ColorName, string> {
  const f = flavors.find((x) => x.id === id);
  if (!f) throw new Error(id);
  const out = {} as Record<ColorName, string>;
  for (const role of roles) {
    const src = toLch(f.colors[role]);
    const t = k.trims[role] ?? ZERO;
    const isGround = ([...ground, ...textRoles] as string[]).includes(role);
    const band = (STRIPE as string[]).includes(role) ? k.stripeChroma : k.supportChroma;
    out[role] = fromLch({
      L: Math.min(0.995, Math.max(0.02, src.L + (isGround ? k.groundLift : 0) + t.dL)),
      C: Math.max(0, src.C * (isGround ? k.groundChroma : band) + t.dC),
      h: (isGround ? k.groundHue : src.h) + t.dh,
    });
  }
  return out;
}

/** The floors from tests/test_palette.py, recomputed live. */
function report(c: Record<ColorName, string>, dark: boolean) {
  const SYN: [string, ColorName][] = [
    ["comment", "overlay1"],
    ["keyword", "orange"],
    ["function", "yellow"],
    ["string", "green"],
    ["type", "sage"],
    ["number", "redHi"],
    ["regex", "clay"],
    ["link", "denim"],
    ["operator", "overlay2"],
    ["variable", "text"],
    ["parameter", "subtext1"],
    ["invalid", "red"],
  ];
  const g = dark ? c.crust : "#FFFFFF";
  const tint = (role: ColorName, a: number) => blend(c[role], g, a);
  const rows = [
    { label: "text on base", got: contrast(c.text, c.base), min: 7 },
    { label: "text_hi on base", got: contrast(c.textHi, c.base), min: 7 },
    { label: "subtext0 on base", got: contrast(c.subtext0, c.base), min: 6 },
    { label: "subtext1 on base", got: contrast(c.subtext1, c.base), min: 6 },
    ...SYN.map(([name, role]) => ({
      label: `${name} on base`,
      got: contrast(c[role], c.base),
      min: 3.4,
    })),
    {
      label: "comment on added",
      got: contrast(c.overlay1, tint("green", dark ? 0.22 : 0.26)),
      min: 2.8,
    },
    {
      label: "comment on removed",
      got: contrast(c.overlay1, tint("red", dark ? 0.26 : 0.2)),
      min: 2.8,
    },
  ];
  return rows;
}

const SAMPLE: [string, ColorName][][] = [
  [["# fare.py — the spine every family runs on", "overlay1"]],
  [
    ["class ", "orange"],
    ["Journey", "sage"],
    ["(", "overlay2"],
    ["Segment", "sage"],
    ["):", "overlay2"],
  ],
  [["    @cached", "clay"]],
  [
    ["    def ", "orange"],
    ["fare", "yellow"],
    ["(", "overlay2"],
    ["self", "redHi"],
    [", ", "overlay2"],
    ["zones", "subtext1"],
    [") -> ", "overlay2"],
    ["float", "sage"],
    [":", "overlay2"],
  ],
  [
    ["        cap ", "text"],
    ["= ", "overlay2"],
    ["8.90", "redHi"],
    ["  if ", "orange"],
    ["zones ", "text"],
    ["> ", "overlay2"],
    ["4", "redHi"],
  ],
  [
    ["        return ", "orange"],
    ["min", "yellow"],
    ["(", "overlay2"],
    ["self", "redHi"],
    [".", "overlay2"],
    ["total", "subtext1"],
    [")", "overlay2"],
  ],
];

export function Studio() {
  const [id, setId] = useState<FlavorId>("guimard");
  const [k, setK] = useState<Knobs>(() => baseKnobs("guimard"));
  const flavor = flavors.find((f) => f.id === id);
  const c = useMemo(() => derive(id, k), [id, k]);
  const rows = useMemo(() => report(c, flavor?.dark ?? true), [c, flavor]);
  const broken = rows.filter((r) => r.got < r.min);

  const pick = (next: FlavorId) => {
    setId(next);
    setK(baseKnobs(next));
  };
  const set = (key: keyof Knobs, v: number) => setK((p) => ({ ...p, [key]: v }));
  const trim = (role: string, field: keyof Trim, v: number) =>
    setK((p) => ({
      ...p,
      trims: { ...p.trims, [role]: { ...(p.trims[role] ?? ZERO), [field]: v } },
    }));

  const python = `    colors={\n${roles
    .map((r) => `        "${r.replace(/([A-Z])/g, (m) => `_${m.toLowerCase()}`)}": "${c[r]}",`)
    .join("\n")}\n    },`;

  const stripeSpread = (() => {
    const v = STRIPE.map((r) => toLch(c[r]).C);
    return Math.max(...v) - Math.min(...v);
  })();

  return (
    <div {...stylex.props(s.page)} style={{ background: c.crust, color: c.text }}>
      <header {...stylex.props(s.bar)} style={{ background: c.mantle, borderColor: c.surface1 }}>
        <b {...stylex.props(s.title)} style={{ color: c.textHi }}>
          Studio
        </b>
        <select
          id="studio-flavor"
          value={id}
          onChange={(e) => pick(e.target.value as FlavorId)}
          {...stylex.props(s.select)}
          style={{ background: c.surface0, color: c.text, borderColor: c.surface2 }}
        >
          {families.map((fam) => (
            <optgroup key={fam.id} label={fam.name}>
              {flavors
                .filter((f) => f.family === fam.id)
                .map((f) => (
                  <option key={f.id} value={f.id}>
                    {f.name}
                  </option>
                ))}
            </optgroup>
          ))}
        </select>
        <span {...stylex.props(s.verdict)} style={{ color: broken.length ? c.red : c.green }}>
          {broken.length
            ? `${broken.length} floor${broken.length > 1 ? "s" : ""} broken`
            : "all floors clear"}
        </span>
        <button
          type="button"
          onClick={() => pick(id)}
          {...stylex.props(s.reset)}
          style={{ color: c.subtext0 }}
        >
          Reset
        </button>
      </header>

      <div {...stylex.props(s.body)}>
        <div {...stylex.props(s.controls)} style={{ borderColor: c.surface1 }}>
          <Group title="Ground" c={c}>
            <Slider
              label="Hue"
              v={k.groundHue}
              min={0}
              max={360}
              step={0.5}
              unit="°"
              c={c}
              onChange={(v) => set("groundHue", v)}
            />
            <Slider
              label="Chroma"
              v={k.groundChroma}
              min={0}
              max={2.5}
              step={0.01}
              unit="×"
              c={c}
              onChange={(v) => set("groundChroma", v)}
            />
            <Slider
              label="Lift"
              v={k.groundLift}
              min={-0.08}
              max={0.08}
              step={0.002}
              c={c}
              onChange={(v) => set("groundLift", v)}
            />
          </Group>

          <Group title="Accent bands" c={c}>
            <Slider
              label="Stripe"
              v={k.stripeChroma}
              min={0}
              max={2}
              step={0.01}
              unit="×"
              c={c}
              onChange={(v) => set("stripeChroma", v)}
            />
            <Slider
              label="Support"
              v={k.supportChroma}
              min={0}
              max={2}
              step={0.01}
              unit="×"
              c={c}
              onChange={(v) => set("supportChroma", v)}
            />
            <p
              {...stylex.props(s.hint)}
              style={{ color: stripeSpread > 0.05 ? c.red : c.subtext0 }}
            >
              stripe spread {stripeSpread.toFixed(3)} — Walnut sits at 0.045; above about 0.05 a
              prompt stripe starts to wobble.
            </p>
          </Group>

          <Group title="Per accent" c={c}>
            {accents.map((role) => {
              const t = k.trims[role] ?? ZERO;
              return (
                <div key={role} {...stylex.props(s.trim)}>
                  <span {...stylex.props(s.swatch)} style={{ background: c[role] }} />
                  <span {...stylex.props(s.trimName)} style={{ color: c.subtext1 }}>
                    {role}
                  </span>
                  <MiniSlider
                    label="L"
                    v={t.dL}
                    min={-0.15}
                    max={0.15}
                    step={0.002}
                    c={c}
                    onChange={(v) => trim(role, "dL", v)}
                  />
                  <MiniSlider
                    label="C"
                    v={t.dC}
                    min={-0.1}
                    max={0.1}
                    step={0.002}
                    c={c}
                    onChange={(v) => trim(role, "dC", v)}
                  />
                  <MiniSlider
                    label="H"
                    v={t.dh}
                    min={-40}
                    max={40}
                    step={0.5}
                    c={c}
                    onChange={(v) => trim(role, "dh", v)}
                  />
                  <code {...stylex.props(s.hex)} style={{ color: c.overlay2 }}>
                    {c[role]}
                  </code>
                </div>
              );
            })}
          </Group>
        </div>

        <div {...stylex.props(s.preview)}>
          <div {...stylex.props(s.ramp)}>
            {[...ground, ...textRoles].map((r) => (
              <span key={r} {...stylex.props(s.rampCell)} style={{ background: c[r] }} />
            ))}
          </div>

          <pre {...stylex.props(s.code)} style={{ background: c.base }}>
            {SAMPLE.map((line, i) => (
              // biome-ignore lint/suspicious/noArrayIndexKey: fixed sample
              <div key={i}>
                {line.map(([text, role]) => (
                  <span key={text} style={{ color: c[role] }}>
                    {text}
                  </span>
                ))}
              </div>
            ))}
          </pre>

          <div {...stylex.props(s.stripe)}>
            {STRIPE.map((r) => (
              <span key={r} {...stylex.props(s.seg)} style={{ background: c[r], color: c.crust }}>
                {r}
              </span>
            ))}
          </div>

          <div {...stylex.props(s.floors)}>
            {rows.map((r) => {
              const ok = r.got >= r.min;
              return (
                <div
                  key={r.label}
                  {...stylex.props(s.floor)}
                  style={{ color: ok ? c.subtext0 : c.red }}
                >
                  <span>{r.label}</span>
                  <b style={{ color: ok ? c.text : c.red }}>{r.got.toFixed(2)}</b>
                  <span {...stylex.props(s.min)}>≥ {r.min}</span>
                </div>
              );
            })}
          </div>

          <textarea
            id="studio-out"
            readOnly
            value={python}
            {...stylex.props(s.out)}
            style={{ background: c.base, color: c.subtext1, borderColor: c.surface1 }}
          />
          <p {...stylex.props(s.hint)} style={{ color: c.subtext0 }}>
            Paste that over the flavor&apos;s <code>colors=</code> block in <code>palette.py</code>,
            then run <code>./build.py</code>. The studio never writes the file itself — the palette
            stays the one source of truth, and the change arrives as a diff you can read.
          </p>
        </div>
      </div>
    </div>
  );
}

function Group({
  title,
  c,
  children,
}: {
  title: string;
  c: Record<ColorName, string>;
  children: React.ReactNode;
}) {
  return (
    <section {...stylex.props(s.group)} style={{ borderColor: c.surface1 }}>
      <h2 {...stylex.props(s.groupTitle)} style={{ color: c.textHi }}>
        {title}
      </h2>
      {children}
    </section>
  );
}

function Slider({
  label,
  v,
  min,
  max,
  step,
  unit,
  c,
  onChange,
}: {
  label: string;
  v: number;
  min: number;
  max: number;
  step: number;
  unit?: string;
  c: Record<ColorName, string>;
  onChange: (v: number) => void;
}) {
  const id = `k-${label.toLowerCase()}`;
  return (
    <label htmlFor={id} {...stylex.props(s.row)}>
      <span {...stylex.props(s.label)} style={{ color: c.subtext0 }}>
        {label}
      </span>
      <input
        id={id}
        type="range"
        value={v}
        min={min}
        max={max}
        step={step}
        onChange={(e) => onChange(Number(e.target.value))}
        {...stylex.props(s.range)}
      />
      <output {...stylex.props(s.value)} style={{ color: c.text }}>
        {v.toFixed(step < 0.01 ? 3 : 2)}
        {unit ?? ""}
      </output>
    </label>
  );
}

function MiniSlider({
  label,
  v,
  min,
  max,
  step,
  c,
  onChange,
}: {
  label: string;
  v: number;
  min: number;
  max: number;
  step: number;
  c: Record<ColorName, string>;
  onChange: (v: number) => void;
}) {
  return (
    <label {...stylex.props(s.mini)} title={label}>
      <span style={{ color: c.overlay1 }}>{label}</span>
      <input
        type="range"
        value={v}
        min={min}
        max={max}
        step={step}
        onChange={(e) => onChange(Number(e.target.value))}
        {...stylex.props(s.range)}
      />
    </label>
  );
}

const s = stylex.create({
  page: { minHeight: "100vh", fontFamily: font.sans },
  bar: {
    display: "flex",
    gap: space.s4,
    alignItems: "center",
    paddingBlock: space.s3,
    paddingInline: space.s5,
    borderBottomStyle: "solid",
    borderBottomWidth: 1,
  },
  title: { fontSize: font.sizeHead, fontWeight: 700, letterSpacing: font.trackHead },
  select: {
    padding: 6,
    fontFamily: font.sans,
    fontSize: font.sizeSmall,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "var(--radius-pill)",
  },
  verdict: { marginLeft: "auto", fontFamily: font.mono, fontSize: font.sizeMicro },
  reset: {
    padding: 6,
    fontFamily: font.sans,
    fontSize: font.sizeMicro,
    cursor: "pointer",
    backgroundColor: "transparent",
    borderWidth: 0,
  },
  body: {
    display: "grid",
    gridTemplateColumns: {
      default: "minmax(0,1fr)",
      "@media (min-width: 1000px)": "380px minmax(0,1fr)",
    },
    gap: space.s5,
    alignItems: "start",
    padding: space.s5,
  },
  controls: { display: "grid", gap: space.s4 },
  group: {
    display: "grid",
    gap: space.s2,
    padding: space.s4,
    borderStyle: "solid",
    borderWidth: 1,
  },
  groupTitle: {
    margin: 0,
    fontSize: font.sizeMicro,
    fontWeight: 700,
    textTransform: "uppercase",
    letterSpacing: font.trackLabel,
  },
  row: {
    display: "grid",
    gridTemplateColumns: "58px minmax(0,1fr) 62px",
    gap: space.s2,
    alignItems: "center",
  },
  label: { fontSize: font.sizeMicro },
  range: { width: "100%", accentColor: "currentColor" },
  value: { fontFamily: font.mono, fontSize: font.sizeMicro, textAlign: "right" },
  trim: {
    display: "grid",
    gridTemplateColumns: "14px 74px repeat(3, minmax(0,1fr)) 70px",
    gap: space.s2,
    alignItems: "center",
  },
  swatch: { width: 14, height: 14, borderRadius: "var(--radius-chip)" },
  trimName: { fontFamily: font.mono, fontSize: 11 },
  mini: {
    display: "grid",
    gridTemplateColumns: "10px minmax(0,1fr)",
    gap: 4,
    alignItems: "center",
    fontSize: 9,
  },
  hex: { fontFamily: font.mono, fontSize: 10.5, textAlign: "right" },
  preview: { display: "grid", gap: space.s4 },
  ramp: { display: "flex", height: 34 },
  rampCell: { flexGrow: "1", flexShrink: "1", flexBasis: "0", minWidth: 0 },
  code: {
    padding: space.s4,
    margin: 0,
    overflowX: "auto",
    fontFamily: font.mono,
    fontSize: 13,
    lineHeight: 1.7,
  },
  stripe: { display: "flex" },
  seg: {
    flexGrow: "1",
    flexShrink: "1",
    flexBasis: "0",
    padding: 8,
    fontFamily: font.mono,
    fontSize: 11,
    fontWeight: 700,
    textAlign: "center",
  },
  floors: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(210px, 1fr))",
    gap: space.s1,
  },
  floor: {
    display: "grid",
    gridTemplateColumns: "minmax(0,1fr) 46px 44px",
    gap: space.s2,
    fontFamily: font.mono,
    fontSize: 11,
  },
  min: { opacity: 0.6 },
  out: {
    width: "100%",
    minHeight: 230,
    padding: space.s3,
    fontFamily: font.mono,
    fontSize: 11.5,
    lineHeight: 1.55,
    resize: "vertical",
    borderStyle: "solid",
    borderWidth: 1,
  },
  hint: { margin: 0, fontSize: font.sizeMicro, lineHeight: 1.5 },
});
