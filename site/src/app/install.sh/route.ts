import { existsSync, readFileSync } from "node:fs";
import path from "node:path";

// Serves the repo's install.sh at /install.sh, so the one-liner is
// `curl -fsSL https://oddurs.github.io/subway-seat/install.sh | sh`.
export const dynamic = "force-static";

const SCRIPT = path.join(process.cwd(), "..", "install.sh");

const STUB = `#!/bin/sh
# Subway Seat's installer isn't in this build yet.
echo "Subway Seat: the installer isn't published yet." >&2
echo "Clone https://github.com/oddurs/subway-seat and follow the README for now." >&2
exit 1
`;

export function GET() {
  const body = existsSync(SCRIPT) ? readFileSync(SCRIPT, "utf8") : STUB;
  return new Response(body, {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
}
