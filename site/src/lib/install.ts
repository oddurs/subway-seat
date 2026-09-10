// The commands and config for install.sh. Its interface (fixed by the installer):
//   sh install.sh [install|switch <flavor>|status|uninstall|list] [options]
//   --flavor walnut|tunnel|enamel|auto  --only id,id  --skip id,id  --all
//   --yes  --dry-run  --copy  --no-enable
//   config file ~/.config/subway-seat/config: flavor=… / only=… / skip=…

export const INSTALL_URL = "https://oddurs.github.io/subway-seat/install.sh";
export const CLONE = "git clone https://github.com/oddurs/subway-seat && cd subway-seat";
export const CONFIG_PATH = "~/.config/subway-seat/config";

export type InstallFlavor = "walnut" | "tunnel" | "enamel" | "auto";
export type Extra = "copy" | "no-enable" | "dry-run" | "yes";

export type Plan = {
  flavor: InstallFlavor;
  only?: string[];
  skip?: string[];
  all?: boolean;
  extras?: Extra[];
  command?: string;
};

/** The options after `install.sh`, in a fixed order. */
export function options(plan: Plan) {
  const out = [plan.command, `--flavor ${plan.flavor}`].filter(Boolean) as string[];
  if (plan.all) out.push("--all");
  else if (plan.only?.length) out.push(`--only ${plan.only.join(",")}`);
  if (!plan.all && !plan.only?.length && plan.skip?.length)
    out.push(`--skip ${plan.skip.join(",")}`);
  for (const e of plan.extras ?? []) out.push(`--${e}`);
  return out.join(" ");
}

/** The one line to paste: fetch install.sh and run it. */
export function installCommand(plan: Plan) {
  return `curl -fsSL ${INSTALL_URL} | sh -s -- ${options(plan)}`;
}

/** The same, from a clone of the repo. */
export function cloneCommand(plan: Plan) {
  return `${CLONE} && ./install.sh ${options(plan)}`;
}

/** What to put in ~/.config/subway-seat/config so a bare `install.sh` does the same. */
export function configFile(plan: Plan) {
  const lines = [`flavor=${plan.flavor}`];
  if (!plan.all && plan.only?.length) lines.push(`only=${plan.only.join(",")}`);
  if (!plan.all && !plan.only?.length && plan.skip?.length)
    lines.push(`skip=${plan.skip.join(",")}`);
  return `${lines.join("\n")}\n`;
}
