"use client";

import * as stylex from "@stylexjs/stylex";
import { useEffect, useMemo, useState } from "react";
import { blend, contrast, fromLch, toLch } from "@/lib/oklab";
import {
  accents,
  type ColorName,
  families,
  type FlavorId,
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
 * Every knob is over OKLCH, because that is what the palette is solved in:
 * lightness, chroma and hue move independently, so "same colour, more of it"
 * and "same weight, different hue" are each one slider rather than a guess in
 * hex. The grain of the controls follows the grain of the system — one hue and
 * one chroma for the whole ground, a chroma for each of the two accent bands,
 * then per-role trims last, the way you grade globally before touching
 * individual colours.
 *
 * The floors are live. Every value the repo's tests assert is recomputed on
 * each move and goes red the moment it breaks, so a palette can't be graded
 * into something `./build.py` would reject.
 *
 * Edits are kept per flavor and survive both switching flavor and reloading, so
 * the nine can be worked on in any order.
 */

/** The four accents used as large fills; they have to hold an even band. */
const STRIPE: ColorName[] = ["red", "orange", "yellow", "green"];
const STORE = "subway-seat:studio";

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

const flavorOf = (id: FlavorId) => {
  const f = flavors.find((x) => x.id === id);
  if (!f) throw new Error(`unknown flavor ${id}`);
  return f;
};

const baseKnobs = (id: FlavorId): Knobs => ({
  groundHue: toLch(flavorOf(id).colors.base).h,
  groundChroma: 1,
  groundLift: 0,
  stripeChroma: 1,
  supportChroma: 1,
  trims: {},
});

const isDefault = (id: FlavorId, k: Knobs) => {
  const b = baseKnobs(id);
  return (
    Math.abs(k.groundHue - b.groundHue) < 0.01 &&
    k.groundChroma === 1 &&
    k.groundLift === 0 &&
    k.stripeChroma === 1 &&
    k.supportChroma === 1 &&
    Object.values(k.trims).every((t) => t.dL === 0 && t.dC === 0 && t.dh === 0)
  );
};

/** Rebuild all 26 roles from the flavor's own values plus the knobs. */
function derive(id: FlavorId, k: Knobs): Record<ColorName, string> {
  const f = flavorOf(id);
  const out = {} as Record<ColorName, string>;
  const groundRoles = [...ground, ...textRoles] as string[];
  for (const role of roles) {
    const src = toLch(f.colors[role]);
    const t = k.trims[role] ?? ZERO;
    const isGround = groundRoles.includes(role);
    const band = (STRIPE as string[]).includes(role) ? k.stripeChroma : k.supportChroma;
    out[role] = fromLch({
      L: Math.min(0.995, Math.max(0.02, src.L + (isGround ? k.groundLift : 0) + t.dL)),
      C: Math.max(0, src.C * (isGround ? k.groundChroma : band) + t.dC),
      h: (isGround ? k.groundHue : src.h) + t.dh,
    });
  }
  return out;
}

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

/** The floors from tests/test_palette.py, recomputed live. */
function report(c: Record<ColorName, string>, dark: boolean) {
  const g = dark ? c.crust : "#FFFFFF";
  const tint = (role: ColorName, a: number) => blend(c[role], g, a);
  return [
    { label: "text on base", got: contrast(c.text, c.base), min: 7, roles: ["text"] },
    { label: "text_hi on base", got: contrast(c.textHi, c.base), min: 7, roles: ["textHi"] },
    { label: "subtext0 on base", got: contrast(c.subtext0, c.base), min: 6, roles: ["subtext0"] },
    { label: "subtext1 on base", got: contrast(c.subtext1, c.base), min: 6, roles: ["subtext1"] },
    ...SYN.map(([name, role]) => ({
      label: `${name} on base`,
      got: contrast(c[role], c.base),
      min: 3.4,
      roles: [role as string],
    })),
    {
      label: "comment on added",
      got: contrast(c.overlay1, tint("green", dark ? 0.22 : 0.26)),
      min: 2.8,
      roles: ["overlay1", "green"],
    },
    {
      label: "comment on removed",
      got: contrast(c.overlay1, tint("red", dark ? 0.26 : 0.2)),
      min: 2.8,
      roles: ["overlay1", "red"],
    },
  ];
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

const snake = (r: string) => r.replace(/([A-Z])/g, (m) => `_${m.toLowerCase()}`);

function loadAll(): Record<string, Knobs> {
  try {
    return JSON.parse(localStorage.getItem(STORE) ?? "{}");
  } catch {
    return {};
  }
}

export function Studio() {
  const [id, setId] = useState<FlavorId>("guimard");
  // Read straight from storage: the page is client-only, so there is no server
  // render for this to disagree with, and edits survive a reload.
  const [all, setAll] = useState<Record<string, Knobs>>(loadAll);
  const [sel, setSel] = useState<ColorName>("base");
  const [copied, setCopied] = useState("");

  useEffect(() => {
    try {
      localStorage.setItem(STORE, JSON.stringify(all));
    } catch {}
  }, [all]);

  const k = all[id] ?? baseKnobs(id);
  const flavor = flavorOf(id);
  const c = useMemo(() => derive(id, k), [id, k]);
  const rows = useMemo(() => report(c, flavor.dark), [c, flavor.dark]);
  const broken = rows.filter((r) => r.got < r.min);

  const set = (key: keyof Knobs, v: number) => setAll((p) => ({ ...p, [id]: { ...k, [key]: v } }));
  const trim = (role: string, field: keyof Trim, v: number) =>
    setAll((p) => ({
      ...p,
      [id]: { ...k, trims: { ...k.trims, [role]: { ...(k.trims[role] ?? ZERO), [field]: v } } },
    }));
  const reset = () => setAll((p) => ({ ...p, [id]: baseKnobs(id) }));

  /** Siblings of the flavor on screen, itself included. */
  const siblings = flavors.filter((f) => f.family === flavor.family).map((f) => f.id);
  const famName = families.find((f) => f.id === flavor.family)?.name ?? flavor.family;

  /**
   * Push one value sideways across the family.
   *
   * A family's three flavors share a hue and a chroma shape and differ only in
   * where they sit on the ladder, so a judgement about one of them is almost
   * always a judgement about all three — and re-dialling it twice by hand is
   * how they drift apart.
   */
  const syncKnob = (key: keyof Knobs) =>
    setAll((prev) => {
      const next = { ...prev };
      for (const sib of siblings) {
        const base = next[sib] ?? baseKnobs(sib);
        next[sib] = { ...base, [key]: k[key] };
      }
      return next;
    });
  const syncTrim = (role: string, field: keyof Trim) =>
    setAll((prev) => {
      const next = { ...prev };
      const v = (k.trims[role] ?? ZERO)[field];
      for (const sib of siblings) {
        const base = next[sib] ?? baseKnobs(sib);
        next[sib] = {
          ...base,
          trims: { ...base.trims, [role]: { ...(base.trims[role] ?? ZERO), [field]: v } },
        };
      }
      return next;
    });

  const block = `${flavor.id.toUpperCase()} = Flavor(
    id="${flavor.id}",
    family="${flavor.family}",
    name="${flavor.name}",
    slug="${flavor.slug}",
    dark=${flavor.dark ? "True" : "False"},
    blurb="${flavor.blurb}",
    colors={
${roles.map((r) => `        "${snake(r)}": "${c[r]}",`).join("\n")}
    },
    ansi_roles=${flavor.dark ? "DARK_ANSI" : "LIGHT_ANSI"},
)`;

  const copy = async (text: string, what: string) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopied(what);
      setTimeout(() => setCopied(""), 1600);
    } catch {}
  };

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
        <span {...stylex.props(s.sub)} style={{ color: c.subtext0 }}>
          {flavor.name}
        </span>
        <span {...stylex.props(s.verdict)} style={{ color: broken.length ? c.red : c.green }}>
          {broken.length
            ? `${broken.length} floor${broken.length > 1 ? "s" : ""} broken`
            : "all floors clear"}
        </span>
        <button
          type="button"
          onClick={() => copy(block, "block")}
          {...stylex.props(s.btn)}
          style={{ background: c.surface1, color: c.textHi, borderColor: c.surface2 }}
        >
          {copied === "block" ? "Copied" : "Copy flavor"}
        </button>
        <button
          type="button"
          onClick={() => copy(JSON.stringify(all, null, 2), "session")}
          {...stylex.props(s.btn)}
          style={{ background: "transparent", color: c.subtext0, borderColor: c.surface2 }}
        >
          {copied === "session" ? "Copied" : "Copy session"}
        </button>
      </header>

      <div {...stylex.props(s.body)}>
        {/* ── Left: every flavor, and which ones you've touched ─────────── */}
        <nav {...stylex.props(s.rail)} style={{ background: c.mantle, borderColor: c.surface1 }}>
          {families.map((fam) => (
            <div key={fam.id} {...stylex.props(s.famGroup)}>
              <h2 {...stylex.props(s.famName)} style={{ color: c.overlay1 }}>
                {fam.name}
              </h2>
              {flavors
                .filter((f) => f.family === fam.id)
                .map((f) => {
                  const on = f.id === id;
                  const edited = all[f.id] && !isDefault(f.id, all[f.id]);
                  const swatch = derive(f.id, all[f.id] ?? baseKnobs(f.id));
                  return (
                    <button
                      key={f.id}
                      type="button"
                      onClick={() => setId(f.id)}
                      {...stylex.props(s.flavorBtn)}
                      style={{
                        background: on ? c.surface1 : "transparent",
                        color: on ? c.textHi : c.subtext0,
                      }}
                    >
                      <span {...stylex.props(s.dots)}>
                        {(["base", "orange", "yellow", "green"] as ColorName[]).map((r) => (
                          <i key={r} {...stylex.props(s.dot)} style={{ background: swatch[r] }} />
                        ))}
                      </span>
                      <span {...stylex.props(s.flavorName)}>
                        {f.name.replace(`${fam.name} `, "")}
                      </span>
                      {edited ? (
                        <i {...stylex.props(s.edited)} style={{ background: c.yellow }} />
                      ) : null}
                    </button>
                  );
                })}
            </div>
          ))}
        </nav>

        {/* ── Middle: what the palette actually looks like ──────────────── */}
        <main {...stylex.props(s.preview)}>
          <div {...stylex.props(s.ramp)}>
            {([...ground, ...textRoles] as ColorName[]).map((r) => (
              <button
                key={r}
                type="button"
                title={`${r} ${c[r]}`}
                onClick={() => setSel(r)}
                {...stylex.props(s.rampCell, sel === r && s.rampOn)}
                style={{ background: c[r], borderColor: sel === r ? c.textHi : "transparent" }}
              />
            ))}
          </div>
          <div {...stylex.props(s.ramp)}>
            {accents.map((r) => (
              <button
                key={r}
                type="button"
                title={`${r} ${c[r]}`}
                onClick={() => setSel(r)}
                {...stylex.props(s.rampCell, sel === r && s.rampOn)}
                style={{ background: c[r], borderColor: sel === r ? c.textHi : "transparent" }}
              />
            ))}
          </div>

          <pre {...stylex.props(s.code)} style={{ background: c.base }}>
            {SAMPLE.map((line) => (
              <div key={line.map(([x]) => x).join("")}>
                {line.map(([text, role]) => (
                  <span key={text} style={{ color: c[role] }}>
                    {text}
                  </span>
                ))}
              </div>
            ))}
          </pre>

          <div {...stylex.props(s.stripe)} title={`stripe spread ${stripeSpread.toFixed(3)}`}>
            {STRIPE.map((r) => (
              <button
                key={r}
                type="button"
                onClick={() => setSel(r)}
                {...stylex.props(s.seg)}
                style={{ background: c[r], color: flavor.dark ? c.crust : c.base }}
              >
                {r}
              </button>
            ))}
          </div>
          <p {...stylex.props(s.hint)} style={{ color: stripeSpread > 0.05 ? c.red : c.subtext0 }}>
            stripe spread {stripeSpread.toFixed(3)} — Walnut sits at 0.045. Past about 0.05 these
            four stop reading as one ribbon in a prompt.
          </p>

          <div {...stylex.props(s.floors)}>
            {rows.map((r) => {
              const ok = r.got >= r.min;
              return (
                <button
                  key={r.label}
                  type="button"
                  onClick={() => setSel(r.roles[0] as ColorName)}
                  {...stylex.props(s.floor)}
                  style={{ color: ok ? c.subtext0 : c.red }}
                >
                  <span {...stylex.props(s.floorName)}>{r.label}</span>
                  <b style={{ color: ok ? c.text : c.red }}>{r.got.toFixed(2)}</b>
                  <span {...stylex.props(s.min)}>≥ {r.min}</span>
                </button>
              );
            })}
          </div>
        </main>

        {/* ── Right: the inspector ──────────────────────────────────────── */}
        <aside
          {...stylex.props(s.inspector)}
          style={{ background: c.mantle, borderColor: c.surface1 }}
        >
          <Section title="Ground" c={c}>
            <Slide
              id="gh"
              label="Hue"
              v={k.groundHue}
              min={0}
              max={360}
              step={0.5}
              unit="°"
              c={c}
              onChange={(v) => set("groundHue", v)}
              onSync={() => syncKnob("groundHue")}
              family={famName}
            />
            <Slide
              id="gc"
              label="Chroma"
              v={k.groundChroma}
              min={0}
              max={2.5}
              step={0.01}
              unit="×"
              c={c}
              onChange={(v) => set("groundChroma", v)}
              onSync={() => syncKnob("groundChroma")}
              family={famName}
            />
            <Slide
              id="gl"
              label="Lift"
              v={k.groundLift}
              min={-0.08}
              max={0.08}
              step={0.002}
              c={c}
              onChange={(v) => set("groundLift", v)}
              onSync={() => syncKnob("groundLift")}
              family={famName}
            />
          </Section>

          <Section title="Accent bands" c={c}>
            <Slide
              id="sc"
              label="Stripe"
              v={k.stripeChroma}
              min={0}
              max={2}
              step={0.01}
              unit="×"
              c={c}
              onChange={(v) => set("stripeChroma", v)}
              onSync={() => syncKnob("stripeChroma")}
              family={famName}
            />
            <Slide
              id="uc"
              label="Support"
              v={k.supportChroma}
              min={0}
              max={2}
              step={0.01}
              unit="×"
              c={c}
              onChange={(v) => set("supportChroma", v)}
              onSync={() => syncKnob("supportChroma")}
              family={famName}
            />
          </Section>

          <Roles
            c={c}
            sel={sel}
            setSel={setSel}
            trims={k.trims}
            trim={trim}
            rows={rows}
            syncTrim={syncTrim}
            family={famName}
          />

          <button
            type="button"
            onClick={reset}
            {...stylex.props(s.btn, s.wide)}
            style={{ background: "transparent", color: c.subtext0, borderColor: c.surface2 }}
          >
            Reset {flavor.name}
          </button>

          <textarea
            id="studio-out"
            readOnly
            value={block}
            {...stylex.props(s.out)}
            style={{ background: c.base, color: c.subtext1, borderColor: c.surface1 }}
          />
          <p {...stylex.props(s.hint)} style={{ color: c.subtext0 }}>
            Paste that over the flavor in <code>palette.py</code> and run <code>./build.py</code>.
            The studio never writes the file: the palette stays the one source of truth, and the
            change arrives as a diff you can read.
          </p>
        </aside>
      </div>
    </div>
  );
}

