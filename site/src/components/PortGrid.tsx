import { byCategory, categoryLabel } from "@/lib/manifest";
import { PortFinder } from "./PortFinder";

/** Every port by category, with a filter box and category chips. */
export function PortGrid() {
  const groups = byCategory().map(({ category, ports }) => ({
    category,
    label: categoryLabel(category),
    ports: ports.map((p) => ({ id: p.id, name: p.name, auto: Boolean(p.auto) })),
  }));
  return <PortFinder groups={groups} />;
}
