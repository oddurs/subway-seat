import { readFileSync } from "node:fs";
import path from "node:path";
import { ImageResponse } from "next/og";
import sharp from "sharp";
import { walnut } from "@/lib/palette";

// Share images in the station-sign style: a black sign band, a big Fraunces
// title, the supergraphic stripes and a strip of shag. Walnut, like the site's default.
// The fonts are ASCII subsets of Arimo 700 and Fraunces 800 (SOFT 100, WONK 1)
// from Google Fonts, under the SIL Open Font License (OFL-*.txt here).

export const OG_SIZE = { width: 1200, height: 630 };

const dir = path.join(process.cwd(), "src", "og");
const fonts = [
  { name: "Sign", data: readFileSync(path.join(dir, "arimo-700.ttf")), weight: 700 as const },
  { name: "Display", data: readFileSync(path.join(dir, "fraunces-800.ttf")), weight: 800 as const },
];
const shag = `data:image/jpeg;base64,${readFileSync(path.join(dir, "shag.jpg")).toString("base64")}`;

const c = walnut.colors;
const SIGN = "#0C0805";
const SIGN_TEXT = "#F8ECD4";

function stripes() {
  const colors = [c.red, c.orange, c.yellow, c.green, c.text];
  const W = 30;
  const paths = colors
    .map((stroke, i) => {
      const r = 60 + i * W;
      return `<path d="M ${420 - r} -20 L ${420 - r} 150 A ${r} ${r} 0 0 0 420 ${150 + r} L 700 ${150 + r}" fill="none" stroke="${stroke}" stroke-width="${W + 0.5}"/>`;
    })
    .join("");
  return `data:image/svg+xml;utf8,${encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 420">${paths}</svg>`)}`;
}

const BULLETS: [string, string][] = [
  ["K", c.orange],
  ["F", c.yellow],
  ["S", c.green],
  ["T", c.sage],
  ["N", c.redHi],
];

/**
 * `rug` adds the strip of shag (a photo, so only the home card has it); the rest
 * end on the five stripes. The PNG is quantized to a palette, which keeps the
 * type crisp at a fraction of the size.
 */
export async function ogCard({
  kicker,
  title,
  line,
  rug = false,
}: {
  kicker: string;
  title: string;
  line: string;
  rug?: boolean;
}) {
  const size = title.length > 22 ? 76 : title.length > 14 ? 96 : 124;
  const image = new ImageResponse(
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        position: "relative",
        backgroundColor: c.mantle,
        fontFamily: "Sign",
      }}
    >
      {/* eslint-disable-next-line @next/next/no-img-element -- satori draws plain img */}
      <img
        src={stripes()}
        alt=""
        width={560}
        height={380}
        style={{ position: "absolute", top: 30, right: -40 }}
      />
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          height: 78,
          paddingLeft: 64,
          paddingRight: 64,
          backgroundColor: SIGN,
          borderTop: `8px solid ${SIGN}`,
          boxShadow: `inset 0 2px 0 ${SIGN_TEXT}`,
        }}
      >
        <div style={{ display: "flex", fontSize: 32, color: SIGN_TEXT, letterSpacing: -0.3 }}>
          Subway Seat
        </div>
        <div style={{ display: "flex", gap: 10 }}>
          {BULLETS.map(([letter, bg]) => (
            <div
              key={letter}
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                width: 40,
                height: 40,
                borderRadius: 20,
                backgroundColor: bg,
                color: c.crust,
                fontSize: 22,
              }}
            >
              {letter}
            </div>
          ))}
        </div>
      </div>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          flexGrow: 1,
          justifyContent: "center",
          paddingLeft: 64,
          paddingRight: 360,
        }}
      >
        <div
          style={{
            display: "flex",
            fontSize: 22,
            color: c.orange,
            letterSpacing: 3.5,
            textTransform: "uppercase",
          }}
        >
          {kicker}
        </div>
        <div
          style={{
            display: "flex",
            marginTop: 14,
            fontFamily: "Display",
            fontSize: size,
            lineHeight: 1,
            color: c.textHi,
            letterSpacing: -1.5,
          }}
        >
          {title}
        </div>
        <div
          style={{
            display: "flex",
            marginTop: 26,
            fontSize: 28,
            lineHeight: 1.35,
            color: c.subtext1,
          }}
        >
          {line}
        </div>
      </div>
      {rug ? (
        // eslint-disable-next-line @next/next/no-img-element -- satori draws plain img
        <img src={shag} alt="" width={1200} height={90} />
      ) : (
        <div style={{ display: "flex", height: 18 }}>
          {[c.red, c.orange, c.yellow, c.green, c.text].map((bg) => (
            <div key={bg} style={{ display: "flex", flexGrow: 1, backgroundColor: bg }} />
          ))}
        </div>
      )}
    </div>,
    { ...OG_SIZE, fonts },
  );
  const png = await sharp(Buffer.from(await image.arrayBuffer()))
    .png({ palette: true, quality: 90, effort: 10, compressionLevel: 9 })
    .toBuffer();
  return new Response(new Uint8Array(png), { headers: { "Content-Type": "image/png" } });
}
