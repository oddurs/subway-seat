import * as stylex from "@stylexjs/stylex";
import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { ClaudeSpotlight } from "@/components/ClaudeSpotlight";
import { FlavorCards } from "@/components/FlavorCards";
import { HerdrDemo } from "@/components/HerdrDemo";
import { TerminalDemo } from "@/components/TerminalDemo";
import { Workbench } from "@/components/Workbench";
import { flavors } from "@/lib/palette";
import { color } from "@/theme/tokens.stylex";

// Press-kit frames: one demo on a plain ground, for README and store screenshots.
// Add ?flavor=tunnel|enamel to pick the flavor.
const SHOTS = {
  vscode: () => <Workbench />,
  terminal: () => <TerminalDemo />,
  herdr: () => <HerdrDemo />,
  claude: () => <ClaudeSpotlight />,
  flavors: () => <FlavorCards flavors={flavors} />,
};

export const dynamicParams = false;
export const metadata: Metadata = { robots: { index: false } };

export function generateStaticParams() {
  return Object.keys(SHOTS).map((name) => ({ name }));
}

export default async function Shot({ params }: PageProps<"/shot/[name]">) {
  const { name } = await params;
  const render = SHOTS[name as keyof typeof SHOTS];
  if (!render) notFound();
  return <main {...stylex.props(styles.frame)}>{render()}</main>;
}

const styles = stylex.create({
  frame: {
    maxWidth: 1240,
    minHeight: "100vh",
    padding: 48,
    marginInline: "auto",
    backgroundColor: color.mantle,
  },
});
