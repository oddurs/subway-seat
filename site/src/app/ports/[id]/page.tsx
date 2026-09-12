import * as stylex from "@stylexjs/stylex";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { ReactNode } from "react";
import { action } from "@/components/action";
import { CodeBlock } from "@/components/CodeBlock";
import { Command } from "@/components/Command";
import { CopyButton } from "@/components/CopyButton";
import { Footer } from "@/components/Footer";
import { Nav } from "@/components/Nav";
import { ShellTabs } from "@/components/ShellTabs";
import { BASE } from "@/lib/base";
import { bundleFor } from "@/lib/bundles";
import { readDist } from "@/lib/dist";
import { installCommand } from "@/lib/install";
import {
  categoryLabel,
  distExists,
  isPath,
  type PortFile,
  portById,
  ports,
  setupFor,
} from "@/lib/manifest";
import { type FlavorId, flavorById, flavors, roleNames, roles, shortName } from "@/lib/palette";
import { pageMeta, REPO, summary } from "@/lib/seo";
import { ink } from "@/theme/ink.stylex";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

export const dynamicParams = false;

export function generateStaticParams() {
  return ports().map((p) => ({ id: p.id }));
}

export async function generateMetadata({ params }: PageProps<"/ports/[id]">): Promise<Metadata> {
  const { id } = await params;
  const port = portById(id);
  if (!port) return {};
  const title = `Subway Seat for ${port.name}`;
  const lead = `${title}: a warm 1970s subway-car theme in three flavors.`;
  const description = `${lead} ${summary(port.notes, 155 - lead.length - 1)}`.trim();
  return {
    title: { absolute: title },
    ...pageMeta(`/ports/${port.id}`, title, description, {
      name: `${port.id}.png`,
      alt: `${title}: a warm 1970s subway-car theme in three flavors.`,
    }),
  };
}

const IMAGE = /\.(png|svg|jpe?g|webp)$/i;
const fileUrl = (p: string) => `${BASE}/files/${p.split("/").map(encodeURIComponent).join("/")}`;
const codeUrl = (p: string) => `${BASE}/code/${p.split("/").map(encodeURIComponent).join("/")}`;

/** `inline code` in notes → <code>; short ones don't break across lines. */
function prose(text: string): ReactNode[] {
  return text.split(/(`[^`]+`)/).map((part, i) =>
    part.startsWith("`") ? (
      // biome-ignore lint/suspicious/noArrayIndexKey: static text segments
      <code key={i} {...stylex.props(styles.inline, part.length < 32 && styles.nowrap)}>
        {part.slice(1, -1)}
      </code>
    ) : (
      part
    ),
  );
}

/** Where a file goes: a path to save or append to, and any step in words. */
function Destination({ file }: { file: PortFile }) {
  const path = file.dest && isPath(file.dest) ? file.dest : null;
  const legacy = file.dest && !path ? file.dest : null; // older manifests put steps in dest
  const how = file.how ?? legacy;
  if (!path && !how) return null;
  return (
    <span {...stylex.props(styles.dest)}>
      {path && (
        <>
          {file.append ? "add to the end of " : "save as "}
          <code {...stylex.props(styles.path)}>{path}</code>
        </>
      )}
      {path && how && <br />}
      {how && <span>{prose(how)}</span>}
    </span>
  );
}

/**
 * What's inside a file the page can't show as text (a swatch book, a
 * Terminal.app profile): the flavor's colors, ANSI order for terminals.
 */
function Inside({ flavor, terminal }: { flavor: FlavorId; terminal: boolean }) {
  const f = flavorById[flavor];
  const list = terminal ? f.ansi : roles;
  return (
    <div
      role="img"
      aria-label={`The ${shortName(flavor)} colors inside`}
      {...stylex.props(styles.inside)}
    >
      {list.map((role, i) => (
        <span
          // biome-ignore lint/suspicious/noArrayIndexKey: ANSI slots repeat roles
          key={i}
          title={`${terminal ? `${i} ` : ""}${roleNames[role] ?? role} ${f.colors[role]}`}
          {...stylex.props(styles.insideChip, styles.fill(f.colors[role]))}
        />
      ))}
    </div>
  );
}