/**
 * Every role, one open at a time.
 *
 * A flat grid of 13 accents each with three sliders is 39 controls on screen
 * and none of them reachable — so the list stays a list, and opening a role is
 * what gives you its lightness, chroma and hue. Clicking a swatch or a failing
 * floor in the preview opens the same row, so there is one selection and three
 * ways to reach it.
 */
function Roles({
  c,
  sel,
  setSel,
  trims,
  trim,
  rows,
  syncTrim,
  family,
}: {
  c: Record<ColorName, string>;
  sel: ColorName;
  setSel: (r: ColorName) => void;
  trims: Record<string, Trim>;
  trim: (role: string, field: keyof Trim, v: number) => void;
  rows: { label: string; got: number; min: number; roles: string[] }[];
  syncTrim: (role: string, field: keyof Trim) => void;
  family: string;
}) {
  const groups: [string, ColorName[]][] = [
    ["Ground", ground as ColorName[]],
    ["Text", textRoles as ColorName[]],
    ["Accents", accents as ColorName[]],
  ];
  return (
    <section {...stylex.props(s.section)} style={{ borderColor: c.surface1 }}>
      <h2 {...stylex.props(s.sectionTitle)} style={{ color: c.textHi }}>
        Roles
      </h2>
      {groups.map(([title, list]) => (
        <div key={title} {...stylex.props(s.accGroup)}>
          <h3 {...stylex.props(s.accGroupName)} style={{ color: c.overlay1 }}>
            {title}
          </h3>
          {list.map((role) => {
            const open = sel === role;
            const t = trims[role] ?? ZERO;
            const lch = toLch(c[role]);
            const fails = rows.filter((r) => r.roles.includes(role) && r.got < r.min);
            return (
              <div key={role}>
                <button
                  type="button"
                  onClick={() => setSel(open ? ("" as ColorName) : role)}
                  aria-expanded={open}
                  {...stylex.props(s.accRow)}
                  style={{
                    background: open ? c.surface1 : "transparent",
                    color: open ? c.textHi : c.subtext0,
                  }}
                >
                  <i {...stylex.props(s.accSwatch)} style={{ background: c[role] }} />
                  <span {...stylex.props(s.accName)}>{role}</span>
                  {fails.length > 0 && (
                    <i {...stylex.props(s.accWarn)} style={{ background: c.red }} />
                  )}
                  <code
                    {...stylex.props(s.accHex)}
                    style={{ color: open ? c.subtext1 : c.overlay1 }}
                  >
                    {c[role]}
                  </code>
                </button>
                {open && (
                  <div {...stylex.props(s.accBody)} style={{ borderColor: c.surface1 }}>
                    <p {...stylex.props(s.lchLine)} style={{ color: c.overlay1 }}>
                      L {lch.L.toFixed(3)} · C {lch.C.toFixed(3)} · H {lch.h.toFixed(0)}°
                    </p>
                    <Slide
                      id={`${role}-l`}
                      label="Lightness"
                      v={t.dL}
                      min={-0.18}
                      max={0.18}
                      step={0.002}
                      c={c}
                      onChange={(v) => trim(role, "dL", v)}
                      onSync={() => syncTrim(role, "dL")}
                      family={family}
                    />
                    <Slide
                      id={`${role}-c`}
                      label="Chroma"
                      v={t.dC}
                      min={-0.12}
                      max={0.12}
                      step={0.002}
                      c={c}
                      onChange={(v) => trim(role, "dC", v)}
                      onSync={() => syncTrim(role, "dC")}
                      family={family}
                    />
                    <Slide
                      id={`${role}-h`}
                      label="Hue"
                      v={t.dh}
                      min={-60}
                      max={60}
                      step={0.5}
                      unit="°"
                      c={c}
                      onChange={(v) => trim(role, "dh", v)}
                      onSync={() => syncTrim(role, "dh")}
                      family={family}
                    />
                    {rows
                      .filter((r) => r.roles.includes(role))
                      .map((r) => (
                        <p
                          key={r.label}
                          {...stylex.props(s.lchLine)}
                          style={{ color: r.got >= r.min ? c.subtext0 : c.red }}
                        >
                          {r.label} — {r.got.toFixed(2)} / {r.min}
                        </p>
                      ))}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      ))}
    </section>
  );
}

function Section({
  title,
  c,
  children,
}: {
  title: string;
  c: Record<ColorName, string>;
  children: React.ReactNode;
}) {
  return (
    <section {...stylex.props(s.section)} style={{ borderColor: c.surface1 }}>
      <h2 {...stylex.props(s.sectionTitle)} style={{ color: c.textHi }}>
        {title}
      </h2>
      {children}
    </section>
  );
}

function Slide({
  id,
  label,
  v,
  min,
  max,
  step,
  unit,
  c,
  onChange,
  onSync,
  family,
}: {
  id: string;
  label: string;
  v: number;
  min: number;
  max: number;
  step: number;
  unit?: string;
  c: Record<ColorName, string>;
  onChange: (v: number) => void;
  /** Push this one value to every flavor in the family. */
  onSync?: () => void;
  family?: string;
}) {
  const [synced, setSynced] = useState(false);
  return (
    <div {...stylex.props(s.row)}>
      <label htmlFor={id} {...stylex.props(s.label)} style={{ color: c.subtext0 }}>
        {label}
      </label>
      <input
        id={id}
        type="range"
        value={v}
        min={min}
        max={max}
        step={step}
        onChange={(e) => onChange(Number(e.target.value))}
        {...stylex.props(s.range)}
        style={{ accentColor: c.yellow }}
      />
      <output {...stylex.props(s.value)} style={{ color: c.text }}>
        {v.toFixed(step < 0.01 ? 3 : 2)}
        {unit ?? ""}
      </output>
      {onSync ? (
        <button
          type="button"
          title={`Apply this ${label.toLowerCase()} to every flavor in ${family}`}
          aria-label={`Apply ${label} to every flavor in ${family}`}
          onClick={() => {
            onSync();
            setSynced(true);
            setTimeout(() => setSynced(false), 900);
          }}
          {...stylex.props(s.sync)}
          style={{ color: synced ? c.green : c.overlay1 }}
        >
          {synced ? "✓" : "⇉"}
        </button>
      ) : (
        <span {...stylex.props(s.sync)} />
      )}
    </div>
  );
}

const s = stylex.create({
  page: { minHeight: "100dvh", fontFamily: font.sans },
  bar: {
    display: "flex",
    flexWrap: "wrap",
    gap: space.s3,
    alignItems: "center",
    paddingBlock: space.s3,
    paddingInline: space.s4,
    borderBottomStyle: "solid",
    borderBottomWidth: 1,
  },
  title: { fontSize: font.sizeHead, fontWeight: 700, letterSpacing: font.trackHead },
  sub: { fontFamily: font.mono, fontSize: font.sizeMicro },
  verdict: { marginLeft: "auto", fontFamily: font.mono, fontSize: font.sizeMicro },
  btn: {
    paddingBlock: 7,
    paddingInline: 12,
    fontFamily: font.sans,
    fontSize: font.sizeMicro,
    fontWeight: 600,
    cursor: "pointer",
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "var(--radius-pill)",
  },
  wide: { width: "100%" },
  body: {
    display: "grid",
    gridTemplateColumns: {
      default: "minmax(0,1fr)",
      "@media (min-width: 1100px)": "208px minmax(0,1fr) 340px",
    },
    alignItems: "stretch",
    minHeight: "calc(100dvh - 58px)",
  },
  rail: {
    display: "grid",
    gap: space.s4,
    alignContent: "start",
    padding: space.s3,
    borderRightStyle: "solid",
    borderRightWidth: 1,
  },
  famGroup: { display: "grid", gap: 2 },
  famName: {
    paddingInline: 6,
    paddingBottom: 4,
    margin: 0,
    fontSize: 10,
    fontWeight: 700,
    textTransform: "uppercase",
    letterSpacing: font.trackLabel,
  },
  flavorBtn: {
    display: "flex",
    gap: 8,
    alignItems: "center",
    width: "100%",
    paddingBlock: 7,
    paddingInline: 6,
    fontFamily: font.sans,
    fontSize: font.sizeMicro,
    fontWeight: 600,
    textAlign: "left",
    cursor: "pointer",
    borderWidth: 0,
    borderRadius: "var(--radius-pill)",
  },
  dots: { display: "flex", flexShrink: 0, gap: 2 },
  dot: { width: 8, height: 8, borderRadius: "var(--radius-chip)" },
  flavorName: { overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" },
  edited: { flexShrink: 0, width: 5, height: 5, marginLeft: "auto", borderRadius: "50%" },
  preview: { display: "grid", gap: space.s3, alignContent: "start", padding: space.s4 },
  ramp: { display: "flex", gap: 2 },
  rampCell: {
    flexGrow: "1",
    flexShrink: "1",
    flexBasis: "0",
    minWidth: 0,
    height: 40,
    padding: 0,
    cursor: "pointer",
    borderStyle: "solid",
    borderWidth: 2,
  },
  rampOn: { height: 46 },
  code: {
    padding: space.s4,
    margin: 0,
    overflowX: "auto",
    fontFamily: font.mono,
    fontSize: 13,
    lineHeight: 1.75,
  },
  stripe: { display: "flex" },
  seg: {
    flexGrow: "1",
    flexShrink: "1",
    flexBasis: "0",
    padding: 9,
    fontFamily: font.mono,
    fontSize: 11,
    fontWeight: 700,
    cursor: "pointer",
    borderWidth: 0,
  },
  floors: { display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(214px, 1fr))", gap: 2 },
  floor: {
    display: "grid",
    gridTemplateColumns: "minmax(0,1fr) 44px 40px",
    gap: 6,
    padding: 4,
    fontFamily: font.mono,
    fontSize: 11,
    textAlign: "left",
    cursor: "pointer",
    backgroundColor: "transparent",
    borderWidth: 0,
  },
  floorName: { overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" },
  min: { opacity: 0.55 },
  inspector: {
    display: "grid",
    gap: space.s3,
    alignContent: "start",
    padding: space.s3,
    borderLeftStyle: "solid",
    borderLeftWidth: 1,
  },
  section: { display: "grid", gap: 6, padding: space.s3, borderStyle: "solid", borderWidth: 1 },
  sectionTitle: { margin: 0, fontFamily: font.mono, fontSize: 11, fontWeight: 700 },
  row: {
    display: "grid",
    gridTemplateColumns: "58px minmax(0,1fr) 52px 18px",
    gap: 7,
    alignItems: "center",
  },
  // Push one value sideways to the rest of the family.
  sync: {
    width: 18,
    height: 18,
    padding: 0,
    fontSize: 11,
    lineHeight: 1,
    cursor: "pointer",
    borderWidth: 0,
    backgroundColor: "transparent",
  },
  label: { fontSize: font.sizeMicro },
  range: { width: "100%" },
  value: { fontFamily: font.mono, fontSize: 11, textAlign: "right" },
  accGroup: { display: "grid", gap: 1, marginTop: 4 },
  accGroupName: {
    paddingBlock: 4,
    margin: 0,
    fontSize: 9.5,
    fontWeight: 700,
    textTransform: "uppercase",
    letterSpacing: font.trackLabel,
  },
  accRow: {
    display: "flex",
    gap: 7,
    alignItems: "center",
    width: "100%",
    paddingBlock: 5,
    paddingInline: 5,
    fontFamily: font.mono,
    fontSize: 10.5,
    textAlign: "left",
    cursor: "pointer",
    borderWidth: 0,
    borderRadius: 3,
  },
  accSwatch: { flexShrink: 0, width: 11, height: 11, borderRadius: "var(--radius-chip)" },
  accName: { overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" },
  accWarn: { flexShrink: 0, width: 5, height: 5, borderRadius: "50%" },
  accHex: { flexShrink: 0, marginLeft: "auto" },
  accBody: {
    display: "grid",
    gap: 5,
    paddingBlock: 8,
    paddingInline: 6,
    marginBottom: 4,
    borderLeftStyle: "solid",
    borderLeftWidth: 2,
  },
  lchLine: { margin: 0, fontFamily: font.mono, fontSize: 10, lineHeight: 1.4 },
  out: {
    width: "100%",
    minHeight: 200,
    padding: space.s3,
    fontFamily: font.mono,
    fontSize: 11,
    lineHeight: 1.5,
    resize: "vertical",
    borderStyle: "solid",
    borderWidth: 1,
  },
  hint: { margin: 0, fontSize: 11, lineHeight: 1.5 },
});
