import * as stylex from "@stylexjs/stylex";
import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { ReactNode } from "react";
import { action } from "@/components/action";
import { CodeBlock } from "@/components/CodeBlock";
import { CopyButton } from "@/components/CopyButton";
import { Footer } from "@/components/Footer";
import { Nav } from "@/components/Nav";
import { BASE } from "@/lib/base";
import { readDist } from "@/lib/dist";
import { type PortFile, portById, ports } from "@/lib/manifest";
import { flavors } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";
import { font } from "@/theme/type.stylex";

export const dynamicParams = false;

export function generateStaticParams() {
  return ports().map((p) => ({ id: p.id }));
}

export async function generateMetadata({ params }: PageProps<"/ports/[id]">): Promise<Metadata> {
  const { id } = await params;
  const port = portById(id);
  return port ? { title: port.name, description: port.notes } : {};
}

/** `inline code` in notes → <code>. */
function prose(text: string): ReactNode[] {
  return text.split(/(`[^`]+`)/).map((part, i) =>
    part.startsWith("`") ? (
      // biome-ignore lint/suspicious/noArrayIndexKey: static text segments
      <code key={i} {...stylex.props(styles.inline)}>
        {part.slice(1, -1)}
      </code>
    ) : (
      part
    ),
  );
}

async function File({ file }: { file: PortFile }) {
  const name = file.path.split("/").slice(1).join("/");
  const code = file.binary ? null : readDist(file.path);
  return (
    <div {...stylex.props(styles.file)}>
      <div {...stylex.props(styles.fileHead)}>
        <div {...stylex.props(styles.fileMeta)}>
          <code {...stylex.props(styles.fileName)}>{name}</code>
          {file.dest && (
            <span {...stylex.props(styles.dest)}>
              {file.append ? "append to " : file.binary ? "" : "save as "}
              <code {...stylex.props(styles.path)}>{file.dest}</code>
            </span>
          )}
        </div>
        <div {...stylex.props(styles.actions)}>
          {code !== null && <CopyButton text={code} />}
          <a
            href={`${BASE}/files/${file.path.split("/").map(encodeURIComponent).join("/")}`}
            download
            {...stylex.props(action.base)}
          >
            Download
          </a>
        </div>
      </div>
      {code !== null && (
        <CodeBlock code={code} lang={file.lang} scroll={code.split("\n").length > 28} />
      )}
    </div>
  );
}

export default async function PortPage({ params }: PageProps<"/ports/[id]">) {
  const { id } = await params;
  const port = portById(id);
  if (!port) notFound();

  const shared = port.files.filter((f) => f.flavor === null);
  return (
    <>
      <Nav />
      <main {...stylex.props(styles.main)}>
        <Link href="/#ports" {...stylex.props(styles.back)}>
          ← All ports
        </Link>
        <header {...stylex.props(styles.head)}>
          <p {...stylex.props(styles.category)}>{port.category}</p>
          <h1 {...stylex.props(styles.title)}>{port.name}</h1>
          <p {...stylex.props(styles.notes)}>{prose(port.notes)}</p>
          <p {...stylex.props(styles.flavorNote)}>
            Showing{" "}
            {flavors.map((f) => (
              <b key={f.id} data-only={f.id}>
                {f.name}
              </b>
            ))}
            . Switch flavors with the bullets up top.{" "}
            <a href={port.homepage} {...stylex.props(styles.homepage)}>
              {port.name} ↗
            </a>
          </p>
        </header>

        {port.enable && (
          <section {...stylex.props(styles.block)}>
            <h2 {...stylex.props(styles.h2)}>Turn it on</h2>
            {flavors.map((f) => {
              const enable = port.enable?.[f.id];
              return enable ? (
                <div key={f.id} data-only={f.id} {...stylex.props(styles.enable)}>
                  <span {...stylex.props(styles.where)}>In {prose(enable.where)}</span>
                  <CodeBlock code={enable.code} lang={enable.lang} />
                </div>
              ) : null;
            })}
          </section>
        )}

        <section {...stylex.props(styles.block)}>
          <h2 {...stylex.props(styles.h2)}>The files</h2>
          {flavors.map((f) => {
            const own = port.files.filter((file) => file.flavor === f.id);
            return own.length ? (
              <div key={f.id} data-only={f.id} {...stylex.props(styles.files)}>
                {own.map((file) => (
                  <File key={file.path} file={file} />
                ))}
              </div>
            ) : null;
          })}
          {shared.length > 0 && (
            <div {...stylex.props(styles.files)}>
              {shared.map((file) => (
                <File key={file.path} file={file} />
              ))}
            </div>
          )}
        </section>
      </main>
      <Footer />
    </>
  );
}

const styles = stylex.create({
  main: {
    display: "grid",
    gridTemplateColumns: "minmax(0, 1fr)",
    gap: 40,
    maxWidth: 1000,
    paddingInline: 24,
    paddingTop: 40,
    marginInline: "auto",
  },
  back: {
    fontSize: 14,
    color: {
      default: color.subtext0,
      ":hover": color.orange,
    },
    textDecoration: "none",
  },
  head: { display: "grid", gap: 12 },
  category: {
    fontSize: 13,
    fontWeight: 600,
    color: color.orange,
    textTransform: "uppercase",
    letterSpacing: "0.16em",
  },
  title: {
    fontFamily: font.display,
    fontSize: "clamp(40px, 6vw, 72px)",
    fontVariationSettings: '"SOFT" 100, "WONK" 1',
    fontWeight: 800,
    lineHeight: 1,
    color: color.textHi,
  },
  notes: {
    maxWidth: "64ch",
    fontSize: 18,
    lineHeight: 1.6,
    color: color.subtext1,
    textWrap: "pretty",
  },
  flavorNote: { fontSize: 14, color: color.overlay1 },
  homepage: {
    color: {
      default: color.subtext0,
      ":hover": color.orange,
    },
  },
  inline: { fontFamily: font.mono, fontSize: "0.88em", color: color.yellow },
  block: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 16 },
  h2: {
    fontFamily: font.display,
    fontSize: 28,
    fontVariationSettings: '"SOFT" 100',
    fontWeight: 700,
    color: color.textHi,
  },
  enable: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 8 },
  where: { fontSize: 14, color: color.subtext0 },
  files: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 26 },
  file: { display: "grid", gridTemplateColumns: "minmax(0, 1fr)", gap: 8 },
  fileHead: {
    display: "flex",
    flexWrap: "wrap",
    gap: 10,
    alignItems: "flex-end",
    justifyContent: "space-between",
  },
  fileMeta: { display: "grid", gap: 2, minWidth: 0 },
  fileName: { fontFamily: font.mono, fontSize: 14, color: color.yellow },
  dest: { fontSize: 13, color: color.overlay1 },
  path: { fontFamily: font.mono, fontSize: 12.5, color: color.subtext1, overflowWrap: "anywhere" },
  actions: { display: "flex", gap: 6 },
});