async function File({ file, terminal }: { file: PortFile; terminal: boolean }) {
  const name = file.path.split("/").slice(1).join("/");
  const image = IMAGE.test(file.path) && distExists(file.path);
  const code = file.binary || image ? null : readDist(file.path);
  return (
    <div {...stylex.props(styles.file)}>
      <div {...stylex.props(styles.fileHead)}>
        <div {...stylex.props(styles.fileMeta)}>
          <code {...stylex.props(styles.fileName)}>{name}</code>
          <Destination file={file} />
        </div>
        <div {...stylex.props(styles.actions)}>
          {code !== null && <CopyButton src={fileUrl(file.path)} name={name} />}
          <a
            href={fileUrl(file.path)}
            download
            aria-label={`Download ${name}`}
            {...stylex.props(action.base)}
          >
            Download
          </a>
        </div>
      </div>
      {image && (
        // eslint-disable-next-line @next/next/no-img-element -- static export; the file is its own preview
        <img
          src={fileUrl(file.path)}
          alt={`Preview of ${name}`}
          loading="lazy"
          {...stylex.props(styles.preview)}
        />
      )}
      {file.binary && !image && file.flavor && <Inside flavor={file.flavor} terminal={terminal} />}
      {code !== null && (
        <CodeBlock
          code={code}
          lang={file.lang}
          flavor={file.flavor ?? undefined}
          scroll={code.split("\n").length > 28}
          full={codeUrl(file.path)}
          label={name}
        />
      )}
    </div>
  );
}

export default async function PortPage({ params }: PageProps<"/ports/[id]">) {
  const { id } = await params;
  const port = portById(id);
  if (!port) notFound();

  const shared = port.files.filter((f) => f.flavor === null);
  const perFlavor = port.files.some((f) => f.flavor !== null);
  const setup = setupFor(port);
  const issue = (f: FlavorId) =>
    `${REPO}/issues/new?${new URLSearchParams({
      template: "bug-report.yml",
      title: `[${port.id}] `,
      port: `${port.name}, ${flavors.find((x) => x.id === f)?.name ?? f}`,
    })}`;

  return (
    <>
      <Nav />
      <main id="main" {...stylex.props(styles.main)}>
        <div {...stylex.props(styles.column)}>
          <Link href="/#ports" {...stylex.props(styles.back)}>
            ← All ports
          </Link>
          <header {...stylex.props(styles.head)}>
            <p {...stylex.props(styles.kicker)}>
              <span {...stylex.props(styles.category)}>{categoryLabel(port.category)}</span>
              {port.requires && <span {...stylex.props(styles.badge)}>Needs {port.requires}</span>}
            </p>
            <h1 {...stylex.props(styles.title)}>{port.name}</h1>
            <p {...stylex.props(styles.notes)}>{prose(port.notes)}</p>
            <p {...stylex.props(styles.flavorNote)}>
              Showing{" "}
              {flavors.map((f) => (
                <b key={f.id} data-only={f.id}>
                  {shortName(f.id)}
                </b>
              ))}
              . Switch flavors with the bullets up top.
            </p>
            <p {...stylex.props(styles.links)}>
              <a href={port.homepage} {...stylex.props(styles.link)}>
                {port.name} <span aria-hidden>↗</span>
              </a>
              {flavors.map((f) => (
                <a key={f.id} data-only={f.id} href={issue(f.id)} {...stylex.props(styles.link)}>
                  Report a problem with this port
                </a>
              ))}
            </p>
          </header>

          {setup !== "manual" && (
            <section aria-labelledby="quick" {...stylex.props(styles.block)}>
              <h2 id="quick" {...stylex.props(styles.h2)}>
                The quick way
              </h2>
              <p {...stylex.props(styles.lede)}>
                The installer links the files{" "}
                {setup === "auto"
                  ? "and switches the theme on for you."
                  : "for you, then tells you the one thing it can't do."}{" "}
                <Link href="/install" {...stylex.props(styles.link)}>
                  More ways to install
                </Link>
              </p>
              {flavors.map((f) => (
                <div key={f.id} data-only={f.id}>
                  <Command text={installCommand({ flavor: f.id, only: [port.id] })} />
                </div>
              ))}
            </section>
          )}

          {port.enable && (
            <section aria-labelledby="enable" {...stylex.props(styles.block)}>
              <h2 id="enable" {...stylex.props(styles.h2)}>
                Turn it on
              </h2>
              {flavors.map((f) => {
                const enable = port.enable?.[f.id];
                if (!enable) return null;
                const fishBlock = <CodeBlock code={enable.code} lang={enable.lang} copy />;
                return (
                  <div key={f.id} data-only={f.id} {...stylex.props(styles.enable)}>
                    <span {...stylex.props(styles.where)}>In {prose(enable.where)}</span>
                    {enable.sh ? (
                      <ShellTabs
                        fish={fishBlock}
                        sh={<CodeBlock code={enable.sh} lang="sh" copy />}
                      />
                    ) : (
                      fishBlock
                    )}
                  </div>
                );
              })}
            </section>
          )}

          {port.auto && (
            <section aria-labelledby="auto" {...stylex.props(styles.block)}>
              <h2 id="auto" {...stylex.props(styles.h2)}>
                Follow light and dark
              </h2>
              <p {...stylex.props(styles.lede)}>
                One setting that changes with your system’s light and dark mode, no switching by
                hand.
              </p>
              <div {...stylex.props(styles.enable)}>
                <span {...stylex.props(styles.where)}>In {prose(port.auto.where)}</span>
                <CodeBlock code={port.auto.code} lang={port.auto.lang} copy />
              </div>
            </section>
          )}

          <section aria-labelledby="files" {...stylex.props(styles.block)}>
            <div {...stylex.props(styles.filesHead)}>
              <h2 id="files" {...stylex.props(styles.h2)}>
                The files
              </h2>
              {flavors.map((f) => {
                const zip = bundleFor(port, f.id);
                return zip ? (
                  <a
                    key={f.id}
                    data-only={f.id}
                    href={`${BASE}/zip/${zip}`}
                    download
                    {...stylex.props(action.base)}
                  >
                    Download all (.zip)
                  </a>
                ) : null;
              })}
            </div>
            {flavors.map((f) => {
              const own = port.files.filter((file) => file.flavor === f.id);
              return own.length ? (
                <div key={f.id} data-only={f.id} {...stylex.props(styles.files)}>
                  {own.map((file) => (
                    <File key={file.path} file={file} terminal={port.category === "Terminals"} />
                  ))}
                </div>
              ) : null;
            })}
            {shared.length > 0 && (
              <div {...stylex.props(styles.files)}>
                <p {...stylex.props(styles.sharedNote)}>
                  {perFlavor
                    ? shared.length === 1
                      ? "This one is shared by all three flavors."
                      : "These are shared by all three flavors."
                    : shared.length === 1
                      ? "One file covers all three flavors."
                      : "One set of files covers all three flavors."}
                </p>
                {shared.map((file) => (
                  <File key={file.path} file={file} terminal={port.category === "Terminals"} />
                ))}
              </div>
            )}
          </section>
        </div>
      </main>
      <Footer />
    </>
  );
}

const styles = stylex.create({
  main: { maxWidth: 1200, paddingInline: 24, paddingTop: 40, marginInline: "auto" },
  column: {
    display: "grid",
    gridTemplateColumns: "minmax(0, 1fr)",
    gap: 44,
    maxWidth: 1000,
  },
  back: {
    justifySelf: "start",
    paddingBlock: 4,
    fontSize: 14,
    color: {
      default: color.subtext0,
      ":hover": ink.accent,
    },
    textDecoration: "none",
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 2,
    borderRadius: 2,
  },
  head: { display: "grid", gap: 12, marginTop: -16 },
  kicker: { display: "flex", flexWrap: "wrap", gap: 12, alignItems: "center" },
  category: {
    fontSize: 13,
    fontWeight: 600,
    color: ink.accent,
    textTransform: "uppercase",
    letterSpacing: "0.16em",
  },
  badge: {
    paddingBlock: 2,
    paddingInline: 10,
    fontSize: 12.5,
    color: color.subtext1,
    borderColor: color.surface2,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: 999,
  },
  title: {
    fontFamily: font.display,
    fontSize: "clamp(40px, 6vw, 72px)",
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 800,
    lineHeight: 1,
    color: color.textHi,
    overflowWrap: "anywhere",
  },
  notes: {
    maxWidth: "64ch",
    fontSize: 18,
    lineHeight: 1.6,
    color: color.subtext1,
    textWrap: "pretty",
  },
  flavorNote: { fontSize: 14, color: color.subtext0 },
  links: { display: "flex", flexWrap: "wrap", rowGap: 4, columnGap: 20, fontSize: 14 },
  link: {
    color: {
      default: color.subtext0,
      ":hover": ink.accent,
    },
    textUnderlineOffset: 3,
    outlineWidth: 2,
    outlineStyle: {
      default: "none",
      ":focus-visible": "solid",
    },
    outlineColor: ink.accent,
    outlineOffset: 2,
    borderRadius: 2,
  },
  inline: { fontFamily: font.mono, fontSize: "0.88em", color: ink.code },
  nowrap: { whiteSpace: "nowrap" },
  block: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 16 },
  lede: { maxWidth: "72ch", fontSize: 15, color: color.subtext0, textWrap: "pretty" },
  h2: {
    fontFamily: font.display,
    fontSize: 28,
    fontVariationSettings: '"SOFT" 100',
    fontWeight: 700,
    lineHeight: 1.2,
    color: color.textHi,
  },
  enable: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 8 },
  where: { fontSize: 14, color: color.subtext0 },
  filesHead: {
    display: "flex",
    flexWrap: "wrap",
    gap: 12,
    alignItems: "center",
    justifyContent: "space-between",
  },
  files: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 26 },
  sharedNote: { marginTop: 6, fontSize: 14, color: color.subtext0 },
  file: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 8 },
  fileHead: {
    display: "flex",
    flexWrap: "wrap",
    gap: 10,
    alignItems: "flex-end",
    justifyContent: "space-between",
  },
  fileMeta: { display: "grid", gap: 2, minWidth: 0 },
  fileName: { fontFamily: font.mono, fontSize: 14, color: ink.code, overflowWrap: "anywhere" },
  dest: { fontSize: 13, color: color.subtext0 },
  path: { fontFamily: font.mono, fontSize: 12.5, color: color.subtext1, overflowWrap: "anywhere" },
  actions: { display: "flex", gap: 6 },
  inside: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(26px, 1fr))",
    gap: 4,
    padding: 10,
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "var(--radius-card)",
  },
  insideChip: {
    height: 26,
    borderRadius: "var(--radius-card)",
    boxShadow: `inset 0 0 0 1px color-mix(in srgb, ${color.text} 12%, transparent)`,
  },
  fill: (bg: string) => ({ backgroundColor: bg }),
  preview: {
    width: "100%",
    maxWidth: 720,
    height: "auto",
    backgroundColor: color.base,
    borderColor: color.surface0,
    borderStyle: "solid",
    borderWidth: 1,
    borderRadius: "var(--radius-card)",
  },
});
